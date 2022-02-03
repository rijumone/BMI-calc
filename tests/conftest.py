'''conftest is responsible to setup fixtures for unit testing.'''
import os
from tempfile import NamedTemporaryFile
import pytest


@ pytest.fixture
def invalid_json_contents_file():
    '''Will create a NamedTemporaryFile containing
    invalid JSON data and yield the same.'''
    with NamedTemporaryFile(delete=False, mode='w') as tmpfile:
        tmpfile.write('foo')
    yield tmpfile.name
    # teardown action
    os.unlink(tmpfile.name)


@ pytest.fixture
def valid_json_contents_file():
    '''Will create a NamedTemporaryFile containing
    valid JSON data and yield the same.'''
    with NamedTemporaryFile(delete=False, mode='w') as tmpfile:
        tmpfile.write('[{"Gender":"Female","HeightCm":150,"WeightKg":70,"BMI":31.11}\
                ,{"Gender":"Female","HeightCm":167,"WeightKg":82,"BMI":29.402}]')
    yield tmpfile.name
    # teardown action
    os.unlink(tmpfile.name)
