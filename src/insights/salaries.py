from typing import Union, List, Dict
from .jobs import read


def get_max_salary(path: str) -> int:
    jobs_list = read(path)
    max_salary = max(
        int(row["max_salary"])
        for row in jobs_list
        if row["max_salary"].isdigit()
    )

    return max_salary


def get_min_salary(path: str) -> int:
    jobs_list = read(path)
    min_salary = min(
        int(row["min_salary"])
        for row in jobs_list
        if row["min_salary"].isdigit()
    )

    return min_salary


def validate_inputs(job: Dict, salary: Union[int, str]) -> None:
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("values for min_salary and max_salary are required")

    type_salary = type(salary)
    min_salary, max_salary = job["min_salary"], job["max_salary"]

    if (
        (type(min_salary) is not int and not str(min_salary).isdigit())
        or (type(max_salary) is not int and not str(max_salary).isdigit())
        or (type_salary is not int and type_salary is not str)
        or (type_salary is str and not salary.isdigit())
    ):
        raise ValueError("some values are not valid")

    if int(min_salary) > int(max_salary):
        raise ValueError("max_salary must be greater than min_salary")


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validate_inputs(job, salary)

    min_salary, max_salary, salaryInt = (
        int(job["min_salary"]),
        int(job["max_salary"]),
        int(salary),
    )

    return min_salary <= salaryInt <= max_salary


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:

    result = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError as e:
            print(e)

    return result
