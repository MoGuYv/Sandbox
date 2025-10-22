"""
Prac 05: Wimbledon
Estimate: 35 minutes
Actual:   0 minutes

Reads 'wimbledon.csv' (UTF-8 with BOM). Expected header includes 'Champion' and 'Country'.
Outputs champion win counts and the set of countries in alphabetical order.
"""

import csv
from collections import Counter
from typing import Iterable


FILENAME = "wimbledon.csv"


def main():
    rows = load_wimbledon(FILENAME)

    champions = [row["Champion"] for row in rows]
    countries = sorted({row["Country"] for row in rows})

    counts = Counter(champions)

    print("Wimbledon Champions:")
    # Keep original insertion order of champions as they first appear in file, but show counts
    for champion, wins in sorted(counts.items(), key=lambda kv: kv[0]):  # alphabetical by name
        print(f"{champion} {wins}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def load_wimbledon(filename: str) -> list[dict[str, str]]:
    """Load CSV rows and normalise to dicts with keys: Year, Champion, Country."""
    with open(filename, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        # Normalise header keys to title-case consistent names
        # Accept common variants like 'winner' or 'champion'
        norm_rows = []
        for row in reader:
            norm = {
                "Year": row.get("Year", row.get("year", "")).strip(),
                "Champion": (row.get("Champion") or row.get("Winner") or row.get("champion") or row.get("winner") or "").strip(),
                "Country": (row.get("Country") or row.get("country") or "").strip(),
            }
            # Only keep rows that have the fields we need
            if norm["Champion"] and norm["Country"]:
                norm_rows.append(norm)
    return norm_rows


if __name__ == "__main__":
    main()
