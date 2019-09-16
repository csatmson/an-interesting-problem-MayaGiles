#Intrest Calculator 2

t = int(input("How many years will you be saving for?"))

p = int(input("How much money are do you plan to invest?"))

r = int(input("What is the interest rate that you bank offers (as a whole number please) ?"))

r = r / 100

#A = P(1 + r/n)**nt

a = p * (1 + r / 12)**(12 * t)

print("If you invest ", p, "dollars, after ", t, "years, with an interest rate of ", r, ", you will have a total of ", a, "dollars.")
