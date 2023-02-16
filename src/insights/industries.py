from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_list = read(path)
    arr = []
    for row in jobs_list:
        if row["industry"] not in arr and len(row["industry"]):
            arr.append(row["industry"])
    return arr


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [row for row in jobs if row["industry"] == industry]
