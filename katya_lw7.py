import numpy as np
from time import perf_counter
import random
import matplotlib.pyplot as plt
from matplotlib import animation


def draw_part(step):
    ax.plot(points[0, step:step + 2], points[1, step:step + 2], marker='x', c='red')


if __name__ == '__main__':
    # сравниваем скорость работы списков и массивов
    lst1, lst2 = [], []
    for i in range(1):
        lst1.append(random.random())
        lst2.append(random.random())
    t = perf_counter()
    for el1, el2 in zip(lst1, lst2):
        tmp = el1 * el2
    print('list time:  ' + str(perf_counter() - t))

    arr1, arr2 = np.array(lst1, float), np.array(lst2, float)
    t = perf_counter()
    tmp = np.multiply(arr1, arr2)
    print('array time: ' + str(perf_counter() - t))

    # рисуем графики
    arr = np.genfromtxt('data2.csv', delimiter=',')
    arr = arr[:,2]
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    plt.xlabel('значение параметра')
    plt.ylabel('частота')
    ax.hist(arr[1:])
    ax.grid()
    plt.show()
    print('среднеквадратичное отклонение: ' + str(np.std(arr[1:])))

    # объемный график x∈(-5;5); y∈(-5;5); z=sin(x^y)
    np.random.seed(40)
    xs = np.linspace(-5, 5, 20)
    ys = xs
    zs = np.sin(xs * ys)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_title('z=sin(x^y)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.plot(xs, ys, zs, marker='x', c='red')
    plt.show()

    # анимированный объёмный график y = sin(x)
    xs = np.linspace(0, 20, 100)
    ys = np.sin(xs)
    points = np.array([xs, ys])

    fig = plt.figure()
    ax = plt.axes()
    ax.set_title('y = sin(x)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim([0, 20])
    ax.set_ylim([-2, 2])
    anim = animation.FuncAnimation(fig, draw_part, interval=100, frames=len(xs))
    plt.show()
