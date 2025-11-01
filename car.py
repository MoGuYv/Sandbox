"""
CP1404/CP5632 Practical 06 - Classes
Author: Lu Junwen
"""

class Car:
    """Represent a car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a Car instance.

        name: str, car's name
        fuel: int, one unit of fuel drives one kilometre
        """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of the car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add the given amount of fuel to the car."""
        if amount < 0:
            print("Fuel amount must be >= 0")
        else:
            self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance.

        Drive given distance if enough fuel,
        or drive until fuel runs out. Return the distance driven.
        """
        if distance < 0:
            print("Distance must be >= 0")
            return 0

        if distance > self.fuel:
            distance_driven = self.fuel
            self.odometer += self.fuel
            self.fuel = 0
            print(f"The car drove {distance_driven}km and ran out of fuel.")
            return distance_driven
        else:
            self.fuel -= distance
            self.odometer += distance
            print(f"The car drove {distance}km.")
            return distance
