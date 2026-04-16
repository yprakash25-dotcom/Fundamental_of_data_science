def key_value(sentence: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for char in sentence:
        if char == " ":
            continue
        counts[char] = counts.get(char, 0) + 1
    return counts


if __name__ == "__main__":
    sentence = input("Enter a sentence for character counting: ").strip()
    if sentence:
        print(f"Character counts: {key_value(sentence)}")
    else:
        print("No sentence provided.")
