while True:
    print("\n=== TO-DO СПИСОК ===")
    print("1. Добавить задачу")
    print("2. Показать все задачи")
    print("3.Удалить задачу")
    print("4. Удалённые задачи")
    print("5. Выход")

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
        file = open("text.txt", "r")
        задачи = file.readlines()
        file.close()
        for i in range(len(задачи)):
            print(f"{i + 1}. {задачи[i]}", end="")
        номер = int(input("Какую удалить? "))
        удалённая = задачи[номер - 1]
        del задачи[номер - 1]


        file = open("deleted.txt", "a")
        file.write(удалённая)
        file.close()


        file = open("text.txt", "w")
        file.writelines(задачи)
        file.close()
    elif выбор == "4":
        file = open("deleted.txt", "r")  
        z17 = file.read()
        file.close()
        print(z17)
    elif выбор == "5":
        break
