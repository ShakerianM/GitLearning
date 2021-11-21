#Learning
class Student():
    def __init__(self,std_id):
        self.std_id = std_id
        print(f'Student with student id of {self.std_id} was added')
        self.courses = []
    def add_course(self, course_name):
        self.courses.append(course_name)
    def __str__(self) -> str:
        return f'Student with id {self.std_id} and courses : {self.courses}'


        
st1 = Student(81077)
st1.add_course("chem")
print(st1)

