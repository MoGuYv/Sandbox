"""
Prac 05: Dictionaries - Hex Colours
Estimate: 15 minutes
Actual:   0 minutes
"""

# Store keys normalised to casefolded (lower-like) strings for case-insensitive lookup.
NAME_TO_HEX = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "beige": "#f5f5dc",
    "black": "#000000",
    "blue": "#0000ff",
    "coral": "#ff7f50",
    "crimson": "#dc143c",
    "gold": "#ffd700",
}


def main():
    print("Hex colour lookup (blank to quit)")
    while True:
        name = input("Colour name: ").strip()
        if name == "":
            break
        key = name.casefold()
        code = NAME_TO_HEX.get(key)
        if code:
            # Show canonical title-cased name + code
            print(f"{name.title()}: {code}")
        else:
            print("Invalid colour name")


if __name__ == "__main__":
    main()
