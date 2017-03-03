import sqlite3 as db

class Database():


    def __init__(self):
        self.dbpath = 'db/tuise_database.db'
        try:
            # connecto to database, will create it if it doesn't exist
            conn = db.connect(self.dbpath)
            # try to create the tables if they don't exist
            f = open('db/create_tables.sql', 'r')
            sql = f.read()
            cur = conn.cursor()
            cur.executescript(sql)
            conn.commit()
        except db.Error, e:
            if conn:
                conn.rollback()
            print "Error: %s" % e.args[0]
        finally:
            if conn:
                conn.close() 
        
        
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d


    def get_all_chat_response(self):
        """
        Gets all the responses in the database.
        """
        result = None
        try:  
            conn = db.connect(self.dbpath)
            conn.row_factory = self.dict_factory
            cur = conn.cursor()
            cur.execute("SELECT * FROM chat_responses")
            result = cur.fetchall()
        except db.Error, e:
            print "Error: %s" % e.args[0]
        finally:
            if conn:
                conn.close()
        return result


    def get_chat_response(self, text):
        """
        Gets the response in the database that matches the trigger
        detected in the inputed text

        Keyword arguments:
        text -- the text where to find triggers on
        """
        result = None
        try:  
            conn = db.connect(self.dbpath)
            conn.row_factory = self.dict_factory
            cur = conn.cursor()
            cur.execute("SELECT id FROM triggers_search WHERE trigger MATCH ?;", ("'" + str(text).lower() + "'", ))
            result_data = cur.fetchone()
            result_id = None
            if result_data is not None:
                result_id = result_data["id"]
            cur.execute("SELECT response FROM chat_all WHERE trigger_id = ?", (result_id,))
            result = cur.fetchone()
        except db.Error, e:
            print "Error: %s" % e.args[0]
        finally:
            if conn:
                conn.close()
        return result


    def set_new_chat_response(self, trigger, response):
        """
        Sets the trigger and the corresponding response in the database

        Keyword arguments:
        trigger -- the sentence, group of words
        response -- the response that matches the trigger
        """
        result = True
        try:
            conn = db.connect(self.dbpath)
            cur = conn.cursor()
            cur.execute("INSERT INTO chat_triggers (trigger) VALUES (?)", (trigger.lower(),))
            trigger_id = cur.lastrowid
            cur.execute("INSERT INTO triggers_search (id, trigger) VALUES (?, ?)", (trigger_id, trigger.lower()))
            cur.execute("INSERT INTO chat_responses (response) VALUES (?)", (response,))
            response_id = cur.lastrowid
            cur.execute("INSERT INTO chat_triggers_responses (triggerId, responseId) VALUES (?, ?)", (trigger_id, response_id))
            conn.commit()
        except db.Error, e:
            if conn:
                conn.rollback()
            result = False
            print "Error: %s" % e.args[0]
        finally:
            if conn:
                conn.close()
        
        return result
    

    def set_chat_response(self, trigger, response_id):
        """
        Sets the trigger with a corresponding response in the database

        Keyword arguments:
        trigger -- the sentence, group of words
        response_id -- the response id that will match the trigger
        """
        result = True
        try:
            conn = db.connect(self.dbpath)
            cur = conn.cursor()
            cur.execute("INSERT INTO chat_triggers (trigger) VALUES (?)", (trigger.lower(),))
            trigger_id = cur.lastrowid
            cur.execute("INSERT INTO chat_triggers_responses (triggerId, responseId) VALUES (?, ?)", (trigger_id, response_id))
            conn.commit()
        except db.Error, e:
            if conn:
                conn.rollback()
            result = False
            print "Error: %s" % e.args[0]
        finally:
            if conn:
                conn.close()
        
        return result


    def get_all_bot_settings(self):
        """
        Returns the bot configuration settings
        """
        result = None
        try:
            conn = db.connect(self.dbpath)
            conn.row_factory = self.dict_factory
            cur = conn.cursor()
            cur.execute("select * from bot_settings")
            result = cur.fetchall()
        except db.Error, e:
            print "Error: %s" % e.args[0]
        finally:
            if conn:
                conn.close()
        return result


    def get_bot_setting(self):
        """
        Returns the bot configuration settings
        """
        result = None
        try:
            conn = db.connect(self.dbpath)
            conn.row_factory = self.dict_factory
            cur = conn.cursor()
            cur.execute("select * from bot")
            bot = cur.fetchone()
            cur.execute("select * from bot_settings where id = ?", (bot['setting'],))
            result = cur.fetchone()
        except db.Error, e:
            print "Error: %s" % e.args[0]
        finally:
            if conn:
                conn.close()
        return result
        
    
    def get_translation_voices(self):
        """
        Returns the translation voices
        """
        result = None
        try:
            conn = db.connect(self.dbpath)
            # get result as string not tuple
            conn.row_factory = lambda cursor, row: row[0]
            cur = conn.cursor()
            cur = conn.cursor()
            cur.execute("select language from translation_voices")
            result = cur.fetchall()
        except db.Error, e:
            print "Error: %s" % e.args[0]
        finally:
            if conn:
                conn.close()
        return result
        
        
    def set_bot_setting(self, bot_id):
        """
        Sets the bot configuration settings

        Keyword arguments:
        bot_id -- that matches the configuration to use
        """
        result = True
        try:
            conn = db.connect(self.dbpath)
            cur = conn.cursor()
            cur.execute("UPDATE bot SET setting=? WHERE id=?", (bot_id, 1))        
            conn.commit()
        except db.Error, e:
            if conn:
                conn.rollback()
            result = False
            print "Error: %s" % e.args[0]
        finally:
            if conn:
                conn.close()
        
        return result
