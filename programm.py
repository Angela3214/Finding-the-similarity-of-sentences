# https://www.coursera.org/learn/mathematics-and-python/programming/QySgp/linieinaia-alghiebra-skhodstvo-tiekstov-i-approksimatsiia-funktsii
import scipy.spatial.distance
import numpy as np
import re
import scipy
f = open('dataset.txt', 'r', encoding='utf8')
s = str()
cnt = 0 # Кол-во предложений
for line in f:
    s += line
    cnt += 1
s = s.lower()
s = re.split('[^a-z]', s)
s = list(filter(None, s)) # Массив со словами из файла
s = list(set(s))
k = 0
matr = np.ones((cnt, len(s)))
f = open('dataset.txt', 'r', encoding='utf8')
for i in f: # Заполнили матрицу, где размера n * d, где n — число предложений. 
# Элемент с индексом (i, j) в этой матрице это количество вхождений j-го слова в 
# i-е предложение (будет матрица 22*254)
    l = i.lower()
    l = re.split('[^a-z]', l)
    l = list(filter(None, l))
    for j in range(len(s)):
        matr[k, j] = l.count(s[j])
    k += 1
dists = []
for row in matr: # Находим косинусное расстояние от 1-ой строки до остальных 
    dists.append(scipy.spatial.distance.cosine(matr[0, :], row))
dists = dists[1:]
min_1 = min(dists) # Находим самое ближайшее предложение
min_1_ind = dists.index(min_1)
dists = dists[:min_1_ind] + dists[min_1_ind + 1:]
min_2 = min(dists) # А теперь второе по величине
file = open('submission-1.txt', 'w')
file.write(str(min_1) + ' ' + str(min_2))
file.close()
