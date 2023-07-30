from sub_theory import *
from sub_lab import *
sum_creditpoints = 0
sum_credits = 0
for i in range(3):

    s1 = sub_theo(int(input("marks:")), int(
        input("ca:")), int(input("attendence:")))
    sum_creditpoints += s1.total_creditPoint(s1.total())
    sum_credits += s1.return_credit()
for i in range(3):
    lab1 = sub_lab(int(input("marks:")), int(
        input("pca:")))
    sum_creditpoints += s1.total_creditPoint(s1.total())
    sum_credits += s1.return_credit()
print(s1.total())
print(lab1.total())
print(sum_creditpoints)
print(sum_credits)
sgpa = round(sum_creditpoints/sum_credits, 2)
print(sgpa)
