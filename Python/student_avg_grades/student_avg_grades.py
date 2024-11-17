import csv

def calculate_average(scores):
    """Calculate the average of a list of scores."""
    return sum(scores) / len(scores)

def main():
    # Step 1: Read the data from "student_grades.csv"
    student_averages = {}

    with open('student_grades.csv', mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Step 2: For each student, calculate their average score
        for row in reader:
            name = row['Name']
            maths_score = float(row['Maths'])
            science_score = float(row['Science'])
            english_score = float(row['English'])
            
            # Step 3: Calculate the average score
            average_score = calculate_average([maths_score, science_score, english_score])
            
            # Step 4: Store the student's name and their corresponding average score
            student_averages[name] = average_score

    # Step 5: Write the data into a new CSV file named "student_average_grades.csv"
    with open('student_average_grades.csv', mode='w', newline='') as csvfile:
        fieldnames = ['Name', 'Average']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()  # Write the header
        for name, average in student_averages.items():
            writer.writerow({'Name': name, 'Average': average})

    print("Average grades have been calculated and saved to 'student_average_grades.csv'.")

if __name__ == "__main__":
    main()