# Program 12.1: Program to Demonstrate Python Deserializing Using JSON load()
# Method

import json


def main():
    with open('personal_data.json', 'r') as f:
        json_object_data = json.load(f)

        print(f'Type of data returned by json load is {type(json_object_data)}')
        print(f"First Name is {json_object_data['first_name']}")
        print(f"Middle Name is {json_object_data['middle_name']}")
        print(f"Last Name is {json_object_data['last_name']}")
        print(f"Phone Number is {json_object_data['contact']['phone']}")
        print(f"Email ID is {json_object_data['contact']['email']}")
        print("-----------------**************---------------")

        for each_json_object in json_object_data['address']:
            print(f"Address Type is {each_json_object['address_type']}")
            print(f"Street Name is {each_json_object['street']}")
            print(f"City Name is {each_json_object['city']}")
            print(f"Zip Number is {each_json_object['zip_code']}")
            print(f"State Name is {each_json_object['state']}")
            print("-----------------**************---------------")


if __name__ == "__main__":
    main()

