#pop() премахва по индекс
some_list = [1001,2,3,4,5,6,14214]
some_list.pop(0)
print(some_list)
#removе премахва назован от нас елемент в листа
texts = ["banan","Lora","Antonia","Todorka"]
texts.remove("Todorka")
print(texts)
#insert() добавя зададен от нас елемент по ИНДЕКС
some_numbers = [1,3,5,6,7,0,273]
some_numbers.insert(2, "cocos")
                 #1index2element
print(some_numbers)
#index чрез зададен определен елемент намираме индекса
ind_nums = [1,2,3,4,5,6]
print(ind_nums.index(3))
#reverse()
my_list = [1,2,3,5,6,7]
my_list.reverse()
print(my_list)
#copy()  се използва Запазване на Оригиналните Данни(началният лист)
nums = [1,2,3,4,5,6]
nums2 = nums.copy()
nums.append(1010)
print(nums)
print(nums2)
#count() дава броя на определени от нас елемнти в листа
my_list = [1,2,3,4,4,4,3,2,4,4]
count = my_list.count(4)
print(count)
#clear()  премахва всички елементи в листа
some_nums = [1,2,3,4,5,6]
some_nums.clear()
print(some_nums)
