#filter() е използва за избор само на елементите, които отговарят на определено условие
def is_even(n): #3 suzdavame funkciq i i davame parameter
    return n % 2 == 0 #4 davame mu kakvo da ni vurne i shte go vurne samo ako e True

nums = [4,2,5,1,34,123,978,6,8,7,47] #1 dava ni list
evens = list(filter(is_even,nums)) #2 davame mu funkciq koqto shte suzdadem i imeto ot lista ot koito shte vzima
print(evens) #printirame

#lamda() #better and shorter to use lamda if we only need it once
nums = [4,2,5,1,34,123,978,6,8,7,47]
even_nums = list(filter(lambda f: f % 2 == 0,nums))
print(even_nums)
#map() #се използва за трансформиране на всеки елемент на итерируем обект с помощта на предоставената функция,
updated_nums = list(map(lambda a:a * 2,even_nums))
print(updated_nums)
