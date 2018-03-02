from setuptools import setup, find_packages

with open("requirements.txt", 'r') as file:
    requirements = file.readlines()

setup(
    name='ferryman',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/vpanteleev/ferryman',
    license='GNU General Public License v3.0',
    author='Vladimir Panteleev',
    install_requires=requirements,
    author_email='vovapanteleev@gmail.com',
    description='Networking service',
    entry_points={
       'console_scripts': ['hello_world = src.core:hello_world']
       }
)
