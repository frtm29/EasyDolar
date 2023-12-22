from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(
    name='EasyDolar',
    version="0.1",
    description="Modelo predicción tipo de cambio USD/CLP",
    license="MIT",
    author="EasyDolar",
    author_email="jdcorrea1@miuandes.cl",
    #url="https://github.com/frtm29/EasyDolar",
    install_requires=requirements,
    packages=find_packages(),
    zip_safe=False
    )
