# Program 12.3: Program to Demonstrate Python Serializing Using JSON dump()
# and dumps() Methods

import json


def main():
    string_data =[{
        "Name": "Debian",
        "Owner": "SPI"
        },
        {
            "Name": "Ubuntu",
            "Owner": "Canonical"
        },
        {
            "Name": "Fedora",
            "Owner": "Red Hat"
        }]

    json_data = json.dumps(string_data)
    print("Data in JSON format")
    print(json_data)

    with open('linux_data.json', 'w') as f:
        json.dump(json_data, f)


if __name__ == "__main__":
    main()