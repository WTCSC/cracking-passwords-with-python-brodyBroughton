import argparse, hashlib

def main():

    ''' PARSING '''

    parser = argparse.ArgumentParser(description = 'open_files') # Description for parser

    parser.add_argument('passwords') # Adding the dictionary and password to parser
    
    parser.add_argument('dictionary')
    
    args = parser.parse_args() # Parsing args



    ''' PASSING CONTENTS OF PASSWORDS INTO ARRAY '''
    
    passwordsFile = open(args.passwords, 'r') # Opening the password file
    
    passwordsListArr = [] # Array for all the words in passwords
    
    for password in passwordsFile.readlines(): # For loop to iterate through every line in password
        
        passwordsListArr.append(password.strip()) # Adds each word to an array and strips newline characters

    passwordsFile.close() # Close password file



    ''' PASSING CONTENTS OF WORDLIST INTO ARRAY '''
    
    wordListFile = open(args.dictionary, 'r') # Opening the wordlist file
    
    wordListArr = [] # Array for all the words in wordlist
    
    for word in wordListFile.readlines(): # For loop to iterate through every line in wordlist

        wordListArr.append(word.strip()) # Adds each word to an array and strips newline characters
    
    wordListFile.close() # Close wordlist file



    ''' HASHING WORD LIST '''
    
    hashedWordListArr = [] # Array for the hashed passwords from wordlist

    for password in wordListArr: # For loop to go through each password in the wordlist array

        sha256_hash = hashlib.sha256() # Create a hash object

        currentBytePassword = password.encode() # Converts the password string to byte password
        
        sha256_hash.update(currentBytePassword) # Update the hash object with bytes
        
        currentBytePassword = sha256_hash.hexdigest() # Get the hexadecimal representation of the hash
        
        hashedWordListArr.append(currentBytePassword) # Adds the current hashed password to the hashed word list array



    ''' ITERATING THROUGH USER PASSWORDS AND SEPERATING THE USER HASHED PASSWORDS '''

    crackedPasswords = [] # Final cracked passwords array
    
    hashedPasswords = [] # Hashed user passwords array
    
    tempStr = '' # Temporary string for passing things into cracked array
    
    for user in passwordsListArr: # For loop that goes through the password array
        
        for letter in user: # Another for loop that goes through the whole user string    
            
            tempStr += letter # Adds each letter to the temporary string
            
            user = user[:0] + user[1:] # Remove the 'user:' from the string
            
            if letter == ':': # Checks if the current letter is a colon to add the names of the users 
                
                crackedPasswords.append(tempStr) # Adds the temp string to the cracked passwords array
                
                hashedPasswords.append(user) # Adds just the hashed password to the hashedPasswords array
                
                tempStr = '' # Resets temp string
                
                break # Moves onto the next user
    


    ''' CHECKING IF A USER HASHED PASSWORD MATCHES WITH HASHED WORDLIST '''
    
    for userHash in hashedPasswords: # For loop that goes through the user hashed passwords
        
        if any(userHash == hashWordList for hashWordList in hashedWordListArr): # Checks if the user hash is in the hashed word list
            
            crackedPasswords[hashedPasswords.index(userHash)] += wordListArr[hashedWordListArr.index(userHash)] # Adds the unhashed user password to the cracked passwords array

        else:

            crackedPasswords.pop(hashedPasswords.index(userHash))# If a password isnt found, it removes that user and moves on


    for x in crackedPasswords: # Finally prints out the users and their cracked passwords :)
        
        print(x)   

if __name__ == "__main__":
    main()