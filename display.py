def display_report(students):
    for s in students:
        print(f"{s['name']} (ID: {s['id']})")
        print(f"  Total: {s['total']} | Average: {s['average']:.2f} | Grade: {s['grade']}")
        if 'rank' in s:
            print(f"  Rank: {s['rank']}")
        print("-" * 40)
