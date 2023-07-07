
"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        #print([parts], end=' ')  # See what the parts look like (notice the integer is a string)
        #parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(f"{parts}, {parts}")  # See if that worked
        print("----------")
    input_file.close()


def comment(subject_code, instructor_name, num_students):
    subject_code =["CP1401","CP1404","CP4321","CP1234"]
    instructor_name = ["Ada Lovelace","Alan Turing","Bill Gates","Steve Jobs"]
    num_students = [192,98,676,123]
    for subject_code, instructor_name, num_students in zip(subject_code, instructor_name, num_students):
        
        print(f"{subject_code} is taught by {instructor_name} and has {num_students} students")


main()
comment()