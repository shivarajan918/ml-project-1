from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."

def get_requirements(file_path):

#this function returns list of requirements.

    requirements=[]
    with open(file_path) as file_obj:
         requirements= file_obj.readlines()
         requirements = [req.replace("\n","") for req in requirements]
     
         if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

     
setup(
name= 'ml-project-1',
version='0.0.1',
author='shivarajan',
author_email='shivarajan918@gmail.com',
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)