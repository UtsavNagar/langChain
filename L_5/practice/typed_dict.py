from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    
np: Person = {'name': 'Utsav', 'age': 22}

print(np) 