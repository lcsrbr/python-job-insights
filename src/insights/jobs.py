from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    with open(path, encoding="utf-8") as file:
        csv_file = csv.DictReader(file, delimiter=",", quotechar='"')
        return [row for row in csv_file]


def get_unique_job_types(path: str) -> List[str]:
    jobs_list = read(path)
    arr = []
    for row in jobs_list:
        if row["job_type"] not in arr:
            arr.append(row["job_type"])
    return arr


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [row for row in jobs if row["job_type"] == job_type]
