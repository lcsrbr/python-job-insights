from src.pre_built.brazilian_jobs import read_brazilian_file


path = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    result = read_brazilian_file(path)
    for row in result:
        keys = [*row.keys()]
        assert keys == ["title", "salary", "type"]
