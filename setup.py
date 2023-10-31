from setuptools import setup, find_packages

# Read the requirements from the 'requirements.txt' file
with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='endtoend',
    version='1.0.0',
    description='end to end ml project',
    author='Parveen Sharma',
    author_email='parveen11030@email.com',
    url='https://github.com/parveen4646/',
    packages=find_packages(),
    install_requires=install_requires,  # Use the list of requirements from requirements.txt
)
