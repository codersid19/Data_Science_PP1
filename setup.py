from setuptools import setup, find_packages
from typing import List

setup_run = "-e ."
def get_req(req_file_path:str)->List[str]:
    requirements= []
    with open(req_file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if setup_run in requirements:
            requirements.remove(setup_run)
    
    return requirements

setup(
    name="Data_Science_PP1",
    version="0.0.1",
    author="Siddhant Shirodkar",
    author_email="siddhant19shirodkar12@gmail.com",
    packages=find_packages(),
    install_requires = get_req('requirements.txt')
)