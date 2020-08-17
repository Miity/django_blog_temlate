import csv
import os
import re

def import_csv():
    path = os.path.abspath("import.csv")

    with open(path, 'w') as f:
        reader = csv.reader(f)

        for row in reader:

            content = row[1]
            start = content.find('<!-- wp:gallery')
            row[1] = row[1][0:start]



            # _, created = Post.objects.get_or_create(
            #     post_date = row[2],
            #     update_at = row[3],
            #     content = row[1],
            #     title = row[0],
            #     slug = row[4],
            # )

            # creates a tuple of the new object or
            # current object and a boolean of if it was created

import_csv()