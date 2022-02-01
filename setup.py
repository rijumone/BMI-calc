import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='BMI Calc',
    version='0.1',
    description='',
    url='',
    author='Rijumone Choudhuri',
    author_email='mailmeonriju@gmail.com',
    license='MIT',
    packages=['bmi_calc'],
    zip_safe=False,
    install_requires=[
        'click',
        'pytest',
    ],

)
