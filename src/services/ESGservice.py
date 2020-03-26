import configparser
import csv
import os
import uuid

import jsonpickle
import json
from treelib import Tree


class NodeParam(object):
    def __init__(self, source, attr, desc, unique_id):
        self.source = source
        self.attr = attr
        self.desc = desc
        self.uniqueId = unique_id


class ESGDataMapper:
    def construct_tree(self, file_path, child_node_index, json_file_location):

        try:
            directory = os.path.join(file_path)
            for root, dirs, files in os.walk(directory):
                for file in files:
                    if str(file).endswith(".csv"):
                        f = open(directory + file, 'r')
                        csv_reader = csv.reader(f, delimiter=',')
                        row_index = 0
                        filename = os.path.basename(f.name)
                        rows = []
                        dict = {"Root": "root", filename: filename.lower()}
                        esg_tree = Tree()
                        esg_tree.create_node("Root", "root",
                                             data=jsonpickle.encode(NodeParam('source', 'attr', 'desc', 'root'),
                                                                    unpicklable=False))  # root node
                        esg_tree.create_node(filename, filename.lower(), parent='root',
                                             data=jsonpickle.encode(NodeParam('source', 'attr', 'desc', str(uuid.uuid1())),
                                                                    unpicklable=False))

                        for row in csv_reader:
                            rows.append(row)

                        for row in rows:
                            if row_index != 0:
                                column_index = 0
                                # data = row
                                for curr_column in row:
                                    if str(curr_column) + str(row[0]) not in dict:
                                        if column_index > child_node_index:
                                            if "\n" in curr_column:
                                                for rowData in curr_column.splitlines():
                                                    node_id_key = str(rowData) + str(row[0])
                                                    dict[node_id_key] = uuid.uuid1()
                                                    esg_tree.create_node(rowData, dict.get(node_id_key),
                                                                         parent=dict.get(
                                                                             str(row[3]) + str(row[0])),
                                                                         data=jsonpickle.encode(
                                                                             NodeParam((rows[0])[column_index], 'attr',
                                                                                       str(rowData).lower(),
                                                                                       str(dict.get(node_id_key))),
                                                                             unpicklable=False))
                                            elif curr_column != '':
                                                node_id_key = str(curr_column) + str(row[0])
                                                dict[node_id_key] = uuid.uuid1()
                                                esg_tree.create_node(curr_column, dict.get(node_id_key),
                                                                     parent=dict.get(
                                                                         str(row[3]) + str(row[0])),
                                                                     data=jsonpickle.encode(
                                                                         NodeParam((rows[0])[column_index], 'attr',
                                                                                   str(curr_column).lower(),
                                                                                   str(dict.get(node_id_key))),
                                                                         unpicklable=False))
                                        else:
                                            node_id_key = str(curr_column) + str(row[0])
                                            dict[node_id_key] = uuid.uuid1()
                                            if column_index == 0:
                                                esg_tree.create_node(curr_column, dict.get(node_id_key),
                                                                     parent=dict.get(filename),
                                                                     data=jsonpickle.encode(
                                                                         NodeParam((rows[0])[column_index], 'attr',
                                                                                   str(curr_column).lower(),
                                                                                   str(dict.get(node_id_key))),
                                                                         unpicklable=False))
                                            else:
                                                esg_tree.create_node(curr_column, dict.get(node_id_key),
                                                                     parent=dict.get(
                                                                         str(row[column_index - 1]) + str(row[0])),
                                                                     data=jsonpickle.encode(
                                                                         NodeParam((rows[0])[column_index], 'attr',
                                                                                   str(curr_column).lower(),
                                                                                   str(dict.get(node_id_key))),
                                                                         unpicklable=False))
                                    column_index += 1
                            row_index += 1
                        f.close()
            filename = filename.replace(".csv", '')
           # print(json_file_location+"//json//"+filename+".json")
            with open(json_file_location+filename+".json", "w") as outfile:
                outfile.write(esg_tree.to_json(with_data=True))
            esg_tree.save2file(json_file_location+filename+".txt")
            return esg_tree.to_json(with_data=True)
        except OSError:
            print("Path not found exception")
            return 'failed'
        except IOError:
            print('An error occurred trying to read the file.')
            f.close()
            return 'failed'
        except Exception as e:
            print("An error occurred while creating a tree")
            print(e)
            return 'failed'



# try:
#     esgDataMapper = ESGDataMapper()
#     config = configparser.RawConfigParser()
#     config.read('ConfigFile.properties')
#     esgDataMapper.construct_tree(config.get('DataMapperSection', 'files.location'), 3)
# except IOError :
#      print('An error occurred trying to read the config file.')
# except Exception as e:
#     print(e)

