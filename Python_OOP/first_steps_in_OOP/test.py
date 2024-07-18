x = "my global"
def smth():
    global x
    x = "new global"
    print(x)

print(x)
(smth())
print(x)