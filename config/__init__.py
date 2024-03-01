import yaml
import os


class BaseData:
    filepath = os.path.join(os.path.dirname(__file__), "interface.yaml")
    with open(filepath) as file:
        configdata = yaml.safe_load(file)
