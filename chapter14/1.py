'''  

Excel-to-CSV Converter
Excel can save a spreadsheet to a CSV file with a few mouse clicks, but if you
had to convert hundreds of Excel files to CSVs, it would take hours of clicking. Using the openpyxl module from Chapter 12, write a program that reads
all the Excel files in the current working directory and outputs them as CSV
files.
334 Chapter 14
A single Excel file might contain multiple sheets; you’ll have to create
one CSV file per sheet. The filenames of the CSV files should be <excel
filename>_<sheet title>.csv, where <excel filename> is the filename of the Excel
file without the file extension (for example, 'spam_data', not 'spam_data.xlsx')
and <sheet title> is the string from the Worksheet object’s title variable.

'''
import os, sys, csv, openpyxl

def convert_excel_to_csv(path_dir):
  os.makedirs('toCsv', exist_ok=True)

  for file in os.listdir(path_dir):
    if file.endswith('.xlsx'):
      wb = openpyxl.load_workbook(os.path.join(path_dir, file))
      for sheetName in wb.sheetnames:
        sheet = wb[sheetName]
        max_column = sheet.max_column + 1
        max_row = sheet.max_row + 1
        csv_rows = []
        for row in range(1, max_row):
          for column in range(1, max_column):
            csv_rows.append(sheet.cell(row=row, column=column).value)
        

        # TODO: write csv
        csv_file = open(os.path.join('toCsv', f'{file}-{sheetName}.csv'), 'w', newline='')
        csv_writer = csv.writer(csv_file)
        csv_file.close()
      wb.close()





if __name__ == "__main__":

  if len(sys.argv) > 1 and os.path.isdir(sys.argv[1]):
    convert_excel_to_csv(sys.argv[1])
  else:
    print("Usage: python 1.py path/to/your/dir/with/excels")

