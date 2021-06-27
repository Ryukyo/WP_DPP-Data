# Challenge_DPP-Data

This script is a solution of Florian Fejer to the DPP data coding challenge

## Structure

- filter.py contains the script with the main method
- data.txt contains sample data in the required format and is the default file used by the filter script
- data2.txt is another file with sample data, which can be used to test the addition of a file path

## How to

Tested on Ubuntu 20.04 and Windows 10 with Python 3.9
Entries in the dataset require the format `<unique record identifier><white_space><numeric value>`

### Run the script

The argument n passed to the main method indicates the n-largest values that should be output.
n <= number of entries in the dataset (i.e. data.txt)

Within the folder containing 'filter.py' run the following command:
`python filter.py`

or to use a data file different from the default 'data.txt':
`python filter.py {path/to/data}`

### Run the tests

### Create test data

Requires numpy installation

Set the parameters in generate_data.py by adjusting:

- n for the number of data entries
- low_id for the smallest possible id
- high_id for the biggest possible id
- max_number for the largest possible number

To generate test data in data2.txt, run the following command:
`python generate_data.py`
