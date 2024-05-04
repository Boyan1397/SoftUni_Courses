first_nums = [el for el in range(1,12)]
numbers = [num if num % 2 == 0 else "odd_num" for num in range(1, 11)]
        #element#2 if        #3else_element   #1for
print(numbers)

nums = [1,2,3,4,5]
nums2 =nums
nums.insert(0,444)
print(nums2)
#refertno e za tova se promenqt i davata lista nums i nums2
nums_list = [1,2,3,4,5,6]
nums_list2 = nums_list
nums_list.append(24234)
print(nums_list)
print(nums_list2)
#listovete sa referntni

