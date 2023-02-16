from src.pre_built.counter import count_ocurrences

path = "tests/mocks/jobs.csv"


def test_counter():
    assert count_ocurrences(path, "back") == 1
    assert count_ocurrences(path, "front") == 1
    assert count_ocurrences(path, "full") == 3
    assert count_ocurrences(path, "trainee") == 1
