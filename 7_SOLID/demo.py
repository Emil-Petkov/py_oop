# class StudentTaxes:
#     def __init__(self, name, semester_tax, average_grade):
#         self.name = name
#         self.semester_tax = semester_tax
#         self.average_grade = average_grade
#
#     def get_discount(self):
#         if self.average_grade > 5:
#             return self.semester_tax * 0.4
#         else:
#             return self.semester_tax
#
#
# class AdditionalDiscount(StudentTaxes):
#     def get_discount(self):
#         result = super().get_discount()
#         if result:
#             return result
#         if 4 < self.average_grade <= 5:
#             return self.semester_tax * 0.2
#
#
# student = StudentTaxes("Student Name", 1000, 6)
#
# print(student.get_discount())  # 400.0

########################################################################

class StudentTaxes:
    def __init__(self, name, semester_tax, average_grade):
        self.name = name
        self.semester_tax = semester_tax
        self.average_grade = average_grade

    def get_discount(self):
        if self.average_grade > 5:
            return self.semester_tax * 0.4

        return 0


class AdditionalDiscount(StudentTaxes):
    def get_discount(self):
        result = super().get_discount()
        if result > 0:
            return result
        if 4 < self.average_grade <= 5:
            return self.semester_tax * 0.2

        return 0


student = [StudentTaxes("Emil", 1000, 6),  # 400.0
           StudentTaxes("Ivan", 1000, 5.5),  # 400.0
           StudentTaxes("Dragan", 1000, 5)  # 0
           ]

[print(s.get_discount()) for s in student]
