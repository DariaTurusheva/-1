def test_list(tmp_list):
    new_ex =''
    while True:
        new_ex = input("Пожалуйста, введите переменную: ")
        if new_ex == '':
            return tmp_list
        tmp_list.append(new_ex)


print("Введите данные для первого списка")
list1 = []
test_list(list1)
print("Введите данные для второго списка")
list2 = []
test_list(list2)


res_list=[]
while len(list1)>0 or len(list2)>0:
    if len(list2) == 0 :
        res_list.append(list1[0])
        del list1[0]
    elif len(list1) == 0:
        res_list.append(list2[0])
        del list2[0]
    elif list1[0] < list2[0]:
        res_list.append(list1[0])
        del list1[0]
    else:
        res_list.append(list2[0])
        del list2[0]
        

print(res_list)