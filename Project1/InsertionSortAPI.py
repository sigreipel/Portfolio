import requests
from IPython.lib.pretty import pprint

response = requests.get("https://ghibliapi.herokuapp.com/films")
# pprint(response.json()[0])

print('Total number of photos:', len(response.json()[0]['image']))
# print(response.json()[0]["release_date"])

# image_result = requests.get(response.json()[0]["image"])
# print(image_result)
# for i in range(len(response.json())):
#     print(response.json()[i]["title"])


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if ord(alist[location]["title"][0]) > ord(alist[positionOfMax]["title"][0]):
                positionOfMax = location
            elif ord(alist[location]["title"][0]) == ord(alist[positionOfMax]["title"][0]):
                for i in range(len(alist[location]["title"])):
                    if ord(alist[location]["title"][i]) > ord(alist[positionOfMax]["title"][i]):
                        positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


alist = response.json()
selectionSort(alist)
pprint(alist)
# print(response.json()[0]["title"][0])
# print(ord(response.json()[0]["title"][0]))
