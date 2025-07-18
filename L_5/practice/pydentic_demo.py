from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Utsav'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10.1, default=0.1, description='this value depresents the CGPA of the student')
    
    
ns: Student = {'age': 22,'email': 'utsav@gmail.com','cgpa':1.1}

student = Student(**ns)

print(student)