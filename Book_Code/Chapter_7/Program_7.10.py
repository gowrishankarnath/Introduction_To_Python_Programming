# Program 7.10: Program to Demonstrate Nested Dictionaries

student_details = {"name": "jasmine", "registration_number": "1AIT18CS05", "sub_marks": {"python": 95, "java": 90, ".net": 85}}


def nested_dictionary():
    print(f"Student Name {student_details['name']}")
    print(f"Registration Number {student_details['registration_number']}")
    average = sum(student_details["sub_marks"].values()) / len(student_details["sub_marks"])
    print(f"Average of all the subjects is {average}")


def main():
    nested_dictionary()


if __name__ == "__main__":
    main()


