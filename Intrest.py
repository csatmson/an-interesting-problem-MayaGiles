#Intrest Calculator 1

x = int(input("How many years will you be saving for?"))

#A = P(1 + r/n)**nt

a = 1000 * (1 + 0.05 / 12)**(12 * x)

print("After ", x, "years, you will have ", a, "dollars.")
