""" 
Write a program to read in the contents of several text files (you can make
the text files yourself) and insert those contents into a spreadsheet, with
one line of text per row. The lines of the first text file will be in the cells of
column A, the lines of the second text file will be in the cells of column B,
and so on.
Use the readlines() File object method to return a list of strings, one
string per line in the file. For the first file, output the first line to column 1,
row 1. The second line should be written to column 1, row 2, and so on. The
next file that is read with readlines() will be written to column 2, the next
file to column 3, and so on. 
"""
import os, sys, openpyxl

def text_files_to_excel(files):
  y = 1
  wb = openpyxl.Workbook()
  sheet = wb['Sheet']
  for i in files:
    x = 1
    assert os.path.exists(i), \
      "File doesn't exist " + i

    file = open(i)
    readlines = file.readlines()
    

    for j in readlines:
      sheet.cell(row=x, column=y).value = j
      x += 1
    y += 1
    file.close()
  
  wb.save('4_ans.xlsx')


if __name__ == "__main__":

  if len(sys.argv) > 1:
    text_files_to_excel(sys.argv[1:])
  else:
    print('BRO, bad args, try again :p')