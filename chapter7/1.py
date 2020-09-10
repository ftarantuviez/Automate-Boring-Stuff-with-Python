"""
Strong Password Detection
Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength.

"""
import re

passwordRegex = re.compile('[a-zA-Z0-9]{8,}')

passwordLower = re.compile('[a-z]+[A-Z]+[0-9]+')

def validate_password(password):
    
    match = passwordRegex.search(password)
    
    
    matchTwo = passwordLower.findall(match.group())
    print(matchTwo.group())
    



if __name__ == '__main__':

    user = input('Please, write your password: ')

    validate_password(user)

