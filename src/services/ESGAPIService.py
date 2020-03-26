import json
import os
from treelib import Tree

from src.configmain import DataMap


#
# class TreeNode(object):
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#
#     def add_child(self, obj):
#         self.children.append(obj)
#
#     def __str__(self, level=0):
#         ret = "\t" * level + repr(self.data) + "\n"
#         for child in self.children:
#             ret += child.__str__(level + 1)
#         return ret
#
#     def __repr__(self):
#         return '<tree node representation>'
#
#
# class Tree:
#     def __init__(self):
#         self.root = TreeNode('ROOT')
#
#     def __str__(self):
#         return self.root.__str__()


res = {}
class ESGData:

    def get_data(self, json_file_location, file_name, name):
        data = {}
        directory = os.path.join(json_file_location)
        for root, dirs, files in os.walk(directory):
            for file in files:
                if str(file).endswith(".json"):
                    if file == file_name:
                        f = open(directory + file, 'r')
                        data = json.load(f)
                        f.close()
                        result = {}
                        result = self.walk(data, name)
        return result

    def walk(self, node, name):
        for k, v in node.items():
            if k == name:
                res[k] = v
                break
            elif isinstance(v, dict):
                self.walk(v, name)
            elif isinstance(v, list):
                for value in v:
                    self.walk(value, name)
        return res
            # else:
            #     print("{0} : {1}".format(k, v))
    #
    # def create_tree_from_JSON(self, data):  # root case
    #     tree = Tree()
    #     node_0 = TreeNode("ROOT")
    #     tree.root = node_0
    #     parent = node_0
    #     self._walk_tree(data, parent)
    #     return tree
    #
    # def _walk_tree(self, data, parent):
    #     node = TreeNode(None)  # recursive case
    #     for key in data:
    #         if isinstance(data[key], dict):
    #             head = TreeNode(key)
    #             self._walk_tree(data[key], head)
    #         else:
    #             node = TreeNode(key)
    #             node.add_child(TreeNode(data[key]))
    #             parent.add_child(node)
    #
    #

