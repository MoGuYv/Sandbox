"""
CP1404/CP5632 Practical 06 - Classes
Author: Lu Junwen
"""

from car import Car

def main():
    """Demo of Car class usage."""
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel added. Current fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)

if __name__ == "__main__":
    main()
