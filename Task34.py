# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

my_letter = {1 : 'ауоыиэяюёе'}
s = str(input("Введите фразу: "))
my_list = s.split()

B = []

for i in range(len(my_list)):
    total = 0
    for letter in my_list[i]:
        for key, value in my_letter.items():
            if letter in value:
                total +=key
    B.append(total)

count = 1
for j in range(len(B) - 1):
    if B[j] == B[j + 1]:
        count +=1

if count == len(B):
    print("Парам пам-пам")
else:
    print("Пам парам")
