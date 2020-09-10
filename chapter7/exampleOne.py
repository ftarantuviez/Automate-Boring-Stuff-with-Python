import re


# d is for digit
def digitsCharacter():

    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search('My number is 415-555-4242.')
    print('Phone number found: ' + mo.group())



# | Pipe Is like OR. If there are two, returns the first
def pipeCharacter():
    heroRegex = re.compile (r'Batman|Tina Fey')
    mo1 = heroRegex.search('Batman and Tina Fey.')
    print(mo1.group())
     
    mo2 = heroRegex.search('Tina Fey and Batman.')
    print(mo2.group())


# ? is to optional pattern

def optional():
    batRegex = re.compile(r'Bat(wo)?man')
    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())
    
    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())


# * is to say find 0 or more
def zeroOrMore():
    batRegex = re.compile(r'Bat(wo)*man')
    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())
    
    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())

    mo3 = batRegex.search('The Adventures of Batwowowowoman')
    print(mo3.group())


def oneOrMore():
     batRegex = re.compile(r'Bat(wo)+man')
     mo1 = batRegex.search('The Adventures of Batwoman')
     print(mo1.group())
     
     mo2 = batRegex.search('The Adventures of Batwowowowoman')
     print(mo2.group())
     
     mo3 = batRegex.search('The Adventures of Batman')
     print(mo3 == None)
    

if __name__ == '__main__':
    
    oneOrMore()
