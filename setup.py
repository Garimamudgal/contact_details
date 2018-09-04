from setuptools import setup


with open("ReadMe.txt", 'r') as file:
    long_description = file.read()

setup(
   name='contact_details',
   version='1.0',
   description='A module to handle contact details',
   author='Garima Mudgal',
   author_email='garimamudgalfeb@gmail.com',
   long_description=long_description,
   packages=['contact_details'],
   package_dir={'contact_details': 'contact_details'},
   package_data={'contact_details': ['test.yml'],}
   )