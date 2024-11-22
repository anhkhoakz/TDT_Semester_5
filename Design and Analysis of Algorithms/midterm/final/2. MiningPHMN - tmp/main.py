import os
from AlgoPHMN import AlgoPHMN


def file_to_path(filename: str) -> str:
    """Get the absolute path of a file.

    Args:
        filename (str): the name of the file

    Returns:
        str: the absolute path
    """
    return os.path.abspath(filename)


def main() -> None:
    output = "./output.txt"

    # =======================
    # EXAMPLE FROM THE ARTICLE:
    input = file_to_path("DB_UtilityPerHUIs.txt")
    min_utility = 30
    minPeriodicity = 1  # minimum periodicity parameter (a number of transactions)
    maxPeriodicity = 5  # maximum periodicity parameter (a number of transactions)
    minAveragePeriodicity = 1  # minimum average periodicity (a number of transactions)
    maxAveragePeriodicity = 3  # maximum average periodicity (a number of transactions)
    # =======================

    minimum_length = 1
    maximum_length = 1000

    algo = AlgoPHMN()
    algo.setMinimumLength(minimum_length)
    algo.setMaximumLength(maximum_length)

    algo.runAlgorithm(
        False,
        input,
        output,
        min_utility,
        minPeriodicity,
        maxPeriodicity,
        minAveragePeriodicity,
        maxAveragePeriodicity,
    )

    algo.printStats()


if __name__ == "__main__":
    main()
