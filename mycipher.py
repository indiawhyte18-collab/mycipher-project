import sys

def main():
    shift = int(sys.argv[1])

    text = ""
    for line in sys.stdin:
        text += line

    result = ""

    for char in text:
        if char.isalpha():  
            char = char.upper()

            position = ord(char) - ord('A')

            new_position = (position + shift) % 26

            new_char = chr(new_position + ord('A'))

            result += new_char

    block_count = 0

    for i in range(0, len(result), 5):
        block = result[i:i+5]
        print(block, end="")

        block_count += 1

        if block_count % 10 == 0:
            print()
        else:
            print(" ", end="")

    if block_count % 10 != 0:
        print()


if __name__ == "__main__":
    main()
