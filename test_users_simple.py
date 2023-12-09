import csv


def test_workers_are_adults():
    with open("users.csv") as f:
        users = csv.DictReader(f, delimiter=";")
        workers = [
            user for user in users if user["status"] == "worker"
        ]  # - возьми каждого пользователя из списка пользователей со статусом worker и положи в user

        for worker in workers:
            assert int(worker["age"]) >= 18, f"Worker {worker['name']} младше 28 лет"
