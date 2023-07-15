class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4
        else:
            return self.semester_tax


class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()
        if result:
            return result
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2


student = StudentTaxes("Student Name", 1000, 6)
student2 = StudentTaxes("Student Name2", 1000, 3)
student3 = StudentTaxes("Student Name3", 1000, 4)

discount = student.get_discount()
discount2 = student2.get_discount()
discount3 = student3.get_discount()

print(discount)
print(discount2)
print(discount3)
