from setuptools import find_packages, setup
from typing import List

def get_requirement()->List[str]:
    requirement_list : List[str] = []
    return requirement_list



setup(
    name = 'sensor',
    version="0.0.1",
    author="Abhijeet",
    author_email="thakurabhijeet21urk@gmail.com",
    packages= find_packages(),
    install_requires = get_requirement(), # ["pymongo"]
     
)