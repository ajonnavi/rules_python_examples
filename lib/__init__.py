import requests
import yaml


def hello_world():
    print("Hello World!")


def requests_version():
    return requests.__version__


def pyyaml_version():
    return yaml.__version__
