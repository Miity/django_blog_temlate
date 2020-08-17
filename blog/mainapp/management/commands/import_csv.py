import csv
import itertools
from datetime import timezone
from dateutil.parser import parse
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from mainapp.models import Post, Category


class Command(BaseCommand):
    help = 'Import Posts from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_path', type=Path, help="Path to CSV file to import")

    def handle(self, *args, csv_path, **options):

        category = Category.objects.filter(slug="import").first()

        fieldnames = [
            "post_title",
            "post_date",
            "post_modified",
            "post_name",
            "post_id",
            "cat_desc",
            "cat_type",  # 'category' or 'post_tag'
            "cat_slug",
            "cat_name",
            "post_content"
        ]

        with csv_path.open("r") as f:
            reader = csv.DictReader(f, fieldnames)

            for _, rows in itertools.groupby(reader, key=lambda x: x["post_id"]):
                rows = list(rows)
                category = None
                for r in rows:
                    if r['cat_type'] == "category":
                        category, created = Category.objects.get_or_create(
                            slug=r["cat_slug"],
                            defaults=dict(
                                title=r["cat_name"],
                                desc=r["cat_desc"]
                            )
                        )
                row = rows[0]

                if category is None:
                    print("Category not assigned for row", row["post_name"], row["post_name"])
                    continue

                try:
                    post_date = parse(row["post_date"]).replace(tzinfo=timezone.utc)
                    update_at = parse(row["post_modified"]).replace(tzinfo=timezone.utc)

                    new_content = row["post_content"].find('<!-- wp:gallery')
                    row["post_content"] = row["post_content"][0:new_content]
                    


                    _, created = Post.objects.get_or_create(
                        slug = row["post_name"].strip() or f"import_{row['post_id']}",
                        defaults=dict(
                            post_date = post_date,
                            update_at = update_at,
                            content = row["post_content"].strip(),
                            title = row["post_title"].strip(),
                            category = category
                        )
                    )
                except IntegrityError as err:
                    print(f"Skipping {row[4]} as it is already present: {err}")
                except Exception as err:
                    print(
                        "Failed to process row",
                        row["post_id"], row["post_name"],
                        row["post_date"], row["post_modified"])
