import sys
import pyperclip

def merge_lines():
    print("Enter multiple lines of text (leave it empty to finish):")
    merged_text = ""
    while True:
        line = input()
        if line == "":
            break
        if merged_text.endswith('-'):
            # Remove the trailing '-' and concatenate without space
            merged_text = merged_text[:-1] + line
        else:
            # Add space before adding new line except if merged_text is empty
            if merged_text:
                merged_text += ' ' + line
            else:
                merged_text = line

    print("\nMerged text:")
    print(merged_text)

    # Copy to clipboard
    pyperclip.copy(merged_text)
    print("\nThe merged text has been copied to your clipboard.")
    merge_lines()


if __name__ == "__main__":
    merge_lines()