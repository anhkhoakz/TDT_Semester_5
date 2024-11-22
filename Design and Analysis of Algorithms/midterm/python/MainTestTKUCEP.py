import os
import urllib.parse
from AlgoTKUCEP import AlgoTKUCEP


def file_to_path(filename):
    # Construct the absolute file path
    return os.path.abspath(urllib.parse.unquote(filename))


def main():
    # Input file
    # input_file = file_to_path("DB_Utility.txt")
    input_file = "./DB_Utility.txt"

    # Output file
    output_file = "./output.txt"

    # Number of top-k HUIs
    k = 3

    # Run the algorithm
    tkucep = AlgoTKUCEP()
    tkucep.run_algorithm(input_file, output_file, k)
    tkucep.print_stats()


if __name__ == "__main__":
    main()
