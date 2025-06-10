import re

def extract_dois_from_text(dois):
    # Regular expression pattern for DOIs in the format 10.XXX/XXX
    doi_pattern = r'\b10\.\d{4,9}/\S+\b'
    # Find all DOIs in the text
    found_dois = re.findall(doi_pattern, dois)
    return "\n".join(found_dois)

def remove_reference_numbers(refs):
    refs = refs.strip().splitlines()
    cleaned_references = []
    for ref in refs:
        cleaned_ref = re.sub(r'^\[\d+\]\s*', '', ref)
        cleaned_references.append(cleaned_ref)
    return "\n".join(cleaned_references)

def format_split_email(emails):
    email_pattern = r'<(.*?)>'
    email_addresses = re.findall(email_pattern, emails)
    return "\n".join(email_addresses)

def selectFunc(full_text):
    selFunc = input("What do you need it formatted as?\nAvailable functions:\n(0) Exit\n(1) Extract dois\n(2) Remove any first numerations\n(3) Clear copied emails from Yandex\nChoose a function: ")
    match selFunc:
        case "0":
            exit()
        case "1":
            return extract_dois_from_text(full_text)
        case "2":
            return remove_reference_numbers(full_text)
        case "3":
            return format_split_email(full_text)
        case "":
            print("!!!Empty field. Try again.\n")
            selectFunc(full_text)
        case _:
            print("!!!Wrong input. Enter a number to select it, f.e. enter 0 to select exit.\n")
            selectFunc(full_text)
        
def writeToFile(fText):
    output_file = "formatted-text.txt"
    with open(output_file, "w", encoding='utf-8') as f:
        if fText:
            f.write(fText)
            print(f"Formatted text have been written to '{output_file}'.")
        else:
            print("!!!No text found. Try again.")
            main()

def main():

    print("Enter text (press Enter to finish):")
    
    # Initialize an empty string to collect input
    full_text = ""
    
    while True:
        # Read a line of input from the user
        line = input()
        
        # Break the loop if the input is empty
        if line.strip() == "":
            break
        
        # Append the line to the full text
        full_text += line + "\n"

    if(full_text == ""):
        print("!!!Empty field. Try again.\n")
        main()
    # Select what to do with the inputted text and output formatted text
    fText = selectFunc(full_text)
    print("\n"+fText+"\n")
    writeToFile(fText)

if __name__ == "__main__":
    main()