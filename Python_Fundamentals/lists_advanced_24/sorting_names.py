names = input().split(", ")
sorted_list = sorted(names,key=lambda x:(-len(x),x))
                   #1list #2key+lambda#3условията

print(sorted_list)

#Lilly, Tim, Kate, Tom, Alex
#['Lilly', 'Alex', 'Kate', 'Tim', 'Tom']