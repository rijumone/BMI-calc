# BMI Calc

Python module to load JSON data into a `Pandas` dataframe. BMI is subsequently calculated for each record.

## Format of JSON
```json
[
    {
        "Gender":"Female",
        "HeightCm":150,
        "WeightKg":70
    },
    {
        "Gender":"Female",
        "HeightCm":167,
        "WeightKg":82
    }
]
```

## Expression to calcuate BMI
```text
BMI(kg/m^2) = mass(kg) / height(m^2)
```

## Installation
0. Clone or download this repo, `cd` to the directory.
1. Setup a python virtual environment and install dependencies.
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install --upgrade pip wheel setuptools
```
2. Install the project as a module.
```bash
$ pip install -e .
```

## Run tests
```bash
pytest
```

## Usage
```bash
python bmi_calc/main.py -path sample_data.json
```

## Help
```bash
python bmi_calc/main.py --help
```