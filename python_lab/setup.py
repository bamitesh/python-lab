from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    Args:
        file_path (str): path of requirements.txt file
    Returns:
        List[str]: list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            
        
    return(requirements)




setup(
    name='python_lab',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/bamitesh/python-lab.git',
    license='MIT',
    author='amitesh bhattacharya',
    author_email='b.amitesh@outlook.com',
    description='A Python package for the lab',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=get_requirements('requirements.txt')    
    
    
    
)
