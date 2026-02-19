while True:
    print("\n=== TO-DO СПИСОК ===")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Выход")

    выбор = input("Выберите: ")

    if выбор == "1":
        z = input("Введите задачу: ")
        file = open("text.txt","a")
        file.write(z+"\n")
        file.close()



    elif выбор == "2":

        file = open("text.txt","r")
        z1 = file.read()

        file.close()
        print(z1)



    elif выбор == "3":
        break