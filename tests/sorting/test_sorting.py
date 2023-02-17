from src.pre_built.sorting import sort_by

mock = [
    {
        "title": "Web developer",
        "min_salary": "1000",
        "max_salary": "2000",
        "date_posted": "2020-06-07",
    },
    {
        "title": "Front end developer",
        "min_salary": "1000",
        "max_salary": "2000",
        "date_posted": "2021-06-01",
    },
    {
        "title": "Back end developer",
        "min_salary": "1000",
        "max_salary": "3000",
        "date_posted": "2020-10-09",
    },
    {
        "title": "Full stack end developer",
        "min_salary": "4000",
        "max_salary": "8000",
        "date_posted": "2021-01-01",
    },
]


def test_sort_by_criteria():

    sort_by(mock, "min_salary")
    assert mock[0]["min_salary"] == "1000"

    sort_by(mock, "max_salary")
    assert mock[0]["max_salary"] == "8000"

    sort_by(mock, "date_posted")
    assert mock[0]["date_posted"] == "2021-06-01"
