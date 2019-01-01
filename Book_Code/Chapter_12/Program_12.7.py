# Program 12.7: Write Python Program to Generate XML Formatted Data and Save it as
# an XML Document

import xml.etree.ElementTree as ET


def main():
    root = ET.Element("catalog")
    child = ET.SubElement(root, "book", {"id":"bk101"})
    subchild_1 = ET.SubElement(child, "author")
    subchild_2 = ET.SubElement(child, "title")
    subchild_1.text = "Michael Connelly"
    subchild_2.text = "City of Bones"
    child = ET.SubElement(root, "book", {"id":"bk102"})
    subchild_1 = ET.SubElement(child, "author")
    subchild_2 = ET.SubElement(child, "title")
    subchild_1.text = "Jeffrey Friedl"
    subchild_2.text = "Mastering Regular Expressions"
    tree = ET.ElementTree(root)
    tree.write("books.xml")


if __name__ == "__main__":
    main()
