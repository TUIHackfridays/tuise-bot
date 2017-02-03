import gzip, os, errno, re
from requests import get
from lxml import etree as et
from lxml import objectify
from geopy.geocoders import Nominatim
from geopy.distance import vincenty


class NDW():
    def __init__(self, target="actuele_statusberichten.xml.gz", area_limit=10):
        """Contructor
        
        Keywords arguments:
        target -- the file to get the information from
        area_limit -- the area size from where to get the traffic information, in km
        """
        self.data_url = "http://opendata.ndw.nu/" + target
        self.target_data = "tmp/" + target
        self.area_limit = area_limit
        self.geolocator = Nominatim()
        self.data = None
        if not os.path.exists(os.path.dirname(self.target_data)):
            try:
                os.makedirs(os.path.dirname(self.target_data))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise


    def _poll_data(self):
        """
        Get the xml gzip file
        """
        r = get(self.data_url, stream=True)
        if r.status_code == 200:
            with open(self.target_data, 'wb') as f:
                f.write(r.content)


    def _parse_data(self):
        """
        Decompress and read the xml file
        """
        with gzip.open(self.target_data, 'rb') as f:
            xmlfile = f.read()
            tree = et.fromstring(xmlfile)
            find = et.XPath('//SOAP:Envelope/SOAP:Body/*',
                            namespaces={"SOAP":"http://schemas.xmlsoap.org/soap/envelope/"})
            d2LogicalModel = et.tostring(find(tree)[0])

            self.data = objectify.fromstring(d2LogicalModel)


    def _text_formatter(self, word):
        """
        Returns the text with a space before every capitalized word.
        
        Keywords arguments:
        word -- string to format
        """
        return re.sub(r"(?<=\w)([A-Z])", r" \1", str(word))


    def getGeneralTraffic(self, location=None, severity_val=3, limit=20):
        """
        Returns the traffic information - situation, duration and location 
        
        Keywords arguments:
        location -- the localion to get the traffic information, default None
        severiry_val -- the level of severity from which to get the traffic information 
            5: highest, 4: high,3: medium, 2: low, 1: lowest, 0: none, -1: unknown, default: 3
        limit -- the maximum number of resut to get, default: 20
        """
#        self._poll_data()
        self._parse_data()
        namespace = "{http://datex2.eu/schema/2/2_0}"
        xsi = "{http://www.w3.org/2001/XMLSchema-instance}"
        severity_values = {
            "highest": 5,
            "high": 4,
            "medium": 3,
            "low": 2,
            "lowest": 1,
            "none": 0,
            "unknown": -1
        }

        if self.data is None:
            return "Sorry but currently I cannot seem to get any traffic information."
        
        
        location_data = None
        
        try:
            if location is not None:
                location_data = self.geolocator.geocode(location)
                print(location_data)
#                print("Location Data:", location_data, self.geolocator.reverse(str(location_data.latitude) + ','  + str(location_data.longitude)).address)
        except Exception as detail:
            print('Error:', detail)
            
        result = []
        situations = self.data.payloadPublication.situation
        for situation in situations:
            if situation.headerInformation.confidentiality == 'noRestriction':
                severity = situation.overallSeverity
                if severity_values[severity] >= severity_val:
                    impact_info = "unknown duration"
                    locations = ""
                    store = True
                    
                    type_of_situation = situation.situationRecord.get(xsi + "type")
                    situationRecord = situation.situationRecord.getchildren()
                    for situationRec in situationRecord:
                        if situationRec.tag == namespace+'impact':
                            impact_info = self._text_formatter(situationRec.delays.delayBand)
                        
                        elif situationRec.tag == namespace+'groupOfLocations' and \
                            (situationRec.get(xsi + "type") == 'Point' or
                            situationRec.get(xsi + "type") == 'Linear' or
                            situationRec.get(xsi + "type") == 'Area'):
                            try:
                                latitude = situationRec.locationForDisplay.latitude
                                longitude = situationRec.locationForDisplay.longitude
                                location = self.geolocator.reverse(str(latitude) + ',' + str(longitude))
                                locations += location.address + "\n"
                                if location_data is not None:
                                    store = vincenty((location_data.latitude, location_data.longitude), 
                                              (latitude, longitude)).km > self.area_limit
                            except Exception as detail:
                                print('Error:', detail)
                                
                        elif situationRec.tag == namespace+'groupOfLocations' and \
                            situationRec.get(xsi + "type") == 'NonOrderedLocationGroupByList':
                            for locationGroup in situationRec.locationContainedInGroup:
                                try:
                                    latitude = locationGroup.locationForDisplay.latitude
                                    longitude = locationGroup.locationForDisplay.longitude
                                    location = self.geolocator.reverse(str(latitude) + ',' + str(longitude))
                                    locations += location.address + "\n"
                                    if location_data is not None:
                                        store = vincenty((location_data.latitude, location_data.longitude), 
                                              (latitude, longitude)).km > self.area_limit
                                except Exception as detail:
                                    print('Error:', detail)
                                    
                        elif situationRec.tag == namespace+'groupOfLocations' and \
                            situationRec.get(xsi + "type") == 'ItineraryByIndexedLocations':
                            if hasattr(situationRec.locationContainedInItinerary.location, 'locationForDisplay'):
                                try:
                                    latitude = situationRec.locationContainedInItinerary.location.locationForDisplay.latitude
                                    longitude = situationRec.locationContainedInItinerary.location.locationForDisplay.longitude
                                    location = self.geolocator.reverse(str(latitude) + ',' + str(longitude))
                                    locations += location.address + "\n"
                                    if location_data is not None:
                                        store = vincenty((location_data.latitude, location_data.longitude), 
                                              (latitude, longitude)).km > self.area_limit
                                except Exception as detail:
                                    print('Error:', detail)
                    
                    if store:
                        if locations == "":
                            locations = "unknown location\n"
                            
                        final_sentence = self._text_formatter(type_of_situation) + " will take " + impact_info + \
                            " in: " + locations
                        result.append((severity_values[severity], final_sentence))
                    
        result = sorted(result, reverse=True, key=lambda item: item[0])
        
        final_result = ""
        
        for text in result[:limit]:
            final_result += text[-1] + '\n'
        
        if final_result == "":
            final_result = "No traffic information for the inputed location."
        
        return final_result


if __name__ == "__main__":
    nwd = NDW()
    nwd.getGeneralTraffic("Hoorn Netherlands", 3, 10)
