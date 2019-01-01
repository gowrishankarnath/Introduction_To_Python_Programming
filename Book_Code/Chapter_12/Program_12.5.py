# Program 12.5: Program to Get JSON Response Content Using Requests Module

import requests


def main():
    r = requests.get('http://date.jsontest.com/')
    date_dict = r.json()
    print(f"Current Time is {date_dict['time']}")
    print(f"MilliSeconds Since Epoch is {date_dict['milliseconds_since_epoch']}")
    print(f"Today's Date is {date_dict['date']}")


if __name__ == "__main__":
    main()
