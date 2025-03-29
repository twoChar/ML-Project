from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    requirments = [] 
    with open(file_path) as file_obj:
        requirments = file_obj.readlines()
        requirments = [req.replace('\n', '') for req in requirments]
        if HYPHEN_E_DOT in requirments:
            requirments.remove(HYPHEN_E_DOT)
    return requirments

    

setup(
    name='ML-Project',
    version='0.0.1',
    author='twoChar',
    author_email='tucy254@gmail.com',
    package=find_packages(),
    install_requires= get_requirements('requirements.txt')
)