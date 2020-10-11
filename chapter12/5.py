""" 

Write a program that performs the tasks of the previous program in reverse
order: The program should open a spreadsheet and write the cells of column A into one text file, the cells of column B into another text file, and
so on.

"""
import os, sys, openpyxl

def excel_to_text_files(sheet):
  max_column = sheet.max_column
  max_row = sheet.max_row
  
  for i in range(1, max_column + 1):
    text_file = open(f'5_ans{i}.txt', 'w')
    for j in range(1, max_row + 1):
      write = sheet.cell(row=j, column=i).value
      if write == None:
        continue
      else:
        text_file.write(write + '\n')

    text_file.close()
    del text_file



if __name__ == "__main__":

  if len(sys.argv) > 1:
    wb = openpyxl.load_workbook(sys.argv[1])
    sheet = wb[wb.sheetnames[0]]
    excel_to_text_files(sheet)
  else:
    print('BRO, bad args, try again :p')