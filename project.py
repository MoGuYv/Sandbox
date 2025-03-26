

import datetime


class Project:


    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.percent_complete}%")

    def __lt__(self, other):
        return self.priority < other.priority

    def is_complete(self):
        return self.percent_complete == 100

    def update(self, percent_complete=None, priority=None):
        if percent_complete is not None:
            self.percent_complete = int(percent_complete)
        if priority is not None:
            self.priority = int(priority)
