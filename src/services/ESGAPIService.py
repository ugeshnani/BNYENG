import json, os


class ESGData:

    def get_data(self, json_file_location, file_name):
        try:
            data = {}
            directory = os.path.join(json_file_location)
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if str(file).endswith(".json"):
                        if file == file_name:
                            f = open(directory + file, 'r')
                            data = json.load(f)
                            print(data)
                            f.close()
            return data
        except Exception as e:
            print(e)
            return "failed"
