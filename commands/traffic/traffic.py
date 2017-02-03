from ndw import NDW

class Traffic():
    def __init__(self):
        self.ndw = NDW()
    
    def _get_parameters(self, message):
        """Get the localion for the traffic.
        
        Keyword arguments:
        message -- the full command with the sentece to translate.
        """
        # clean traffic command
        text_input = message[0].lower().replace("traffic", "", 1)
        
        if "information" in text_input:
            return None
        
        elif "in" not in text_input:
            return None
        
        in_index = text_input.rfind("in")
        location = text_input[in_index + 2:].strip()
        
        return location
    
    def traffic(self, message):
        """
        Returns the traffic information.
        
        Keyword arguments:
        message -- the full command with the location.
        """
        talk = True
        # TODO
        # get the location using the _get_parameters function
        # get the result using the class ndw get general traffic function
        location = self._get_parameters(message)
        result = self.ndw.getGeneralTraffic(location, 3, 10)      
        
        if not result:
            result = "No traffic information for location %s" % location
        
        return talk, result