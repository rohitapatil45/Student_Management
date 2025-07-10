from data import students, get_student_input
from logic import process_students, assign_ranks
from display import display_report
from utils import export_to_csv, export_to_json
from extensions import all_subject_averages, subject_topper

def main():
    students.append(get_student_input())  # Optional: Uncomment to add from CLI
    processed = process_students(students)
    ranked = assign_ranks(processed)
    display_report(ranked)
    export_to_csv(ranked)
    export_to_json(ranked)

    print("Class Averages:", all_subject_averages(students))
    print("Topper in Science:", subject_topper(students, "science")["name"])

if __name__ == "__main__":
    main()
