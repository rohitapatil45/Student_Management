from functools import reduce

def subject_average(students, subject):
    passed = list(filter(lambda s: all(m >= 40 for m in s["marks"].values()), students))
    total = reduce(lambda acc, s: acc + s["marks"][subject], passed, 0)
    return total / len(passed) if passed else 0

def all_subject_averages(students):
    return {s: subject_average(students, s) for s in ["math", "science", "english"]}

def subject_topper(students, subject):
    return max(filter(lambda s: all(m >= 40 for m in s["marks"].values()), students),
               key=lambda s: s["marks"][subject])
