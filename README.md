# Cuboid Calculator

## Using the script

The script is very simple and takes command line inputs. 
You may run "python3 script.py --help" to view the options.
An example use would be "python3 script.py 7 4 2.3"

To run tests you must activate the venv with:
` source myenv/bin/activate `
and then execute
` python -m pytest test.py `

## Testing

### Scenario 1

The scenario should test that the script performs as expected
and that it can accurately perform the required calculations of
a cuboid. These are: volume, surface area, sums of the edge lengths

| Test Case                  | Acceptance Criteria           | Status |
| ---------------------------| ----------------------------- | ------ |
| Input values 4, 9, 12 and  | result['volume'] == 432       | Passed |
| verify the volume returned |                               |        |
| -------------------------- | ----------------------------- | ------ |
| Input values 4, 9, 12 and  | result['surface_area'] == 384 | Passed |
| verify the surface area    |                               |        |
| returned                   |                               |        |
| -------------------------- | ----------------------------- | ------ |
| Input values 4, 9, 12 and  | result['sum_of_edge_lengths'] | Passed |
| verify the sum of the edge | == 100                        |        |
| lengths returned           |                               |        |
| ---------------------------| ----------------------------- | ------ |


### Scenario 2

Users may attempt to input a string into the calculator, such as 
writing "Four" instead of "4". The calculator should be able to handle
this gracefully, by providing a meaningful error message. A test should
input a string into the calculator and verify that an appropriate
exception is raised.

| Test Case                     | Acceptance Criteria          | Status |
| ------------------------------| ---------------------------- | ------ |
| Input string as argument for  | ValueError could not convert | Passed |
| cuboid_calculator()           | string to float: '<STRING>') |        |
| ----------------------------- | ---------------------------- | ------ |

### Scenario 3

It does not make sense to non-positive numbers to this calculator.
If this happens it is likely to have been done in error, in which case
it would be helpful for the user to see an appropriate error message
rather than receive potentially confusing results.

| Test Case                        | Acceptance Criteria          | Status |
| -------------------------------- | ---------------------------- | ------ |
| Input non-positive number as     | Error: <NON-POSITIVE NUMBER> | Passed |
| argument for cuboid_calculator() | is a non-positive number.    |        |
| -------------------------------- | ---------------------------- | ------ |

