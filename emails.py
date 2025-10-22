"""
Prac 05: Word Occurrences
Estimate: 25 minutes
Actual:   0 minutes
"""

def main():
    text = input("Text: ").strip()
    counts: dict[str, int] = {}

    # Count occurrences, case-insensitive; split by whitespace
    for word in text.split():
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1

    # Sort by word (key)
    sorted_items = sorted(counts.items(), key=lambda kv: kv[0])

    # Compute width = longest word length for alignment
    width = max((len(word) for word, _ in sorted_items), default=0)

    for word, count in sorted_items:
        # Align numbers in a neat column: "word .... : n"
        print(f"{word:{width}} : {count}")


if __name__ == "__main__":
    main()
