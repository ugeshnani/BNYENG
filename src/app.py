from flask import Flask, request
from src.configmain import DataMap
from src.services.ESGAPIService import ESGData
from src.services.ESGservice import ESGDataMapper

app = Flask(__name__, template_folder='template')


@app.route("/")
def start():
    return "Welcome to home page"


@app.route('/ESG', methods=['GET'])
def construct_tree():
    esgDataMapper = ESGDataMapper()
    data_map = DataMap("../Config/ConfigFile.properties")
    file_location = data_map.get_file_location()
    json_file_location = data_map.get_json_file_location()
    return esgDataMapper.construct_tree(file_location, 3, json_file_location)


@app.route('/GET_DATA', methods=['GET'])
def get_data():
    esgdata = ESGData()
    name = request.form.get('fileName')
    data_map = DataMap("../Config/ConfigFile.properties")
    json_file_location = data_map.get_json_file_location()
    print(json_file_location)
    return esgdata.get_data(json_file_location, file_name='ESG-Master-Mapping_1-0.json', name = name)


# except Exception as e:
#     print(e)
#     return "An error occurred while construct tree"


if __name__ == "__main__":
    app.secret_key = 'mysecret'
    app.run(host="localhost", port=6007, debug=False)
