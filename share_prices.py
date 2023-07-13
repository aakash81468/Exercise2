import csv

def find_highest_share_month(csv_file):
    # Dictionary to store the highest share month and year for each company
    highest_share_months = {}

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames

        # Remove 'Year' and 'Month' from the headers
        companies = headers[2:]

        for company in companies:
            highest_share_month = None
            highest_share_value = float('-inf')

            for row in reader:
                share_value = float(row[company])

                if share_value > highest_share_value:
                    highest_share_value = share_value
                    highest_share_month = row['Month'] + ' ' + row['Year']

            highest_share_months[company] = highest_share_month

            # Reset the reader to the beginning of the file
            file.seek(0)
            next(reader)

    return highest_share_months

csv_file = '/Users/aakash.soni/Documents/LearningPython/Assessment/share_prices.csv'
result = find_highest_share_month(csv_file)

for company, month in result.items():
    print(f"{company}: {month}")
