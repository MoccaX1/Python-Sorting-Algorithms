from tkinter import *
import time


def bubbleSort(lst):
    for number in range(len(lst) - 1, 0, -1):
        for i in range(number):
            if lst[i] > lst[i + 1]:
                animation(bato0(i), i, reto1(i + 1))
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                print(lst)


def selectionSort(lst):
    for i in range(len(lst)-1, 0, -1):
       pos_max=0
       for location in range(1, i+1):
           if lst[location]>lst[pos_max]:
               animation(i, pos_max, location)
               pos_max = location
               print(lst)
       animation(i, pos_max)
       lst[i], lst[pos_max] = lst[pos_max], lst[i]
       print(lst)


def InsertionSort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        pos = i - 1
        while pos >= 0 and lst[pos] > x:
            animation(pos + 1, i, pos)
            lst[pos + 1] = lst[pos]
            pos -= 1
            print(lst)
        animation(pos + 1, i)
        lst[pos + 1] = x
        print(lst)


def InterChangeSort(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[i]:
                animation(i, reto1(i + 1), j)
                lst[i], lst[j] = lst[j], lst[i]
                print(lst)


def HeapSort(lst):
    n = len(lst)
    s = 0
    for k in range(1, n):
        x = lst[k]
        s = k
        f = (s - 1)//2
        while s > 0 and lst[f] < x:
            animation(f, k, s)
            lst[s] = lst[f]
            print(lst)
            s = f
            f = (s - 1) // 2
        lst[s] = x
    for k in range(n - 1, 0, -1):
        animation(k, s, 0)
        iv = lst[k]
        lst[k] = lst[0]
        print(lst)
        f = 0
        if k is 1:
            s = -1
        else:
            s = 1
        if k > 2 and lst[2] > lst[1]:
            s = 2
        while s >= 0 and iv < lst[s]:
            animation(f, k, s)
            lst[f] = lst[s]
            print(lst)
            f = s
            s = 2 * f + 1
            if s + 1 <= k - 1 and lst[s] < lst[s + 1]:
                s += 1
            if s > k - 1:
                s = -1
        animation(reto1(k - 1), k, s)
        lst[f] = iv


def QuickSort(lst, L, R):
    if L >= R:
        return
    x = lst[int((L + R)/2)]
    i = L
    j = R
    while i < j:
        while lst[i] < x:
            i += 1
        while lst[j] > x:
            j -= 1
        if i <= j:
            animation(i, int((L + R)/2), j)
            lst[i], lst[j] = lst[j], lst[i]
            print(lst)
            i += 1
            j -= 1
    QuickSort(lst, L, j)
    QuickSort(lst, i, R)


def reto1(i):
    if i is len(lst):
        i = 0
    return i


def bato0(i):
    if i < 0:
        i = 0
    return i


def animation(i=0, j=0, z=0):
    size_lst = len(lst)
    x, y = 220 - 2 * size_lst, 550 + 0.5*max(lst)
    r = 10
    cv.delete(ALL)
    k = 0
    for ic in range(size_lst):
        k += 1
        cv.create_rectangle(x, y, x + r, y - (lst[ic] * 5), fill="purple", activefill="white", tag=[ic], width=1.0)
        if lst[ic] == lst[i] and ic == i:
            cv.create_rectangle(x, y, x + r, y - (lst[ic] * 5), fill="green", activefill="white", tag=[ic], width=1.0)
        if lst[ic] == lst[j] and ic == j:
            cv.create_rectangle(x, y, x + r, y - (lst[ic] * 5), fill="red", activefill="white", tag=[ic], width=1.0)
        if lst[ic] == lst[z] and ic == z:
            cv.create_rectangle(x, y, x + r, y - (lst[ic] * 5), fill="yellow", activefill="white", tag=[ic], width=1.0)
        cv.create_text((x + 5, y - (lst[ic] * 5) - 5), text=lst[ic], fill="yellow")
        cv.create_text((x + 5, y + 10), text=k, fill="purple")
        x += r + 5
    cv.create_text((x/2, y + 30), text="Vị trí xếp: %d" % (i + 1), fill="green")
    cv.create_text((x/2 + 100, y + 30), text="Vị trí mốc: %d" % (j + 1), fill="red")
    cv.create_text((x / 2 + 200, y + 30), text="Vị trí so sánh: %d" % (z + 1), fill="yellow")
    cv.update()
    time.sleep(2)


root = Tk()
root.title("Biểu diễn thuật toán sắp xếp")
lst = []

print("Nhập vào các giá trị (mỗi số cách nhau bởi khoảng trắng, kết thúc nhập bằng phím Enter)")
x = input().split()

try:
    for i in x:
        lst.append(int(i))
except ValueError:
    print("Nhập không hợp lệ!")
    exit()

cv = Canvas(width=800 + 5*len(lst), height=600 + round(0.5*max(lst)), bg="black")
cv.pack()
cv.update()


class Nhap:
    def __init__(self, name_class):
        self.name = name_class
        self.io = 'G'

    def Input(self):
        print("Lựa chọn theo danh sách sau:")
        print("Nhập A: Sắp xếp nổi bọt ")
        print("Nhập B: Sắp xếp lựa chọn ")
        print("Nhập C: Sắp xếp chèn ")
        print("Nhập D: Đổi chỗ trực tiếp ")
        print("Nhập E: Sắp xếp vun đống ")
        print("Nhập F: Sắp xếp nhanh")
        self.io = input()

    def check(self):
        if self.io is 'A':
            
            a = Label(root, text="SẮP XẾP NỔI BỌT")
            a.config(anchor=W, justify="center")
            a.pack()
            cv.update()
            return bubbleSort(lst)

        elif self.io is 'B':

            a = Label(root, text="SẮP XẾP LỰA CHỌN")
            a.config(anchor=W, justify="center")
            a.pack()
            cv.update()
            return selectionSort(lst)

        elif self.io is 'C':

            a = Label(root, text="SẮP XẾP CHÈN")
            a.config(anchor=W, justify="center")
            a.pack()
            cv.update()
            return InsertionSort(lst)

        elif self.io is 'D':

            a = Label(root, text="ĐỔI CHỖ TRỰC TIẾP")
            a.config(anchor=W, justify="center")
            a.pack()
            cv.update()
            return InterChangeSort(lst)

        elif self.io is 'E':

            a = Label(root, text="SẮP XẾP VUN ĐỐNG")
            a.config(anchor=W, justify="center")
            a.pack()
            cv.update()
            return HeapSort(lst)

        elif self.io is 'F':

            a = Label(root, text="SẮP XẾP NHANH")
            a.config(anchor=W, justify="center")
            a.pack()
            cv.update()
            return QuickSort(lst, 0, len(lst)-1)

        else:
            print("Nhập không hợp lệ!")
            exit()


u = Nhap("Demo thuật toán")
u.Input()
u.check()

animation()
root.mainloop()
