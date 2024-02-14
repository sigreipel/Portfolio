from IPython.lib.pretty import pprint
from tkinter import Tk, Label, Button
from PIL import ImageTk, Image
from PIL import Image
from io import BytesIO
import requests

# response = requests.get(base_url, params=query_params)
response = requests.get("https://ghibliapi.herokuapp.com/films")
# # pprint(response.json()[0])
#
# print('Total number of photos:', len(response.json()[0]['image']))
# # print(response.json()[0]["image"])
#
# image_result = requests.get(response.json()[0]["image"])
# print(image_result)
#
# im = Image.open(BytesIO(image_result.content))
# im.show()
# im.close()

# for i in range(1, len(response.json()[0]["image"])-1):
#     image_result = requests.get(response.json()[i]["image"])
#     im = Image.open(BytesIO(image_result.content))
#     im.show()

class Queue:
    def __init__(self):  # O(1)
        self.__object_list = []

    def is_empty(self):  # O(1)
        return self.__object_list == []

    def dequeue(self):  # O(1)
        return self.__object_list.pop()

    def enqueue(self, param):  # O(n)
        return self.__object_list.insert(0, param)

    def size(self):  # O(1)
        return len(self.__object_list)


slideShow = Queue()

def insertionSort(list):
    for i in range(1, len(list)):
        currVal = ord(list[i]["title"][0])
        position = i

        while position > 0 and ord(list[position - 1]["title"][0]) < currVal:
            list[position] = list[position - 1]
            position = position - 1

        currVal = list[position]["title"][0]


class ImageGallery:

    def __init__(self):
        self.__main_window = Tk()

        response = requests.get("https://ghibliapi.herokuapp.com/films")
        self.__curr_image_num = 0
        # self.__photo_data = response.json()[self.__curr_image_num]
        slideShow.enqueue(response.json()[self.__curr_image_num]['title'])
        slideShow.enqueue(response.json()[self.__curr_image_num]['original_title'])
        slideShow.enqueue(response.json()[self.__curr_image_num]['release_date'])
        slideShow.enqueue(response.json()[self.__curr_image_num]['description'])
        image_response = requests.get(response.json()[self.__curr_image_num]['image'])
        self.__curr_image_num += 1

        print('\nTitle:', slideShow.dequeue())
        print('Original Title:', slideShow.dequeue())
        print('Release Date:', slideShow.dequeue())
        print('Description:', slideShow.dequeue())

        im = Image.open(BytesIO(image_response.content))

        im = im.resize((im.size[0] // 2, im.size[1] // 2))
        im = ImageTk.PhotoImage(im)

        self.__image_label = Label(self.__main_window, image=im)
        self.__image_label.image = im

        self.__next_button = Button(self.__main_window, text="Next", command=self.load_next)

        self.__image_label.pack()
        self.__next_button.pack()

        self.__main_window.mainloop()

    def load_next(self):
        slideShow.enqueue(response.json()[self.__curr_image_num]['title'])
        slideShow.enqueue(response.json()[self.__curr_image_num]['original_title'])
        slideShow.enqueue(response.json()[self.__curr_image_num]['release_date'])
        slideShow.enqueue(response.json()[self.__curr_image_num]['description'])
        image_response = requests.get(response.json()[self.__curr_image_num]['image'])
        print('\nTitle:', slideShow.dequeue())
        print('Original Title:', slideShow.dequeue())
        print('Release Date:', slideShow.dequeue())
        print('Description:', slideShow.dequeue())
        # print(response.json()[self.__curr_image_num]["image"])
        self.__curr_image_num += 1

        im = Image.open(BytesIO(image_response.content))
        im = im.resize((im.size[0] // 2, im.size[1] // 2))
        im = ImageTk.PhotoImage(im)
        self.__image_label.config(image=im)
        self.__image_label.image = im
