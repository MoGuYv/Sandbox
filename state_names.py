"""
Prac 05: Dictionaries - State Names
Estimate: 15 minutes
Actual:   0 minutes
"""

# Constant dictionary of Australian state/territory abbreviations to full names.
STATE_ABBREV_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "WA": "Western Australia",
    "SA": "South Australia",
    "ACT": "Australian Capital Territory",
}


def main():
    """Look up state names by abbreviation with case-insensitive input, print all states formatted,
    and use EAFP (exceptions) instead of LBYL."""
    print("State names lookup")
    # Show all nicely formatted (aligned) once as required
    print_all_states(STATE_ABBREV_TO_NAME)

    # Interactive lookup until blank
    while True:
        short_state = input("Enter short state (blank to quit): ").strip()
        if short_state == "":
            break
        # Case-insensitive: normalise to upper
        key = short_state.upper()
        try:
            full_name = STATE_ABBREV_TO_NAME[key]  # EAFP: try and handle KeyError
        except KeyError:
            print("Invalid short state")
        else:
            print(f"{key} is {full_name}")


def print_all_states(mapping: dict[str, str]) -> None:
    """Print all states and names neatly aligned."""
    # Longest abbreviation width (mostly 2–3, but generalise)
    width = max(len(abbrev) for abbrev in mapping)
    # Sort by abbreviation alphabetically (could also sort by name if desired)
    for abbrev in sorted(mapping):
        print(f"{abbrev:<{width}} is {mapping[abbrev]}")


if __name__ == "__main__":
    main()
