'''
Python module to load JSON data into a `Pandas` dataframe.
BMI is subsequently calculated for each record.
'''
import os
import json
from collections import OrderedDict
import click
import pandas as pd


BMI_MAP = OrderedDict({
    18.5: {'Category': 'Underweight', 'HealthRisk': 'Malnutrition risk', },
    25: {'Category': 'Normal weight', 'HealthRisk': 'Low risk', },
    30: {'Category': 'Overweight', 'HealthRisk': 'Enhanced risk', },
    35: {'Category': 'Moderately obese', 'HealthRisk': 'Medium risk', },
    40: {'Category': 'Severely obese', 'HealthRisk': 'High risk', },
    999: {'Category': 'Very severely obese', 'HealthRisk': 'Very high risk', },
})

BMI_OVERWEIGHT = 25  # bmi greater than this is overweight


def validate(func):
    '''Will validate json_file_path against common errors.'''
    def wrapper(json_file_path):
        if json_file_path is None:
            raise TypeError('json_file_path can\'t be None')
        if not os.path.isfile(json_file_path):
            raise FileNotFoundError(f'{json_file_path} file doesn\'t exist.')
        with open(json_file_path, encoding='utf8') as _j:
            json.load(_j)
        return func(json_file_path)
    return wrapper


@click.command()
@click.option('-path', '--json-file-path', required=True,
              type=str, help='File path of file containing JSON data')
def cli(json_file_path):
    '''Calculate BMI and count overweight.'''
    _output_df = main(json_file_path)
    # _output_data = _output_df.to_json()
    n_overweight = count_by_bmi(_output_df, BMI_OVERWEIGHT)
    n_all = count_by_bmi(_output_df, 0)
    # print(f'Output as JSON:\n{_output_data}')
    print("People who are at least overweight:\n"
          + f"{n_overweight} out of {n_all}\n"
          + f"{n_overweight*100/n_all}%")


@validate
def main(json_file_path):
    '''Entry point of the module. Calculates BMI and count of overweight people.'''
    dataframe = pd.read_json(json_file_path)
    dataframe['BMI'] = dataframe.apply(calc_bmi, axis=1,)
    dataframe['Category'] = dataframe.apply(get_bmi_details, axis=1, args=('Category', ))
    dataframe['HealthRisk'] = dataframe.apply(get_bmi_details, axis=1, args=('HealthRisk', ))
    print(dataframe)
    return dataframe


def calc_bmi(row, ) -> float:
    '''
    Calculate BMI as per following expression.
    BMI(kg/m^2 ) = mass(kg) / height(m)^2
    Args:
        mass (float): in kg
        height (float): in cm
    Returns:
        bmi (float)
    '''
    return row['WeightKg']/((row['HeightCm']/100)**2)


def count_by_bmi(dataframe, bmi):
    '''
    Count greater than equals BMI in dataframe
    Args:
        dataframe (pandas.DataFrame): dataframe which has the BMI column
        bmi: bmi threshold above which row is matched
    Returns:
        count (int)
    '''
    # pylint: disable=simplifiable-if-expression, singleton-comparison
    bmi_series = dataframe.apply(
        lambda x: True if x['BMI'] >= bmi else False, axis=1)
    # Count number of True in bmi_series
    return len(bmi_series[bmi_series == True].index)


def get_bmi_details(row, key):
    '''Will attempt to return BMI details by iterating
    over known BMI ranges details.'''
    for bmi_value, bmi_details in BMI_MAP.items():
        if row['BMI'] < bmi_value:
            return bmi_details[key]
    return None


if __name__ == '__main__':
    # pylint: disable=no-value-for-parameter
    cli()
