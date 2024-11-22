import os
from AlgoTKUCEP import AlgoTKUCEP


def file_to_path(filename: str) -> str:
    """Convert a filename to a full path.

    Args:
        filename (str): The name of the file.

    Returns:
        str: The full path of the file.
    """

    return os.path.abspath(filename)


def main() -> None:
    """Main function to run the TKUCEP algorithm."""
    input_file = file_to_path("DB_Utility.txt")

    output_file = "./output.txt"

    k = 3

    tkucep = AlgoTKUCEP()
    tkucep.run_algorithm(input_file, output_file, k)
    tkucep.print_stats()


if __name__ == "__main__":
    main()
