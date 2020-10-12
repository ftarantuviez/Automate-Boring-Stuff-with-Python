"""  

Using the os.walk() function from Chapter 9, write a script that will go
through every PDF in a folder (and its subfolders) and encrypt the PDFs
using a password provided on the command line. Save each encrypted
PDF with an _encrypted.pdf suffix added to the original filename. Before
deleting the original file, have the program attempt to read and decrypt
the file to ensure that it was encrypted correctly.
Then, write a program that finds all encrypted PDFs in a folder (and its
subfolders) and creates a decrypted copy of the PDF using a provided password. If the password is incorrect, the program should print a message to
the user and continue to the next PDF.

"""
import os, PyPDF2, sys

def encrypt_pdfs(path_dir):
  password = input("put the password for all pdfs: ")

  for folders, subfolders, files in os.walk(path_dir):
    for file in files:
      if file.endswith('.pdf'):
        pdf = open(os.path.join(folders, file), 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        pdf_writer = PyPDF2.PdfFileWriter()
        for pageNumber in range(pdf_reader.numPages):
          pageObj = pdf_reader.getPage(pageNumber)
          pdf_writer.addPage(pageObj)
        
        pdf_output = open(os.path.join(folders, f'_{file}'), 'wb')
        pdf_writer.encrypt(password)
        pdf_writer.write(pdf_output)
        pdf.close()
        pdf_output.close()
        del pdf_output, pdf, pdf_reader, pdf_writer

        print(os.path.join(folders, file) + ' was encrypted succesfully')
      
      else:
        continue
        
def desencrypt_pdfs(path_dir):
  for folders, subfolders, files in os.walk(path_dir):
    for file in files:
      if file.endswith('.pdf'):
        pdf = open(file, 'rb')
        pdf_reader = PyPDF2.PdfFileReader(pdf)
        pdf_writer = PyPDF2.PdfFileWriter()

        if pdf_reader.isEncrypted:
          while True:
            user_password = input("Which is the password to the file " + os.path.join(folders, file))
            if pdf_reader.decrypt(user_password) == 1:
              for pageNumber in range(pdf_reader.numPages):
                pageObj = pdf_reader.getPage(pageNumber)
                pdf_writer.addPage(pageObj)
              
              pdf_output = open(os.path.join(folders, f'd{file}'), 'wb')
              pdf_writer.write(pdf_output)
              pdf.close()
              pdf_output.close()
              del pdf_output, pdf, pdf_reader, pdf_writer
              print(os.path.join(folders, file) + ' was desencrypted succesfully')
              break
            else:
              print('ERROR: PASSWORD INCORRECT')
              continue



if __name__ == "__main__":

  if len(sys.argv) > 0:
    path_dir = sys.argv[1]
    if os.path.exists(path_dir):
      while True:
        user = input("Do you wanna [E]ncrypt pdfs or [D]esencrypt them?:")
        if user.lower() == "e":
          encrypt_pdfs(path_dir)
          sys.exit()
        elif user.lower() == "d":
          desencrypt_pdfs(path_dir)
          sys.exit()
        else:
          continue
    else:
      print("BRO, this folder doesn't exists")
  else:
    print("Put the path of the folder as argument >.<")