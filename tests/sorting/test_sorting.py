from src.pre_built.sorting import sort_by
from src.insights.jobs import read


path = "tests/mocks/jobs_with_salaries_and_date_posted.csv"


def test_sort_by_criteria():
    file = read(path)

    sort_by(file, "min_salary")
    assert file[0]["min_salary"] == "1000"

    sort_by(file, "max_salary")
    assert file[0]["max_salary"] == "8000"

    sort_by(file, "date_posted")
    assert file[0]["date_posted"] == "2021-06-01"
