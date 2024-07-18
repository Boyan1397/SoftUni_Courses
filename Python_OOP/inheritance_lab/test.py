class Grandpop:
    def __init__(self, eyes):
        self.eyes = eyes

class Father(Grandpop):
    def __init__(self, smile, eyes):
        super().__init__(eyes)
        self.smile = smile

class Mother:
    def __init__(self, nose):
        self.nose = nose


class Son(Father, Mother):
    def __init__(self,smile,  eyes, nose, height):
        Father.__init__(self, eyes, smile)
        Mother.__init__(self, nose)
        self.height = height


son = Son("bright", "blue", "small", "1,89")
print(son.smile)
print(son.eyes)