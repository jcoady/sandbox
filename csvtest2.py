# Python program to read CSV file line by line 
# import necessary packages 
import csv 
import urllib.request  # the lib that handles the url stuff
import codecs

file_url = 'https://github.com/jcoady/sandbox/blob/main/samplecsv.csv?raw=true'

# Open file 
with urllib.request.urlopen(file_url)as file_obj:
    # Create reader object by passing the file 
    # object to reader method 
    reader_obj = csv.reader(codecs.iterdecode(file_obj, 'utf-8'))

    # Iterate over each row in the csv 
    # file using reader object 
    for row in reader_obj: 
        print(row)

