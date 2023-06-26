#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    lista = [1]
    lista1 = []
    lista1.append(lista[:])
    while len(lista) != n:
        if len(lista) == 1:
            lista.append(1)
        elif len(lista) % 2 == 0:
            center = len(lista) // 2
            lista.insert(center, 2 * lista[center])

            left = center - 1
            right = center + 1

            while lista[right] != 1:
                lista[left] += lista[left - 1]
                lista[right] += lista[right + 1]
                left -= 1
                right += 1
        else:
            center = len(lista) // 2
            lista[center] += lista[center - 1]
            lista.insert(center + 1, lista[center])

            left = center - 1
            right = center + 2

            while lista[right] != 1:
                lista[left] += lista[left - 1]
                lista[right] += lista[right + 1]
                left -= 1
                right += 1
        lista1.append(lista[:])
    return lista1
