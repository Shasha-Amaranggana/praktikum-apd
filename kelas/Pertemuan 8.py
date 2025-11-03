# kk = int(input("MAsukkin angka: "))
# aa = bin(kk)
# print(aa)

# num = int("42") # 42
# name = str(123) # "123"
# data1 = list("abc") # ['a', 'b', 'c']
# data2 = dict(a=1, b=2) # {'a': 1, 'b': 2}
# print(type(num))

# abs(-9) # 9
# max([1, 3, 7]) # 7
# min([1, 3, 7]) # 1
# round(3.14159,2) # 3.14
# sum([1, 2, 3]) # 6

# max = max([1, 3, 7])
# print(max)

# angka = 2
# angka2 = 3.14

# jumlah = sum([angka, angka2])
# print(jumlah)

# for i, v in enumerate(['a','b']):
#     # print(i) # 0 , 1
#     # print(v) # a , b
#     print(i, v) # 0 a , 1 b

# len([10, 20, 30]) # 3

# list(map(str, [1,2,3])) # ['1', '2', '3']

# sorted([3, 1, 2]) # [1, 2, 3]

# list(zip([1,2],['a','b'])) # [(1,'a'), (2,'b')]

import inquirer 

pertanyaan = [
inquirer.List(
    'size',
    message="What size do you need?",
    choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
    ),
]
# mendapatkan jawaban
answer = inquirer.prompt(pertanyaan)
print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
print(answer['size']) # Ambil value dari key 'size' (Large)