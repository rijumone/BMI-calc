'''Unit tests for BMI Calc'''
import json
import pytest
import pandas
# pylint: disable=wildcard-import, unused-wildcard-import
from conftest import *
from bmi_calc import main


def test_non_empty_json_file_path():
    '''
    GIVEN main() function which calculates BMI
    WHEN main() is called without a json_file_path param
    RAISES TypeError
    '''
    with pytest.raises(TypeError):
        main.main(None)


def test_invalid_json_file_path():
    '''
    GIVEN main() function which calculates BMI
    WHEN main() is called with an invalid json_file_path param
    RAISES FileNotFoundError
    '''
    with pytest.raises(FileNotFoundError):
        main.main(json_file_path='foo')

# pylint: disable=redefined-outer-name


def test_valid_json_data(valid_json_contents_file):
    '''
    GIVEN main() function which calculates BMI
    WHEN main() is called with an valid json contents\
        in the json_file_path file
    THEN a Pandas DataFrame is returned having the \
        following columns:
        - Gender
        - HeightCm
        - WeightKg
        - Category
        - HealthRisk
        - BMI
    '''
    output_df = main.main(json_file_path=valid_json_contents_file)

    assert isinstance(output_df, pandas.DataFrame)
    for column in output_df.columns:
        assert column in ['Gender', 'HeightCm',
                          'WeightKg', 'Category', 'HealthRisk', 'BMI', ]


def test_invalid_json_data(invalid_json_contents_file):
    '''
    GIVEN main() function which calculates BMI
    WHEN main() is called with an invalid json contents\
        in the json_file_path file
    RAISES json.decoder.JSONDecodeError
    '''
    with pytest.raises(json.decoder.JSONDecodeError):
        main.main(json_file_path=invalid_json_contents_file)


def test_count_overweight(valid_json_contents_file):
    '''
    GIVEN main() function which calculates BMI\
        and count_by_bmi() function which returns count
    WHEN main() is called with an valid json contents\
        in the json_file_path file with N overweight people
    THEN count_by_bmi() returns N
    '''
    output_df = main.main(json_file_path=valid_json_contents_file)
    assert main.count_by_bmi(output_df, main.BMI_OVERWEIGHT) == 2
