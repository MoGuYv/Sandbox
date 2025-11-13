"""Project class for CP1404 Practical 07.

Represents a project with name, start date, priority, cost estimate,
and percentage completion.
"""

from datetime import date


class Project:
    """Represent a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """
        Create a Project.

        :param name: str
        :param start_date: datetime.date
        :param priority: int (1 = highest priority)
        :param cost_estimate: float (dollars)
        :param completion: int, 0–100
        """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def is_complete(self):
        """Return True if the project is complete (100%)."""
        return self.completion >= 100

    def __lt__(self, other):
        """Compare projects by priority (for sorting)."""
        return self.priority < other.priority

    def __repr__(self):
        """Return programmer-friendly string."""
        return (f"Project({self.name!r}, {self.start_date!r}, "
                f"{self.priority!r}, {self.cost_estimate!r}, {self.completion!r})")

    def __str__(self):
        """Return user-friendly string formatted like the sample output."""
        date_string = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {date_string}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")
