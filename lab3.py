# 1, 3
#def read_file():
#    file = "example.txt"
#    read_mode = input('Введите метод чтения (весь, построчно): ')
#   with open(file, 'r') as file:
#        if read_mode == 'весь':
#            content = file.read()
#            print(content)
#        elif read_mode == 'построчно':
#            for line in file:
#                print(line, end='')
#        else:
#            print('Неверный режим чтения')
#           read_file()

#read_file()

# 2

def writetofile():
    user_text = input('Введите текст для записи в новый файл: ')
    with open('user_input.txt', 'w') as file:
        file.write(user_text + '\n')
    print('Текст записан в файл user_input.txt')

def appendtofile():
    user_text = input('Введите текст для добавления: ')
    with open('user_input.txt', 'a') as file:
        file.write(user_text + '\n')
    print('Текст добавлен в файл user_input.txt')

writetofile()

appendtofile()
