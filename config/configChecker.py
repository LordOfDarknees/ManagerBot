from os.path import exists
from configparser import ConfigParser, NoOptionError
import logging

class Check:
    def __init__(self):
        self.config = ConfigParser()
        self.bot_values = {'token': "MTE3OTg0MDk3NzU0NDk0OTg0Mg.Gv7DMm.gAbX446wWWgPuxlCYCViyZLvbEVa6gtzB1hJi8", "prefix": "!", "database": "savefiles.db"}
        self.test_values = {"ApiKey": "PLACEHOLDER IN DEFAULT"}
        # Just a small function to write the file
        
        if not exists('config.ini'):
            self.config['Bot'] = self.bot_values
            self.config["CryptoAPI"] = self.test_values
            self.write_file()
        else:
            # Read File
            self.config.read('config.ini')

            # Get the list of sections
            # print(self.config.sections())

            # Check if file has section
            try:
                self.config.read('config.ini')

            # If it doesn't i.e. An exception was raised
            except NoOptionError:
                # setback to default to repair itself
                logging.warn("Something seemed Corrupt in the config file Config file was reset")
                self.config['Bot'] = self.bot_values
                self.config["TestStuff"] = self.test_values
                self.write_file()

    def write_file(self):
        self.config.write(open('config.ini', 'w'))

if __name__ == "__main__":
    Check()
