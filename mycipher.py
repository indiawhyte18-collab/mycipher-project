import sys

def main():
    # 1. Get shift from command line
    shift = int(sys.argv[1])

    # 2. Read input from stdin
    text = ""
    for line in sys.stdin:
        text += line

    # 3. Convert to uppercase and shift letters
    result = ""

    for char in text:
        if char.isalpha():  # only letters
            char = char.upper()

            # Convert to number (A=0 ... Z=25)
            position = ord(char) - ord('A')

            # Shift
            new_position = (position + shift) % 26

            # Convert back to letter
            new_char = chr(new_position + ord('A'))

            result += new_char

    # 4. Print in blocks of 5, 10 blocks per line
    block_count = 0

    for i in range(0, len(result), 5):
        block = result[i:i+5]
        print(block, end="")

        block_count += 1

        if block_count % 10 == 0:
            print()
        else:
            print(" ", end="")

    # Final newline if needed
    if block_count % 10 != 0:
        print()


if __name__ == "__main__":
    main()
