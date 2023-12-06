from dataclasses import dataclass
from enum import Enum


USER_ADULT_AGE = 18


class Status(Enum):
    student = "student"
    worker = "worker"


@dataclass
class User:
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE # - вернет тру или фолс если работник младше 18

class Worker(User):

    status = Status.worker

    def __init__(self, name, age, item):
        self.name = name
        self.age = age
        self.items = item


if __name__ == '__main__': # - способ запустить код в ООП
    # Oleg;16;student;book,pen,paper
    d = {"name": "Oleg",
         "age": 16,
         "status": "student",
         "items": ["book", "pen", "paper"]}

    oleg = User(name='Oleg', age=16,status=Status.student, item=['pen', 'book', 'paper'])
    oleg2 = User(name='Oleg', age=16, status=Status.student, item=['pen', 'book', 'paper'])
    olga = User(name='Olga', age=22, status=Status.worker, item=['footbol', 'book', 'paper'])
    olga_worker = Worker(name='Olga', age=22, item=['footbol', 'book', 'paper'])


    assert oleg == oleg2
    assert oleg.age == 16



