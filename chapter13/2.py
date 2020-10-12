"""  
Say you have an encrypted PDF that you have forgotten the password to,
but you remember it was a single English word. Trying to guess your forgotten password is quite a boring task. Instead you can write a program that will
decrypt the PDF by trying every possible English word until it finds one
that works. This is called a brute-force password attack. Download the text file
dictionary.txt from http://nostarch.com/automatestuff/. This dictionary file contains over 44,000 English words with one word per line.
Using the file-reading skills you learned in Chapter 8, create a list of
word strings by reading this file. Then loop over each word in this list, passing
it to the decrypt() method. If this method returns the integer 0, the password was wrong and your program should continue to the next password.
If decrypt() returns 1, then your program should break out of the loop and
print the hacked password. You should try both the uppercase and lowercase form of each word. (On my laptop, going through all 88,000 uppercase
and lowercase words from the dictionary file takes a couple of minutes. This
is why you shouldn’t use a simple English word for your passwords.)
"""
import PyPDF2, sys, os

def hack_password(file):
  pdf = open(file, 'rb')
  pdf_reader = PyPDF2.PdfFileReader(pdf)

  assert pdf_reader.isEncrypted, \
    "file is not encrypt"
  english_dictionary = open('dictionary.txt')
  all_words = english_dictionary.read().splitlines()
  
  for word in all_words:
    if pdf_reader.decrypt(word) == 1:
      print('THE PASSWORD IS: ' + word)
      break
    elif pdf_reader.decrypt(word.lower()) == 1:
      print('THE PASSWORD IS: ' + word.lower())
      break
    else:
      continue
  
  english_dictionary.close()
  print('Still hacking hahaha ;)')


if __name__ == "__main__":
    
    if len(sys.argv) > 0:
      file = sys.argv[1]
      assert os.path.exists(file) and file.endswith('.pdf'), \
        "File doesn't exist os is not pdf file"
      
      hack_password(file)
    else:
      print("you have to put the file as argument")
      