import requests
import csv

file_url = 'https://github.com/jcoady/sandbox/blob/main/samplecsv.csv?raw=true'

response = requests.get(file_url)

if response.status_code == 200:
    lines = response.text.splitlines()

    for row in csv.reader(lines):
        print(row)
    
    for line in lines:
        print(line)
else:
    print("Failed to retreive the file. Status code:", response.status_code)