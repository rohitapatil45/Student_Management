import csv, json

def export_to_csv(data, filename="report.csv"):
    with open(filename, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def export_to_json(data, filename="report.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
