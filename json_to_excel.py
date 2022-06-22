import json
import openpyxl
from csv import DictWriter
import csv
# Opening JSON file
f = open('sites.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)



with open('spreadsheet.csv','w') as outfile:
    writer = DictWriter(outfile, ('site_name',
    'site_uid',
    'user_email',
    'is_setup_completed',
    'subscription_name',
    'product_names',
    'products_count',
    'transaction_ref',
    'transaction_id',
    'creation',
    'modified'))
    writer.writeheader()
    writer.writerows(data)

def csv_to_excel(csv_file, excel_file):
    csv_data = []
    with open(csv_file) as file_obj:
        reader = csv.reader(file_obj)
        for row in reader:
            csv_data.append(row)
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    for row in csv_data:
        sheet.append(row)
    workbook.save(excel_file)
if __name__ == "__main__":
    csv_to_excel("spreadsheet.csv", "books.xlsx")

