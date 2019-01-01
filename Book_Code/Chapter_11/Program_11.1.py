# Program 11.1: Program to Illustrate Class and Object Creation


class Mobile:

    def __init__(self):
        print("This message is from Constructor Method")

    def receive_message(self):
        print("Receive message using Mobile")

    def send_message(self):
        print("Send message using Mobile")


def main():
    nokia = Mobile()
    nokia.receive_message()
    nokia.send_message()


if __name__ == "__main__":
    main()



