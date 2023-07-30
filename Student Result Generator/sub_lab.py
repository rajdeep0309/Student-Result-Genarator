# import sub_theory


class sub_lab:
    def __init__(self, marks, pca):
        self.marks = marks
        self.pca = pca
        # self.att = att
    # ................finding total

    def total(self):
        self.ans = self.marks+self.pca
        return (self.ans)

    # ............creditpoints calculation
    def return_creditPoint(self):
        self.ans = self.total()

        self.points = 0
        self.credit = 0
        if self.ans > 90 and self.ans <= 100:
            self.points = 10
            self.credit = 4
        elif self.ans > 80:
            self.points = 9
            self.credit = 3.5
        elif self.ans > 70:
            self.points = 8
            self.credit = 3
        elif self.ans > 60:
            self.points = 7
            self.credit = 2.5
        elif self.ans > 50:
            self.points = 6
            self.credit = 2
        elif self.ans == 0:
            self.points = 0
            self.credit = 0
        else:
            self.points = 5
            self.credit = 1.5

        self.sub_credit = self.credit

        return self.credit * self.points

    #  credits
    def return_credit(self):
        return self.sub_credit

    def return_points(self):
        return self.points


# sum_creditpoints = 0
# sum_credits = 0
# for i in range(3):
#     marks = int(input("marks:"))
#     pca = int(input("pca:"))
#     lab1 = sub_lab(marks, pca)
#     sum_creditpoints += lab1.total_creditPoint(lab1.total())
#     sum_credits += lab1.return_credit()
#     print(lab1.total())
#     print(lab1.total_creditPoint(lab1.total()))
#     print(lab1.return_credit())
# sgpa = round(sum_creditpoints/sum_credits, 2)
# print(sgpa)
