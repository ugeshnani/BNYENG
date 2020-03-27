import json
import os


import pickle

from treelib import Tree

class ESGData:

    def get_data(self, json_file_location, file_name, name):
        data = {}
        sub_t = Tree()
        directory = os.path.join(json_file_location)
        with open(directory + file_name, 'rb') as config_dictionary_file:
            sub_t = pickle.load(config_dictionary_file)
        return sub_t.subtree(name).to_json(with_data=True)
