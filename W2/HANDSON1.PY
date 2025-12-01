#STUDENT GRADE MANAGEMENT
student=[]
def add_student(name,grade):
    student.append({"name ":name,"grade":grade})

def calculate_avg():
    total=sum(std['grade'] for std in student)
    return total/len(student) if student else 0
add_student("Neha",100)
add_student("Debapriya",99)
add_student("Suvendu",98)
add_student("Tripan",10)
print(student)
print(f"Avg grade: {calculate_avg():.2f}")



