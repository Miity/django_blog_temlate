import csv
import os
from mainapp.models import Post

def import_csv():
    path = os.path.abspath("import.csv")

    with open(path) as f:
        reader = csv.reader(f)

        for row in reader:
            print('row 4 is: ' + row)

            _, created = Post.objects.get_or_create(
                post_date = row[2],
                update_at = row[3],
                title = row[0],
                slug = row[4],
                content = row[1],
            )

            # creates a tuple of the new object or
            # current object and a boolean of if it was created

import_csv()