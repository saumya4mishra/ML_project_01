from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Saumya"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return a list of requirement mention in requirements.txt file

    Returns: This function is going to return a list which contains name of libraries mentioned in requirements.txt file

    """
    with open(REQUIREMENTS_FILE_NAME) as req_file:
       return req_file.readlines().remove("-e .")


# Declaring variables for setup functions


setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description="This is my first end-end ML project",
    package=find_packages(),
    install_requires=get_requirements_list()
)
