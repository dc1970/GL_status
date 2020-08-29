import csv

if __name__ == '__main__':
    csv_in_file = 'Arbel_GL-v3.csv'
    csv_out_file = 'Arbel_GL-v4.csv'
    stat_file_name = 'DVTool_arbel_gld122g.stat'

    # Load statistics
    fast_stat = {}
    slow_stat = {}
    stat_file = open(stat_file_name, 'r').read().splitlines()
    for line in stat_file:
        l = line.split()
        if l[11] == 'fast':
            fast_stat[l[0]] = l[10]
        if l[11] == 'slow':
            slow_stat[l[0]] = l[10]

    result_dict = []
    # Read CSV to dictionary and update latest results
    with open(csv_in_file, 'r') as file:
        csv_in_dict = csv.DictReader(file)
        for row in csv_in_dict:
            # Update Fast status
            if 'Pass' in row['Fast Status'] or 'Fail' in row['Fast Status']:
                row['Fast Status'] = ''
            if row['Tests'] in fast_stat.keys():
                row['Fast Status'] = fast_stat[row['Tests']]
            # Update slow status
            if 'Pass' in row['Slow Status'] or 'Fail' in row['Slow Status']:
                row['Slow Status'] = ''
            if row['Tests'] in slow_stat.keys():
                row['Slow Status'] = slow_stat[row['Tests']]
            result_dict.append(row)

    # Write updated result to new csv file
    with open(csv_out_file, 'w', newline='') as file:
        fieldnames = result_dict[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in result_dict:
            writer.writerow(row)
