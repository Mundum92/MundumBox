#immutable_var=('Телефон',250980,True,84,'Килограмма')
#print(immutable_var)
#immutable_var[0]=5
#immutable_var[2]='двадцать пять'
#при работе со списками(в скобках или без),с строками цифрами или лог операциями,сохраняется их неизменность -упорядоченнсть
#по этому из нельзя изменить-изменить можно кортежи (с квадратными скобками)
mutable_list=[250980,'Home Phone',True,7.8]
print(mutable_list)
mutable_list[0]='двадцать пять ноль девять восемдесят'
mutable_list[1]='домашний телефон'
mutable_list[2]=False
mutable_list[3]=5
print(mutable_list)
mutable_list.remove(False)
print(mutable_list)
mutable_list.append('Pizza')
print(mutable_list)
mutable_list.append(['Koechto',60])
print(mutable_list)
name=('Privet')
mutable_list.extend(name)
print(mutable_list)
name=['Привет']
mutable_list.extend(name)
print(mutable_list)
