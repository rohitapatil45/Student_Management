students = [
    {"id": 1, "name": "Meera", "marks": {"math": 78, "science": 90, "english": 85}},
    {"id": 2, "name": "Ravi", "marks": {"math": 32, "science": 50, "english": 60}},
    {"id": 3, "name": "Simran", "marks": {"math": 88, "science": 92, "english": 81}}
]

def get_student_input():
    name = input("Enter student name: ")
    sid = int(input("Enter student ID: "))

    def get_mark(subject):
        while True:
            try:
                m = int(input(f"Enter marks for {subject}: "))
                if 0 <= m <= 100:
                    return m
                print("Marks must be between 0–100.")
            except ValueError:
                print("Invalid input.")

    marks = {sub: get_mark(sub) for sub in ["math", "science", "english"]}
    return {"id": sid, "name": name, "marks": marks}
