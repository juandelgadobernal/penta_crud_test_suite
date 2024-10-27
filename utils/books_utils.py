import json
import os

def load_data(data_path):
    """
    Loads JSON data from a file located at the specified path.
    :param data_path: str: The relative path to the JSON file to load.
    :return: JSON data from the file
    """
    file_path = os.path.join(os.path.dirname(__file__), data_path)
    with open(file_path) as f:
        return json.load(f)
