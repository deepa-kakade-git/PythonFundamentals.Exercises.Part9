import json
import os
import pickle


def read_json(filepath):
    try:
        with open(filepath, 'r') as f:  #path to the json file to be read file is opened in read mode
            parsed_json = json.load(f)  # this function loads the data from json file to python object
        return parsed_json  #returns the parsed json data as python object
    except:
        return


def read_all_json_files(dirpath):  # this function returns all json files in the path provided in dirpath
    json_list = []   # creates an empty list to store the path of all the json files
    with os.scandir(dirpath) as filenames:  # os.scandir function is used to iterate over all the dirs specified in the dirpath
        for sfile in filenames:  #this line iterates over each file in the filepath
            if sfile.is_file() and sfile.name.endswith('.json'): # this line checks if the file is file and the extesio if it is .json
                    print(sfile)
                    parsed_json = read_json(sfile.path)
                    json_list.append(read_json(sfile))
    return json_list


# pjson = read_json('link.json')
#
# read_all_json_files('.')

def write_pickle(filepath, data):
    try:
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
        print(f"Data written to {filepath} .")
    except Exception as e:
        print(f"Error while writing to {filepath}: {e}")

def load_pickle(filepath):
    with open(filepath, 'rb') as f:
        x = pickle.load(f)
        return x

if __name__ == '__main__':
    directorypath = '/Users/deepa/Documents/Projects/PythonFundamentals.Exercises.Part9'
    read_all_json_files(directorypath)
