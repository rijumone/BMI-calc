import json
from collections import OrderedDict
import click


BMI_MAP = OrderedDict({
    18.5: {'category': 'Underweight', 'health_risk': 'Malnutrition risk', },
    25: {'category': 'Normal weight', 'health_risk': 'Low risk', },
    30: {'category': 'Overweight', 'health_risk': 'Enhanced risk', },
    35: {'category': 'Moderately obese', 'health_risk': 'Medium risk', },
    40: {'category': 'Severely obese', 'health_risk': 'High risk', },
    999: {'category': 'Very severely obese', 'health_risk': 'Very high risk', },
})

@click.command()
@click.option('-path', '--json-file-path',required=True, \
    type=str, help='File path of text file containing JSON data')
def cli(json_file_path):
    '''TODO click wrapper'''
    main(json_file_path)


def main(json_file_path):
    with open(json_file_path) as _file_obj:
        _data = json.load(_file_obj)

    for row in _data:
        bmi = calc_bmi(
            mass=row['WeightKg'],
            height=row['HeightCm']/100,
        )

        for bmi_value, bmi_details in BMI_MAP.items():
            if bmi < bmi_value:
                row['category'] = bmi_details['category']
                row['health_risk'] = bmi_details['health_risk']
                break

        row['bmi'] = bmi

    print(json.dumps(_data, indent=2))


def calc_bmi(mass, height) -> float:
    '''
    Calculate BMI as per following expression.
    BMI(kg/m^2 ) = mass(kg) / height(m)^2
    Args:
        mass (float): in kg
        height (float): in m
    '''
    return mass/(height**2)


if __name__ == '__main__':
    cli()
