import csv
import os


def import_csv():
    path = os.path.abspath("import.csv")

    with open(path) as f:
        reader = csv.reader(f)

        for row in reader:
            print(row)

            # creates a tuple of the new object or
            # current object and a boolean of if it was created

import_csv()