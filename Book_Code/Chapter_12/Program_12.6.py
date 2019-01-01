# Program 12.6: Construct an XML Formatted Data and Write Python Program to Parse
# that XML Data

import xml.etree.ElementTree as ET


def main():
    university_data = '''
    <top_universities>
        <year_2018>
            <university_name location="USA">MIT</university_name>
            <ranking>First</ranking>
        </year_2018>
        
        <year_2018>
            <university_name location="UK">Oxford</university_name>
            <ranking>Sixth</ranking>
        </year_2018>
        
        <year_2018>
            <university_name location="Singapore">NTU</university_name>
            <ranking>Eleventh</ranking>
        </year_2018>
    </top_universities> 
                     '''
    root = ET.fromstring(university_data)
    for ranking_year in root.findall('year_2018'):
        university_name = ranking_year.find('university_name').text
        ranking = ranking_year.find('ranking').text
        location = ranking_year.find('university_name').get('location')
        print(f"{university_name} University has secured {ranking} Worldwide ranking and is located in {location}")


if __name__ == "__main__":
    main()
