#  Даны два файла, в каждом из которых находится запись многочлена. 
#  Найдите сумму данных многочленов

def openFile(nameFile):
    data = open(nameFile, encoding='utf-8')
    full_string = data.readlines()
    data.close()
    list = full_string[0].split(' + ')
    return list

Mnogochlen1_nepravilniy = openFile('Mchlen1.txt')
Mnogochlen2_nepravilniy = openFile('Mchlen2.txt')

Mnogochlen1_nepravilniy.extend(['0',] * (len(Mnogochlen2_nepravilniy) - len(Mnogochlen1_nepravilniy)))
Mnogochlen2_nepravilniy.extend(['0',] * (len(Mnogochlen1_nepravilniy) - len(Mnogochlen2_nepravilniy)))

if len(Mnogochlen1_nepravilniy) < 3:
    Mnogochlen1_nepravilniy.append('0')
if len(Mnogochlen2_nepravilniy) < 3:
    Mnogochlen2_nepravilniy.append('0')

Mnogochlen1 = ['0','0','0']
Mnogochlen2 = ['0','0','0']

_a_ = Mnogochlen1_nepravilniy[0]

if "x^2" in _a_:
    Mnogochlen1[0] = _a_
elif "x" in _a_:
    Mnogochlen1[1] = _a_

_b_ = Mnogochlen1_nepravilniy[1]

if "x" in _b_:
    Mnogochlen1[1] = _b_
else:
    Mnogochlen1[2] = _b_

if int(Mnogochlen1_nepravilniy[2]) !=0:
    Mnogochlen1[2] = Mnogochlen1_nepravilniy[2]

_c_ = Mnogochlen2_nepravilniy[0]

if "x^2" in _c_:
    Mnogochlen2[0] = _c_
elif "x" in _c_:
    Mnogochlen2[1] = _c_

_d_ = Mnogochlen2_nepravilniy[1]
if "x" in _d_:
    Mnogochlen2[1] = _d_
else:
    Mnogochlen2[2] = _d_
if int(Mnogochlen2_nepravilniy[2]) !=0:
    Mnogochlen2[2] = Mnogochlen2_nepravilniy[2]

_a1_ = Mnogochlen1[0]
_b1_ = Mnogochlen1[1]
_a2_ = Mnogochlen2[0]
_b2_ = Mnogochlen2[1]

if _a1_[0] == 'x':
    Mnogochlen1[0] = str(1) + Mnogochlen1[0]
if _b1_[0] == 'x':
    Mnogochlen1[1] = str(1) + Mnogochlen1[1]
if _a2_[0] == 'x':
    Mnogochlen2[0] = str(1) + Mnogochlen2[0]
if _b2_[0] == 'x':
    Mnogochlen2[1] = str(1) + Mnogochlen2[1]


Mnogochlen1[0] = Mnogochlen1[0].replace('x^2', '')
Mnogochlen2[0] = Mnogochlen2[0].replace('x^2', '')

Mnogochlen1[1] = Mnogochlen1[1].replace('x', '')
Mnogochlen2[1] = Mnogochlen2[1].replace('x', '')

print(Mnogochlen1)
print(Mnogochlen2)

koeffitsient1 = int(Mnogochlen1[0]) + int(Mnogochlen2[0])
koeffitsient2 = int(Mnogochlen1[1]) + int(Mnogochlen2[1])
koeffitsient3 = int(Mnogochlen1[2]) + int(Mnogochlen2[2])


data = open('Mchlen1.txt', encoding='utf-8')
example1 = data.readlines()
data.close()

data = open('Mchlen2.txt', encoding='utf-8')
example2 = data.readlines()
data.close()

print(f'\nМногочлен 1:\n {example1}\nМногочлен 2:\n {example2}')
print(f'Сумма многочленов:\n{koeffitsient1}x^2 + {koeffitsient2}x + {koeffitsient3}')