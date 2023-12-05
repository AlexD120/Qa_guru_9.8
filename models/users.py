

class User:
    name: str
    age: int
    status: str
    items: list[str]
    def __init__(self, name, age, status, item):
        self.name = name
        self.age = age
        self.status = status
        self.items = item


if __name__ == '__main__':
    d = {'name': 'Oleg',
         'age': 16,
         'status': 'student',
         'items': ['pen', 'book', 'paper']}

    oleg = User(name='Oleg', age=16,status='student', item=['pen', 'book', 'paper'])
    olga = User(name='Olga', age=22, status='worker', item=['footbol', 'book', 'paper'])

assert oleg.age==16