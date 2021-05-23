""" Takes edge legnths as command line inputs as arguments and calculates
    aspects of a cuboid. View function doc-string for more details. """

import argparse

def parse_arguments():
    # Initialise parser and set help description
    parser = argparse.ArgumentParser(description=
        'This script takes 3 inputs. They shall be treated as edges \
        (a, b, c) of a cuboid. The script will output the volume, \
        surface area and sums of the edge lengths of the cuboid \
        and output them to the shell. Results are output to 3 decimal \
        places.')

    # Add arguments and descriptions
    parser.add_argument('input_a', help="Edge 'a' of the cuboid")
    parser.add_argument('input_b', help="Edge 'b' of the cuboid")
    parser.add_argument('input_c', help="Edge 'c' of the cuboid")
    args = parser.parse_args()

    return args


def cuboid_calculator(a, b, c):
    """ Function that calculates the volume, surface area
        and sum of edge lengths of a cuboid. """

    # Conversion is done to cause an error if a non-numeric 
    # value is input to the function
    a = float(a)
    b = float(b)
    c = float(c)

    # Validate that number is positive
    for i in (a, b, c):
        if i <= 0:
            err_msg = f"Error: {i} is a non-positive number."
            print(err_msg)
            return err_msg

    # Run calculations
    volume = a * b * c

    surface_area = 2 * ((a * b) + (a * c) + (b * c))

    sum_of_edge_lengths = 4 * (a + b + c)

    # Store results in dictionary
    results = {
        'input_a': a,
        'input_b': b,
        'input_c': c,
        'volume': volume,
        'surface_area': surface_area,
        'sum_of_edge_lengths': sum_of_edge_lengths
    }

    for key, value in results.items():
        print(f'{key.capitalize()}: {value}')
    return results


if __name__ == "__main__":
    arguments = parse_arguments()
    cuboid_calculator(arguments.input_a, arguments.input_b, arguments.input_c)
