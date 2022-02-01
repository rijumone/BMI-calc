import pytest
from conftest import *

def test_non_empty_json_file_path():
    '''
    GIVEN main() function which calculates BMI
    WHEN main.main() is called without a None json_file_path param
    RAISES TypeError
    '''
    with pytest.raises(TypeError):
        main.main(None)
