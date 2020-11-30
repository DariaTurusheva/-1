def test_list(tmp_list):
    new_variable =''
    while True:
        new_variable = input("Ведите переменную: ")
        if new_variable == '':
            return tmp_list
        tmp_list.append(new_variable)


print("Введите данные для списка:")
list1 = []
test_list(list1)

ver = input("Введите нужную переменную: ")

if len(list1) == 0:
    print("Пустой список")
else:
    position = []
    for i in range(0,len(list1)):
        if ver == list1[i]:
            position.append(i)
    if len(position) == 0:
        print(0)
    else:
        print(position)
