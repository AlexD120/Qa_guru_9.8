import pytest
import csv


@pytest.fixture
def users():
    with open("users.csv") as f:
        users = list(csv.DictReader(f, delimiter=";"))
    return users


@pytest.fixture
def workers(users):
    """
    Берем только работников из списка
    """
    workers = [
        user for user in users if user["status"] == "worker"
    ]  # - возьми каждого пользователя из списка пользователей со статусом worker и положи в user
    return workers


def user_is_adulr(user):
    return int(user["age"]) >= 18


def test_workers_are_adults_v2(workers):
    """
    Тестируем что все работники старше 18 лет
    """
    for worker in workers:
        assert user_is_adulr(worker), f"Worker {worker['name']} младше 28 лет"
