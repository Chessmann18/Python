age = int(input("Введите возраст"))
if age > 0 and age <= 10:
    print("Вы ребёнок")
elif age > 10 and age <= 16:
    print("Вы подросток")
elif age > 16 and age <= 22:
    print("Вы взрослый")
elif age > 22 and age <= 30:
    print("Вы всё еще взрослый")
elif age > 30 and age <= 50:
    print("Вы по-прежнему взрослый")
elif age > 50 and age <= 80:
    print("Вы пожилой человек")
elif age > 80 and age <=100:
    print("Вы в глубокой старости")
    print("Возраст введён не верно!!!!")