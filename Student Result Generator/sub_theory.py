class sub_theo:
    def __init__(self, marks, ca, att):
        self.marks = marks
        self.ca = ca
        self.att = att
    # ................finding total

    def total(self):
        self.ans = self.marks + self.ca + self.att
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
#     ca = int(input("ca:"))
#     att = int(input("attendence:"))
#     s1 = sub_theo(marks, ca, att)
    # sum_creditpoints += s1.total_creditPoint(s1.total())
    # sum_credits += s1.return_credit()
#     print(s1.total())
#     print(s1.total_creditPoint(s1.total()))
#     print(s1.return_credit())
# sgpa = round(sum_creditpoints/sum_credits, 2)
# print(sgpa)
