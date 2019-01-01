# Program 11.2: Program to Illustrate Multiple Parameters in __init__() Method


class Mobile:

    def __init__(self, mobile_name):
        self.mobile_name = mobile_name

    def receive_message(self):
        print(f"Receive message using {self.mobile_name} Mobile")

    def send_message(self):
        print(f"Send message using {self.mobile_name} Mobile")


def main():
    nokia = Mobile("Nokia")
    nokia.receive_message()
    nokia.send_message()


if __name__ == "__main__":
    main()
