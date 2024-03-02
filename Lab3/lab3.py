counter = 0
#Первый вопрос
answer = input("Столица России?\n")
if answer == "Москва" or answer == "москва":
    counter = counter + 1
    print("Вы ответили верно")
else:
    print("Вы ответили не верно")
#Второй вопрос  
answer = input("Какой язык мы изучаем?\n")
if answer == "Python" or answer == "Пайтон":
    couter = counter + 1
    print("Вы ответили верно")
else:
    ("Вы ответили не верно")
#Третий вопрос
answer = input("В какой группе мы учимся?\n")  
if answer == "P-21" or answer == "П-21":
    counter = counter + 1
    print("Вы ответили верно")
else:
    print("Вы ответили не верно")
#Четвёртый вопрос
answer = input("В каком году ты поступил в колледж?\n")
if answer == "2021" or answer == "2022":
    counter = counter + 1
    print("Вы ответили верно")
else:
    print("Вы ответили не верно")
print(f"Вы набрали баллов {counter}")
