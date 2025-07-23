import csv

def read_csv(file):
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def write_csv(file, data):
    with open(file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
