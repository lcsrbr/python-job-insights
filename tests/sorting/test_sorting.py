from src.pre_built.sorting import sort_by
from src.insights.jobs import read
import csv

path = "tests/mocks/jobs_with_salaries_and_date_posted.csv"


def test_sort_by_criteria():
    with open(path, encoding="utf-8") as file:
        csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
        file_convert = [row for row in csv_file]

    sort_by(file_convert, "min_salary")
    assert file_convert[0]["min_salary"] == "1000"

    sort_by(file_convert, "max_salary")
    assert file_convert[0]["max_salary"] == "8000"

    sort_by(file_convert, "date_posted")
    assert file_convert[0]["date_posted"] == "2021-06-01"
