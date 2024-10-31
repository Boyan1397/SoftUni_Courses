class StudentT:
    def __init__(self, name, tax, average_grade):
        self.name = name
        self.tax = tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade >= 5:
            return self.tax * 0.4


class AdditionalDiscount(StudentT):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 5 > self.average_grade >= 4:
            return self.tax * 0.2


st = StudentT("bobo", 1000, 4)
print(st.get_discount())

mor = AdditionalDiscount("Bobo", 10000, 5.5)
print(mor.get_discount())


