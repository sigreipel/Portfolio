# Course Project
# Svetlana Greipel

from IPython.lib.pretty import pprint # ignore this - it's just so I can print things nicely in the notebook
from tkinter import Tk, Label, Button
from PIL import ImageTk
from PIL import Image
from io import BytesIO
import requests
# https://ghibliapi.herokuapp.com/?ref=apilist.fun
response = requests.get("https://ghibliapi.herokuapp.com/films")
print(response)

list = response.json()  # retrieve the JSON data (it should be a list of dictionaries)


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if ord(alist[location]["title"][0]) > ord(alist[positionOfMax]["title"][0]):
                positionOfMax = location

        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return alist


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


class ImageGallery:

    def __init__(self):
        self.__main_window = Tk()

        response = requests.get("https://ghibliapi.herokuapp.com/films")
        self.__data = response.json()
        self.__data = selectionSort(self.__data)
        self.__curr_image_num = 0
        self.__photo_data = self.__data[self.__curr_image_num]
        slideShow.enqueue(self.__data[self.__curr_image_num]['title'])
        slideShow.enqueue(self.__data[self.__curr_image_num]['original_title'])
        slideShow.enqueue(self.__data[self.__curr_image_num]['release_date'])
        slideShow.enqueue(self.__data[self.__curr_image_num]['description'])
        image_response = requests.get(self.__data[self.__curr_image_num]['image'])

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
        self.__curr_image_num += 1
        list = response.json()
        selectionSort(list)
        for i in range(1, len(list)):
            slideShow.enqueue(list[i]['title'])
            slideShow.enqueue(list[i]['original_title'])
            slideShow.enqueue(list[i]['release_date'])
            slideShow.enqueue(list[i]['description'])

        image_response = requests.get(list[self.__curr_image_num]['image'])
        print('\nTitle:', slideShow.dequeue())
        print('Original Title:', slideShow.dequeue())
        print('Release Date:', slideShow.dequeue())
        print('Description:', slideShow.dequeue())
        print(list[self.__curr_image_num]["image"])

        im = Image.open(BytesIO(image_response.content))
        im = im.resize((im.size[0] // 2, im.size[1] // 2))
        im = ImageTk.PhotoImage(im)
        self.__image_label.config(image=im)
        self.__image_label.image = im


# selectionSort(list)
# pprint(list)
ImageGallery()
