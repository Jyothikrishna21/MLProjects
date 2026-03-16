# setup.py file is responsible to create my machine learning application as a package 

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirments(file_path:str)->List[str]:
    '''
        this function will reaturn the list of requirments
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='jyothi krishna',
    author_email='daakuraj21@gmail.com',
    packages=find_packages(),
    install_requires=get_requirments('requirements.txt')
)