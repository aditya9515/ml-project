from setuptools import setup, find_packages
# conda activate D:\projects\P3_ml-project\ml-project\venv

# def get_requirements():
#     with open('requirements.txt') as f:
#         requirements = f.readlines()
#     return [req.strip() for req in requirements]

setup(
    name='sensor',
    author='Aditya',
    author_email='kosurusai646@gmail.com',
    packages=find_packages(),
    version='0.0.1',
    install_requires=["pymongo==4.2.0"],
)