import requests

def get_student_by_id(student_id: int):
    url = f"http://127.0.0.1:8000/students/id/{student_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.json())
        return None

student = get_student_by_id(student_id=5)
if student:
    print(student)
else:
    print("Student not found")


