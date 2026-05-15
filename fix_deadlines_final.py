import csv
import re

input_file = 'australian_science_prizes_expanded.csv'
output_file = 'temp.csv'

with open(input_file, mode='r', encoding='utf-8') as f:
    reader = list(csv.reader(f))
    header = reader[0]
    data = reader[1:]

d_idx = header.index('Deadline')

new_data = []
for row in data:
    if not row:
        continue
    d = row[d_idx]
    
    # If it contains two years separated by a comma/space, e.g. "2027, 2026"
    # we should take the first one (the original one)
    d = re.sub(r'(\d{4}),\s*\d{4}', r'\1', d)
    
    # Clean up any trailing ", 2026" that shouldn't be there
    # (if there's already a year)
    if d.count('202') > 1:
         # Take the first occurrence of a year
         parts = re.split(r'(202\d)', d)
         if len(parts) > 2:
             d = "".join(parts[:2])
    
    row[d_idx] = d
    new_data.append(row)

with open(output_file, mode='w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(new_data)
