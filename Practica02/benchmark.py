import sorts
import random as rd
import time as tm
import matplotlib.pyplot as plt

sorts_list = []
bubble_times = []
selection_times = []
insertion_times = []
gnome_times = []
exchange_times = []
stooge_times = []
N = []

def Generate(n, min, max):
    temp = []
    for i in range(n):
        temp.append(rd.randint(min,max))
    return (temp)

initial = 20
final = 101
increase = 20 

for i in range(initial, final, increase):
    sorts_list.append(Generate(i, 1, 100))
    N.append(i)

for i in sorts_list:
    t_initBubble = tm.time()
    sorts.Bubble_Sort(i)
    t_finBubble = tm.time()
    bubble_times.append(t_finBubble - t_initBubble)

    t_initSelection = tm.time()
    sorts.Selection_Sort(i)
    t_finSelection = tm.time()
    selection_times.append(t_finSelection - t_initSelection)

    t_initInsertion = tm.time()
    sorts.insertion_sort(i)
    t_finInsertion = tm.time()
    insertion_times.append(t_finInsertion - t_initInsertion)

    t_initGnome = tm.time()
    sorts.gnome_sort(i)
    t_finGnome = tm.time()
    gnome_times.append(t_finGnome - t_initGnome)

    t_initExchange = tm.time()
    sorts.exchange_sort(i)
    t_finExchange = tm.time()
    exchange_times.append(t_finExchange - t_initExchange)

    t_initStooge = tm.time()
    sorts.stooge_sort(i)
    t_finStooge = tm.time()
    stooge_times.append(t_finStooge - t_initStooge)


def Showing_Plot():
    plt.plot(N, bubble_times, marker="o", label="Bubble Sort")
    plt.plot(N, selection_times, marker="o", label="Selection Sort")
    plt.plot(N, insertion_times, marker="o", label="Insertion Sort")
    plt.plot(N, gnome_times, marker="o", label="Gnome Sort")
    plt.plot(N, exchange_times, marker="o", label="Exchange Sort")
    plt.xlabel("Dataset Size")
    plt.ylabel("Run-Time")
    plt.legend()
    plt.grid()
    plt.show()

def Showing_StoogePlot():
    plt.plot(N, stooge_times, marker="o", label="Stooge Sort")
    plt.xlabel("Dataset Size")
    plt.ylabel("Run-Time")
    plt.legend()
    plt.grid()
    plt.show()
