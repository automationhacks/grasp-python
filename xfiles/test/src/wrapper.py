import yaml
import os


def return_yaml(file_path):
    with open(file_path) as f:
        return yaml.load(f)


def find(name, path=r'C:\Users\gsingh\Dropbox\Technical\Python\TheLearnPythonProject\xfiles\test'):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)