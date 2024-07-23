my_dict={'Женя':1992,'Коля':1995,'Толя':1986}
print(my_dict)
print(my_dict.get('Женя'))
print(my_dict.get('Катя','Такого имени нет в словаре'))
my_dict['Алексей']=1994
my_dict['Миша']= 1985
print(my_dict)
a=my_dict.pop('Женя')
b=my_dict.pop('Коля')
print(my_dict)
print(a)
print(b)
my_set={1,2,3,4,5,2,4,3,1,5,'Женя','a','b','c','b','c','a',(2,4,5)}
print( my_set)
my_set.add(6)
my_set.add('Коля')
print( my_set)
my_set.remove(1)
print( my_set)
