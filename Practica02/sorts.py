def Bubble_Sort(arr):

    lista = arr.copy()
    n = len(lista)
    # Ciclo externo corre n veces de forma fija
    for i in range(n):
        # Ciclo interno compara elementos adyacentes
        for j in range(0, n - 1):
            if lista[j] > lista[j + 1]:
                # Intercambio de elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista

def Selection_Sort(arr):

    lista = arr.copy()
    n = len(lista)
    for i in range(n - 1):
        # Suponemos que el primer elemento no ordenado es el menor
        min_idx = i
        # Buscamos en el resto de la lista
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        # Intercambiamos el menor encontrado con el primer elemento actual
        lista[i], lista[min_idx] = lista[min_idx], lista[i]

    return lista

def insertion_sort(arr):
    """
    Ordenamiento por Inserción.
    Complejidad: O(N^2)
    """
    lista = arr.copy()
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        # Compara la clave con los elementos anteriores y los desplaza
        while j >= 0 and lista[j] > clave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = clave
    return lista

def gnome_sort(arr):
    lista = arr.copy()
    i = 0
    n = len(lista)
    
    while i < n:
        if i == 0 or lista[i] >= lista[i - 1]:
            i += 1  # Avanza si está en orden
        else:
            lista[i], lista[i - 1] = lista[i - 1], lista[i]  # Intercambia
            i -= 1  # Retrocede un paso
            
    return lista

def exchange_sort(arr):
    """
    Ordenamiento por Intercambio Directo (Exchange Sort).
    Complejidad: O(N^2)
    """
    lista = arr.copy()
    n = len(lista)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Si el elemento posterior es menor, intercambia de inmediato
            if lista[j] < lista[i]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

'''
l (Low / Izquierda): Es el índice inicial (límite inferior) de la sublista actual.

h (High / Derecha): Es el índice final (límite superior) de la sublista actual.
Ejemplo de uso stooge_sort_rec(arr, 0, len(arr) - 1)
'''


def stooge_sort_rec(arr, l, h):
    if l >= h:
        return

    # Si el primer elemento es mayor que el último, intercambiar
    if arr[l] > arr[h]:
        arr[l], arr[h] = arr[h], arr[l]

    # Si hay 3 o más elementos en el rango
    if h - l + 1 > 2:
        t = (h - l + 1) // 3
        # Aplicar fuerza bruta a los 3 tercios superpuestos
        stooge_sort_rec(arr, l, h - t)       # Primeros 2/3
        stooge_sort_rec(arr, l + t, h)       # Últimos 2/3
        stooge_sort_rec(arr, l, h - t)       # Primeros 2/3 de nuevo

def stooge_sort(arr):
    lista = arr.copy()
    stooge_sort_rec(lista, 0, len(lista) - 1)
    return lista