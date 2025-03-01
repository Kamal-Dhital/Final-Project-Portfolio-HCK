# Student Name : Kamal Dhital
# Student Id: 2407046

# This is python program that encrypts and decrypts the text.


# Function to print the welcome statement
def welcome():
    """
    Prints a welcome message to the console and provides an explanation
    of the program's functionality.
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


def enter_message():
    """

    This function prompts the user to enter a message and choose between encryption or decryption.
    It then asks for the shift number and returns the user's choices as input values.

    Returns:
    - userInputOnMode: A string indicating the user's choice of encryption ('e') or decryption ('d').
    - userInputOnMessage: A string representing the message entered by the user.
    - userInputOnShift: An integer representing the shift number chosen by the user.

    """

    flag = False

    while not flag:
        try:
            userInputOnMode = input(
                "Would you like to encrypt (e) or decrypt (d): "
            ).lower()
            if userInputOnMode == "e" or userInputOnMode == "d":
                flag = True
            else:
                print("Invalid Mode")
        except Exception as e:
            print(e)
            print("Invalid Input")

    userInputOnMessage = input(
        f"What message would you like to {'encrypt' if userInputOnMode == 'e' else 'decrypt'}: "
    ).upper()

    while True:
        try:
            userInputOnShift = int(input("What is the shift number: "))
            if userInputOnShift > 0 and userInputOnShift <= 25:
                break
        except ValueError as e:
            print("Invalid Shift")
        except Exception as e:
            print("Enter a valid range")

    return userInputOnMode, userInputOnMessage, userInputOnShift


def encrypt(userInputOnMessage, userInputOnShift):
    """
    Encrypts a message by shifting each letter in the message by a given shift number.

    Parameters:
    - userInputOnMessage (str): The message to be encrypted.
    - userInputOnShift (int): The shift number to be applied to each letter.

    Returns:
    - str: The encrypted message.
    """

    result = ""
    for char in userInputOnMessage:
        if char.isalpha():
            shifted_char = chr(
                (ord(char) - ord("A") + userInputOnShift) % 26 + ord("A")
            )
            result += shifted_char
        else:
            result += char
    return result


def decrypt(userInputOnMessage, userInputOnShift):
    """
    Decrypts an encrypted message by shifting each letter in the message by a given negative shift number.

    Parameters:
    - userInputOnMessage (str): The message to be decrypted.
    - userInputOnShift (int): The negative shift number to be applied to each letter.

    Returns:
    - str: The decrypted message.
    """

    return encrypt(userInputOnMessage, -userInputOnShift)


def is_file(filename):
    """
    Checks if a file exists at the given file path.

    Parameters:
    - filename (str): The path to the file.

    Returns:
    - bool: True if the file exists, False otherwise.

    """

    try:
        with open(filename):
            return True
    except FileNotFoundError as e:
        print(e)
        print("File not found | Please Enter a valid File path")
        return False
    except Exception as e:
        print(e)
        return False


def process_file(filename, userInputOnMode, userInputOnShift):
    """
    Process a file by encrypting or decrypting each line based on the given mode and shift number.

    Parameters:
    - filename (str): The name of the file to be processed.
    - userInputOnMode (str): The mode of operation, either "e" for encryption or any other value for decryption.
    - userInputOnShift (int): The shift number to be applied to each letter.

    Returns:
    - list: A list of encrypted or decrypted lines from the file.

    Raises:
    - FileNotFoundError: If the specified file does not exist.
    """

    result_list = []
    try:
        with open(filename, "r") as file:
            for line in file:
                line = line.strip().upper()
                if userInputOnMode == "e":
                    result_list.append(encrypt(line, userInputOnShift))
                else:
                    result_list.append(decrypt(line, userInputOnShift))
    except FileNotFoundError as err_mesg:
        print(err_mesg)
    return result_list


def write_messages(output):
    """
    Writes the output messages to a file named "results.txt".

    Parameters:
    - output (list): A list of strings representing the output messages.

    Returns:
    - None

    The function opens the "results.txt" file in append mode and writes each output message from the input list on a new line. The function does not return any value.
    """

    with open("results.txt", "a") as file:
        for newOutput in output:
            file.write(newOutput + "\n")


def message_or_file():
    """
    Prompts the user for input on encryption or decryption mode, source type (file or console), message or filename, and shift number.

    Returns a tuple containing the user input values.

    Parameters:
    - None

    Returns:
    - tuple: A tuple containing the following values:
        - userInputOnMode (str): The encryption or decryption mode ('e' or 'd').
        - userInputOnMessage (str): The message to be encrypted or decrypted (None if reading from a file).
        - filename (str): The filename to read from (None if reading from the console).
        - userInputOnShift (int): The shift number to be applied to each letter.

    Raises:
    - None
    """

    flag = False
    while not flag:
        try:
            userInputOnMode = input(
                "Would you like to encrypt (e) or decrypt (d): "
            ).lower()
            if userInputOnMode == "e" or userInputOnMode == "d":
                flag = True
            else:
                print("Invalid Mode")
        except Exception as e:
            print("Invalid Input")

    while True:
        try:
            userInputOnFileOrConsole = input(
                "Would you like to read from a file (f) or the console (c)? "
            ).lower()
            if userInputOnFileOrConsole == "f" or userInputOnFileOrConsole == "c":
                break
            else:
                print("Invalid Source type")
        except Exception as e:
            print(e)

    while True:
        try:
            if userInputOnFileOrConsole == "c":
                userInputOnMessage = input(
                    f"What message would you like to {'encrypt' if userInputOnMode == 'e' else 'decrypt'}: "
                ).upper()
                filename = None
                break
            else:
                while True:
                    try:
                        filename = input("Enter a filename: ")
                        if is_file(filename):
                            break
                    except Exception as e:
                        print("Invalid Filename")
                userInputOnMessage = None
                break
        except Exception as e:
            print(e)

    while True:
        try:
            userInputOnShift = int(input("What is the shift number: "))
            if userInputOnShift > 0 and userInputOnShift <= 25:
                break
        except ValueError as err_mesg:
            print(err_mesg)
        except Exception as e:
            print("Enter a valid range")

    return userInputOnMode, userInputOnMessage, filename, userInputOnShift


def main():
    """
    Runs the main logic of the Caesar Cipher program.

    This function prompts the user for input on encryption or decryption mode, source type (file or console), message or filename, and shift number. It then performs the encryption or decryption based on the user's input and saves the output to a file or displays it on the console.

    Parameters:
    - None

    Returns:
    - None

    (The function starts by calling the 'welcome' function to print a welcome message and provide an explanation of the program's functionality. It then enters a while loop to repeatedly prompt the user for input and perform the encryption or decryption.

    Within the loop, the function calls the 'message_or_file' function to get the user's input values. If the user provides a message, the function calls the 'encrypt' or 'decrypt' function based on the mode and shift number provided by the user. The result is then saved to a file or displayed on the console based on the user's choice.

    If the user provides a filename, the function calls the 'process_file' function to encrypt or decrypt each line in the file based on the mode and shift number provided by the user. The results are then saved to a file named 'results.txt' using the 'write_messages' function.

    After processing the message or file, the function prompts the user if they want to encrypt or decrypt another message. If the user chooses not to, the function prints a goodbye message and exits the loop, ending the program.)
    """

    welcome()

    while True:
        (
            userInputOnMode,
            userInputOnMessage,
            filename,
            userInputOnShift,
        ) = message_or_file()

        if userInputOnMessage:
            result = (
                encrypt(userInputOnMessage, userInputOnShift)
                if userInputOnMode == "e"
                else decrypt(userInputOnMessage, userInputOnShift)
            )

            while True:
                try:
                    consoleDataSave = input(
                        "Do you want to save console data to file(y/n)? "
                    ).lower()
                    if consoleDataSave == "y" or consoleDataSave == "n":
                        break
                except Exception as e:
                    print(
                        "Invalid Input in Console Data Save | Please type (y) to save and (n) to continue without save? "
                    )
            if consoleDataSave == "y":
                with open("results.txt", "a") as file:
                    for results in result:
                        file.write(results)
                    file.write("\n")
                    print(f"Output written to results.txt")

            else:
                print(f"Result: {result}")

        elif filename:
            results = process_file(filename, userInputOnMode, userInputOnShift)
            print(f"Output written to results.txt")
            write_messages(results)

        another_message = input(
            "Would you like to encrypt or decrypt another message? (y/n): "
        ).lower()
        if another_message != "y":
            print("Thanks for using the program, goodbye!")
            break


if __name__ == "__main__":
    main()
