import os

class FileNotFoundError(Exception):
    """Custom exception for file not found errors."""
    pass

class InvalidInputDataError(Exception):
    """Custom exception for invalid input data."""
    pass

class DiskSpaceFullError(Exception):
    """Custom exception for insufficient disk space."""
    pass

def read_input_file(file_path):
    """Read the content of the input file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Input file not found: {file_path}")

def process_text_data(text):
    """Process the text data to count words and character frequencies."""
    if not isinstance(text, str):
        raise InvalidInputDataError("Input data is not a valid string.")

    words = text.split()
    word_count = len(words)
    char_frequency = {}

    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char_frequency[char] = char_frequency.get(char, 0) + 1

    return word_count, char_frequency

def write_output_file(output_path, word_count, char_frequency):
    """Write the processed results to the output file."""
    try:
        with open(output_path, 'w') as file:
            file.write(f"Word Count: {word_count}\n")
            file.write("Character Frequencies:\n")
            for char, freq in char_frequency.items():
                file.write(f"{char}: {freq}\n")
    except OSError as e:
        if e.errno == 28:  # No space left on device
            raise DiskSpaceFullError("Cannot write to output file: Disk space full.")
        else:
            raise

def main():
    input_file_path = input("Enter the path to the input file: ")
    output_file_path = input("Enter the path to the output file: ")

    try:
        # Step 1: Read input data
        text = read_input_file(input_file_path)

        # Step 2: Process text data
        word_count, char_frequency = process_text_data(text)

        # Step 3: Store results
        write_output_file(output_file_path, word_count, char_frequency)

        print("Text processing completed successfully. Results saved to output file.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except InvalidInputDataError as iid_error:
        print(iid_error)
    except DiskSpaceFullError as dsf_error:
        print(dsf_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()