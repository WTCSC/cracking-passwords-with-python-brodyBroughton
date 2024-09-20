import argparse, hashlib

def main():

    ''' PARSING '''

    # Description for parser
    parser = argparse.ArgumentParser(description = 'open_files')

    # Adding the dictionary and password to parser
    parser.add_argument('passwords')
    
    parser.add_argument('dictionary')
    
    # Parsing args
    args = parser.parse_args()



    ''' PASSING CONTENTS OF PASSWORDS INTO ARRAY '''
    try:
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
    except FileNotFoundError:
        print('File not found')


    ''' PASSING CONTENTS OF WORDLIST INTO ARRAY '''
    try:
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
    except FileNotFoundError:
        print('File not found')

    ''' HASHING WORD LIST '''

    # Array for the hashed passwords from wordlist
    hashedWordListArr = []   

    # For loop to go through each password in the wordlist array
    for password in wordListArr:

        # Create a hash object
        sha256_hash = hashlib.sha256()

        # Converts the password string to byte password
        currentBytePassword = password.encode()

        # Update the hash object with bytes
        sha256_hash.update(currentBytePassword)

        # Get the hexadecimal representation of the hash
        currentBytePassword = sha256_hash.hexdigest()

        # Adds the current hashed password to the hashed word list array
        hashedWordListArr.append(currentBytePassword)



    ''' ITERATING THROUGH USER PASSWORDS AND SEPERATING THE USER HASHED PASSWORDS '''

    # Final cracked passwords array
    crackedPasswords = []

    # Hashed user passwords array
    hashedPasswords = []

    # Temporary string for passing things into cracked array
    tempStr = ''

    # For loop that goes through the password array
    for user in passwordsListArr:

        # Another for loop that goes through the whole user string
        for letter in user:
            
            # Adds each letter to the temporary string
            tempStr += letter

            # Remove the 'user:' from the string
            user = user[:0] + user[1:]
        
            # Checks if the current letter is a colon to add the names of the users
            if letter == ':':
                
                # Adds the temp string to the cracked passwords array
                crackedPasswords.append(tempStr)

                # Adds just the hashed password to the hashedPasswords array
                hashedPasswords.append(user)

                # Resets temp string
                tempStr = ''

                # Moves onto the next user
                break
    


    ''' CHECKING IF A USER HASHED PASSWORD MATCHES WITH HASHED WORDLIST 
    user = 0
    
    for userHash in hashedPasswords:

        # For loop that goes through the hashed words in the hashed word list array
        for hashWordList in hashedWordListArr:
            
            # Finally checks if the user password hash matches up with the hashed word
            if userHash == hashWordList:
                #print(user)
                unhashedPassword = wordListArr[hashedWordListArr.index(userHash)]

                crackedPasswords[user] += unhashedPassword

                user += 1
    '''
    for userHash in hashedPasswords: # For loop that goes through the user hashed passwords
        
        if any(userHash == hashWordList for hashWordList in hashedWordListArr): # Checks if the user hash is in the hashed word list
            
            crackedPasswords[hashedPasswords.index(userHash)] += wordListArr[hashedWordListArr.index(userHash)] # Adds the unhashed user password to the cracked passwords array

        else:

            crackedPasswords.pop(hashedPasswords.index(userHash))# += '' # If not found, adds nothing
            
    for x in crackedPasswords:
        
        print(x)   
if __name__ == "__main__":
    main()