import argparse, hashlib

def main():

    ''' PARSING '''

    # Description for parser
    parser = argparse.ArgumentParser(description = 'open_files')

    # Adding the dictionary and password to parser
    parser.add_argument('dictionary')

    parser.add_argument('passwords')
    
    # Parsing args
    args = parser.parse_args()



    ''' PASSING CONTENTS OF WORDLIST INTO ARRAY '''

    # Opening the wordlist file
    wordListFile = open(args.dictionary, 'r')
    
    # Array for all the words in wordlist
    wordListArr = []

    # For loop to iterate through every line in wordlist
    for word in wordListFile.readlines():

        # Adds each word to an array and strips newline characters
        wordListArr.append(word.strip())
    
    # Close wordlist file
    wordListFile.close()



    ''' PASSING CONTENTS OF PASSWORDS INTO ARRAY '''

    # Opening the wordlist file
    passwordsFile = open(args.passwords, 'r')
    
    # Array for all the words in wordlist
    passwordsListArr = []

    # For loop to iterate through every line in wordlist
    for password in passwordsFile.readlines():

        # Adds each word to an array and strips newline characters
        passwordsListArr.append(password.strip())

    # Close wordlist file
    passwordsFile.close()



    ''' HASHING WORD LIST '''

    # Array for the hashed passwords from wordlist
    hashedWordListArr = []

    # Create a hash object
    sha256_hash = hashlib.sha256()

    # For loop to go through each password in the wordlist array
    for password in wordListArr:

        # Converts the password string to byte password
        currentBytePassword = password.encode()

        # Update the hash object with bytes
        sha256_hash.update(currentBytePassword)

        # Get the hexadecimal representation of the hash
        currentBytePassword = sha256_hash.hexdigest()

        # Adds the current hashed password to the hashed word list array
        hashedWordListArr.append(currentBytePassword)



    ''' ITERATING THROUGH '''

    # Final cracked passwords array
    crackedPasswords = []

    # Temporary string for passing things into cracked array
    tempStr = ''

    # For loop that goes through the password array
    for user in passwordsListArr:

        # Another for loop that goes through the whole user string
        for letter in user:
            
            # Adds each letter to the temporary string
            tempStr += letter

            # Checks if the current letter is a colon to add the names of the users
            if letter == ':':

                # Adds the temp string to the cracked passwords array
                crackedPasswords.append(tempStr)

                # Resets temp string
                tempStr = ''

                # Moves onto the next user
                break
            
if __name__ == "__main__":
    main()