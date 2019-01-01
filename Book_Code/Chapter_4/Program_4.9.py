# Program 4.9: Program to Demonstrate the Use of Default Parameters


def work_area(prompt, domain="Data Analytics"):
    print(f"{prompt} {domain}")


def main():
    work_area("Sam works in")
    work_area("Alice has interest in", "Internet of Things")


if __name__ == "__main__":
    main()
