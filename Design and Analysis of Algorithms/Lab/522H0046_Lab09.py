from typing import List, Dict, Optional, Tuple


class Man:
    """Class to represent a man in the stable marriage problem"""

    def __init__(self, name: str, preference: Dict[str, int]):
        """Initialize a man with name and preference

        Args:
            name (str): Name of the man
            preference (Dict[str, int]): Dictionary of preferences with woman's name as key and rank as value
        """
        self.name: str = name
        self.preference: Dict[str, int] = preference
        self.status: Optional[str] = None
        self.unproposed_preference: List[str] = sorted(
            preference.keys(), key=lambda x: preference[x]
        )

    def __str__(self):
        return f"Man(name={self.name}, status={self.status}, unproposed={self.unproposed_preference})"


class Woman:
    """Class to represent a woman in the stable marriage problem"""

    def __init__(self, name: str, preference: Dict[str, int]):
        """Initialize a woman with name and preference

        Args:
            name (str): Name of the woman
            preference (Dict[str, int]): Dictionary of preferences with man's name as key and rank as value
        """
        self.name: str = name
        self.preference: Dict[str, int] = preference
        self.status: Optional[str] = None

    def __str__(self):
        return f"Woman(name={self.name}, status={self.status})"


def select(men: List[Man]) -> Optional[Man]:
    """Select a free man who still has women to propose to

    Args:
        men (List[Man]): List of men

    Returns:
        Optional[Man]: A free man who has not proposed to all women, or None if no such man exists
    """
    for man in men:
        if man.status is None and man.unproposed_preference:
            return man
    return None


def propose(men: List[Man], women: List[Woman], man: Man) -> None:
    """Make a proposal from a man to a woman

    Args:
        men (List[Man]): List of men
        women (List[Woman]): List of women
        man (Man): The man who is proposing
    """
    woman_name: str = man.unproposed_preference.pop(0)
    woman: Woman = next(w for w in women if w.name == woman_name)

    if woman.status is None:
        woman.status = man.name
        man.status = woman.name
    else:
        current_partner: str = woman.status
        current_partner_rank: int = woman.preference[current_partner]
        new_partner_rank: int = woman.preference[man.name]

        if new_partner_rank < current_partner_rank:
            previous_partner = next(m for m in men if m.name == current_partner)
            previous_partner.status = None

            woman.status = man.name
            man.status = woman.name


def stable_marriage(
    men: List[Man], women: List[Woman]
) -> Tuple[List[Man], List[Woman]]:
    """Perform the stable marriage algorithm

    Args:
        men (List[Man]): List of men
        women (List[Woman]): List of women

    Returns:
        Tuple[List[Man], List[Woman]]: Final pairings of men and women
    """
    unmatched_men: List[Man] = men[:]
    while True:
        free_man: Optional[Man] = select(unmatched_men)
        if not free_man:
            break
        propose(unmatched_men, women, free_man)
        # Remove man from unmatched list after being paired
        unmatched_men = [man for man in unmatched_men if man.status is None]
    return men, women


def main() -> None:
    men: List[Man] = [
        Man("A", {"X": 1, "Y": 2, "Z": 3}),
        Man("B", {"Y": 1, "X": 2, "Z": 3}),
        Man("C", {"Y": 1, "Z": 2, "X": 3}),
    ]

    women: List[Woman] = [
        Woman("X", {"A": 1, "B": 2, "C": 3}),
        Woman("Y", {"B": 1, "A": 2, "C": 3}),
        Woman("Z", {"C": 1, "B": 2, "A": 3}),
    ]

    men, women = stable_marriage(men=men, women=women)

    print("Men pairing:")
    for man in men:
        print(f"{man.name} is paired with {man.status}")

    print("\nWomen pairing:")
    for woman in women:
        print(f"{woman.name} is paired with {woman.status}")


if __name__ == "__main__":
    main()
