import tkinter as tk
import matplotlib.pyplot as plt
import random as rd
import time as tm

lista = []
bubble_times = []
selection_times = []
N = [30, 50, 70, 90, 110, 130]

def Bubble_Sort(arr):
    n = len(arr)
    # Ciclo externo corre n veces de forma fija
    initial_time = tm.time()
    for i in range(n):
        # Ciclo interno compara elementos adyacentes
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                # Intercambio de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    final_time = tm.time()
    total_time = final_time - initial_time

    return total_time

def Selection_Sort(arr):
    n = len(arr)

    initial_time = tm.time()
    for i in range(n - 1):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        # Buscamos en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiamos el menor encontrado con el primer elemento actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    final_time = tm.time()
    total_time = final_time - initial_time

    return total_time

def Generate(n, min, max):
    return [rd.randint(min, max) for i in range(n)]

def Showing_Plot():
    for i in N:
        lista.append(Generate(i, 1, 100))

    for i in range(len(N)):
        bubble_times.append(Bubble_Sort(lista[i]))
        selection_times.append(Selection_Sort(lista[i]))

    plt.plot(N, bubble_times, marker="o", label="Bubble Sort")
    plt.plot(N, selection_times, marker="o", label="Selection Sort")
    plt.title("Bubble vs Selection")
    plt.xlabel("Tamaño de entrada")
    plt.ylabel("Tiempo de ejecucion")
    plt.legend()
    plt.grid()
    plt.show()

# -----------------------------------------------
# Configuracion de la ventana root en tkinter
root = tk.Tk()

width_screen = root.winfo_screenwidth()
height_screen = root.winfo_screenheight()

width_root = 375
height_root = 300
x_coordinate = (width_screen - width_root)//2
y_coordinate = (height_screen - height_root)//2

root.title("Algo ritmo")
root.geometry(f"{width_root}x{height_root}+{x_coordinate}+{y_coordinate}")

lb1 = tk.Label(root, text="Bubble vs. Selection", background="purple4", foreground="gray")
lb1.pack(pady=8)

bu1 = tk.Button(root, text="Inicio: 30")
bu1.pack(pady=10)

bu2 = tk.Button(root, text="Incremento: +20")
bu2.pack(pady=12)

bu3 = tk.Button(root, text="Fin: 130")
bu3.pack(pady=14)

bu4 = tk.Button(root, text="Generar y Calcular", command=Showing_Plot)
bu4.pack(pady=16)

root.mainloop()
