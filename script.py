import csv
from collections import defaultdict


def read_grades_csv(file_path):
    exams = []
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            subject = row["Exam"]
            grade = int(row["Grade"])
            credits = int(row["Credits"])
            category = row.get("Category", "General")
            exams.append(
                {
                    "subject": subject,
                    "grade": grade,
                    "credits": credits,
                    "category": category,
                }
            )
    return exams


def calculate_averages_by_category(exams):
    # Data by category
    grades_by_category = defaultdict(lambda: {"sum_grades": 0, "sum_credits": 0})

    # Global data
    weighted_sum_grades = 0
    total_sum_credits = 0

    # Processing exams
    for exam in exams:
        category = exam["category"]
        grade = exam["grade"]
        credits = exam["credits"]

        # Calculation for single category
        grades_by_category[category]["sum_grades"] += grade * credits
        grades_by_category[category]["sum_credits"] += credits

        # General calculation
        weighted_sum_grades += grade * credits
        total_sum_credits += credits

    # General average calculation
    overall_average = (
        weighted_sum_grades / total_sum_credits if total_sum_credits > 0 else 0
    )

    # Calculation of averages per category
    averages_by_category = {}
    for category, data in grades_by_category.items():
        sum_grades = data["sum_grades"]
        sum_credits = data["sum_credits"]
        category_average = sum_grades / sum_credits if sum_credits > 0 else 0
        averages_by_category[category] = category_average

    return averages_by_category, overall_average


def print_results(averages_by_category, overall_average):
    print("Averages by category:")
    for category, average in averages_by_category.items():
        print(f"{category}: {average:.2f}")

    print(f"\nOverall average: {overall_average:.2f}")


# Main script
file_csv = "uni.csv"  # Enter the name of the CSV file
exams = read_grades_csv(file_csv)
averages_by_category, overall_average = calculate_averages_by_category(exams)
print_results(averages_by_category, overall_average)
