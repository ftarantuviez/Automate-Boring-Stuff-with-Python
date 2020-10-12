''' 

Say you have the boring job of removing the first line from several hundred
CSV files. Maybe you’ll be feeding them into an automated process that
requires just the data and not the headers at the top of the columns. You
could open each file in Excel, delete the first row, and resave the file—but
that would take hours. Let’s write a program to do it instead.
The program will need to open every file with the .csv extension in the
current working directory, read in the contents of the CSV file, and rewrite
the contents without the first row to a file of the same name. This will
replace the old contents of the CSV file with the new, headless contents.

At a high level, the program must do the following:
•	 Find all the CSV files in the current working directory.
•	 Read in the full contents of each file.
•	 Write out the contents, skipping the first line, to a new CSV file.
At the code level, this means the program will need to do the following:
•	 Loop over a list of files from os.listdir(), skipping the non-CSV files.
•	 Create a CSV Reader object and read in the contents of the file, using
the line_num attribute to figure out which line to skip.
•	 Create a CSV Writer object and write out the read-in data to the new file.

'''
#! python3
# removeCsvHeader.py - Removes the header from all CSV files in the current
# working directory.
import csv, os

def project_one():
  os.makedirs('projectOne', exist_ok=True)

  # Loop through every file in the current working directory.
  for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
      continue # skip non-csv files
    print('Removing header from ' + csvFilename + '...')
    # Read the CSV file in (skipping first row).
    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
      if readerObj.line_num == 1:
        continue # skip first row
      csvRows.append(row)
    csvFileObj.close()

    # Write out the CSV file.
    csvFileObj = open(os.path.join('projectOne', csvFilename), 'w',
    newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
      csvWriter.writerow(row)
    csvFileObj.close()


if __name__ == "__main__":
    project_one()