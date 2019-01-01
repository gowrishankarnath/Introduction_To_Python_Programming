# Program 12.2: Program to Demonstrate Python Deserializing Using JSON loads()
# Method

import json


def main():
    json_string = '''
        {
                "title": "Product",
                "description": "A product from Patanjali's catalog",
                "category": "Ayurvedic",
                "item": {
                           "name": "Aloevera Sun Screen Cream",
                           "type": "Face Cream"
                        }
         }
                  '''
    json_object_data = json.loads(json_string)
    print(f"Title is {json_object_data['title']}")
    print(f"Description is {json_object_data['description']}")
    print(f"Category is {json_object_data['category']}")
    print(f"Item name is {json_object_data['item']['name']}")
    print(f"Item type is {json_object_data['item']['type']}")


if __name__ == "__main__":
    main()
