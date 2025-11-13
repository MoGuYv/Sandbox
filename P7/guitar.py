"""Guitar class for CP1404 Practicals."""

from datetime import date

CURRENT_YEAR = date.today().year
VINTAGE_AGE = 50


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0.0):
        """Create a Guitar with name, year and cost."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return age of the guitar in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare Guitars by year (for sorting from oldest to newest)."""
        return self.year < other.year
