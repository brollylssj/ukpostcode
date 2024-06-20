# UK Postcode Library

A Python library to validate and format UK postcodes.

## Installation

You can install the library using pip:

```pip install ukpostcode```

You can install the library directly from the GitHub repository:

```sh
pip install git+https://github.com/brollylssj/ukpostcode.git
```

### Install Dependencies
Install the necessary dependencies using the provided requirements.txt file:

```pip install -r requirements.txt```


## Usage

```python
from ukpostcode import UKPostcode

postcode = "EC1A1BB"
uk_postcode = UKPostcode(postcode)
print(uk_postcode)  # Output: EC1A 1BB
print(uk_postcode.get_outward_code())  # Output: EC1A
print(uk_postcode.get_inward_code())  # Output: 1BB
```

## Usage Instructions
To use the library from the command line, you can now run:

```sh
python -m ukpostcode "M1 1AE" 
```

## Testing
To run the tests, use:

```sh
pytest
```

