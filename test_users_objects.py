import pytest
from models.provider import (
    UserProvider,
    CsvUserProvider,
    ApiUserProvider,
    DatabaseUserProvider,
)
from models.users import User, USER_ADULT_AGE, Status, Worker


@pytest.fixture(params=[CsvUserProvider])
def user_provider(request) -> UserProvider:
    return request.param()


@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


@pytest.fixture
def workers(users) -> list[Worker]:
    """
    Берем только работников из списка
    """
    workers = [
        Worker(name=user.name, age=user.age, item=user.items)
        for user in users
        if user.status == Status.worker
    ]  # - возьми каждого пользователя из списка пользователей со статусом worker и положи в user
    return workers


def test_workers_are_adults_v3(workers):
    """
    Тестируем что все работники старше 18 лет
    """
    for worker in workers:
        assert worker.is_adult(), f"Worker {worker.name} младше {USER_ADULT_AGE} лет"
