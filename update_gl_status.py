import csv

if __name__ == '__main__':
    csv_in_file = 'Arbel_GL-v3.csv'
    csv_out_file = 'Arbel_GL-v4.csv'
    result_dict = []
    with open(csv_in_file, 'r') as file:
        csv_in_dict = csv.DictReader(file)
        for row in csv_in_dict:
            if 'Pass' in row['Fast Status'] or 'Fail' in row['Fast Status']:
                row['Fast Status'] = ''
            if 'Pass' in row['Slow Status'] or 'Fail' in row['Slow Status']:
                row['Slow Status'] = ''
            result_dict.append(row)


    with open(csv_out_file, 'w', newline='') as file:
        fieldnames = result_dict[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for row in result_dict:
            writer.writeheader()
            writer.writerow(row)





