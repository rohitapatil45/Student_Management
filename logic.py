def has_passed(student):
    return all(m >= 40 for m in student["marks"].values())

def calculate_scores(student):
    marks = student["marks"].values()
    total = sum(marks)
    avg = total / len(marks)
    return {
        "id": student["id"],
        "name": student["name"],
        "total": total,
        "average": avg
    }

def assign_grade(report):
    avg = report["average"]
    if avg >= 90:
        grade = "A+"
    elif avg >= 75:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "F"
    return {**report, "grade": grade}

def process_students(data):
    return list(map(
        assign_grade,
        map(calculate_scores,
            filter(has_passed, data)
        )
    ))

def sort_students(data, by="average"):
    return sorted(data, key=lambda x: x[by], reverse=True)

def assign_ranks(data):
    sorted_data = sort_students(data)
    return list(map(lambda t: {**t[1], "rank": t[0] + 1}, enumerate(sorted_data)))
