
import xml.etree.ElementTree as ET





def findCoordByFeach(feach, town):


    #main_url = "https://www.uralsib.ru/raw/offices-xml/yandex"
    filename = "ural.xml"



    #context = ssl._create_unverified_context()
    #request.urlopen(linkid, context=context)

    root= ET.parse(filename).getroot()

    listOfCoords = []
    #listOfCoords = root.findall('./company/feature-enum-multiple[@value="' + feach + '"]/../coordinates')
    listOfComp = root.findall('./company/feature-enum-multiple[@value="' + feach + '"]/..')
    for elem in listOfComp:
        x = elem.findall('./locality-name')
        if (len(x) > 0):
            if (x[0].text == town):
                listOfCoords.append(elem.findall('./coordinates')[0])

    
    answer = []

    for elem in listOfCoords:

        answer.append((elem[0].text, elem[1].text))
        

    return answer

def findByTown(coords, town):

    listOfCoords = root.findall('./company/coordinates')

    return coords

print(findCoordByFeach("pay_for_internet_access", "город Уфа"))


