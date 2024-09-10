# README

## Description

This Python script reads data from a CSV file containing university exams, grades obtained, credits for each exam, and the category to which the exam belongs (e.g., "Informatics", "Mathematics", "Economics", etc.). The script calculates the weighted average of grades for each category and the overall weighted average for all exams. Finally, it prints the obtained averages.

## Features

- **`read_grades_csv(file_path)`**: Reads a CSV file containing exams and returns a list of dictionaries with data for subject, grade, credits, and category.
- **`calculate_averages_by_category(exams)`**: Calculates the average grade for each category and the overall weighted average based on credits.
- **`print_results(averages_by_subject, overall_average)`**: Prints the grade averages for each category and the overall average.

## Requirements

- Python 3.x
- `csv` module
- `collections` module (included in Python)

## Usage

1. Prepare a CSV file containing your exams with the following columns: `Exam`, `Grade`, `Credits`, and `Category`. Use `;` as the delimiter.
2. Modify the `file_csv` variable in the script to point to your CSV file.
3. Run the script to obtain the grade averages by category and the overall average.

### Example Usage:

#### Input (CSV file)

The CSV file should be formatted as follows:

```
Exam;Grade;Credits;Category
"Calculus";28;9;"Mathematics"
"Architecture";27;10;"Informatics"
"Internet Law";30;8;"Law"
"Business Administration";24;7;"Economics"
"Organization";28;7;"Economics"
"Programming";26;20;"Informatics"
"Algorithms";30;14;"Informatics"
"Finance";27;8;"Economics"
"Numerical Methods";29;10;"Mathematics"
"Microeconomics";29;7;"Economics"
"Operating Systems";30;18;"Informatics"
"Statistics";30;7;"Mathematics"
"Strategy";30;8;"Economics"
"Databases";29;10;"Informatics"
"Cybersecurity";30;8;"Informatics"
"Engineering";26;8;"Informatics"
"Digital Humanities";30;8;"Informatics"
"SOM";30;9;"Economics"
"TechWeb";29;8;"Informatics"
"Business Theory";30;8;"Economics"
```

#### Output

Example output from the script:

```
Averages by category:
Mathematics: 28.92
Informatics: 28.46
Law: 30.00
Economics: 28.39

Overall average: 28.57
```

## CSV File Modification

You can update the CSV file by adding new exams or modifying existing values. Make sure to maintain the correct format and use `;` as the delimiter.