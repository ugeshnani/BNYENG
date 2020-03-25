import configparser as cfg


class DataMap:
    def __init__(self, config):
        self.location = self.read_location_from_config_file(config)
        self.file_location = self.read_file_location_from_config_file(config)
        self.json_file_location = self.read_json_file_location_from_config_file(config)

    @staticmethod
    def read_location_from_config_file(config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('DataMapperSection', 'location')

    @staticmethod
    def read_file_location_from_config_file(config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('DataMapperSection', 'files.location')

    @staticmethod
    def read_json_file_location_from_config_file(config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('DataMapperSection', 'json.files.location')

    def get_location(self):
        return self.location

    def get_file_location(self):
        return self.file_location

    def get_json_file_location(self):
        return self.json_file_location
