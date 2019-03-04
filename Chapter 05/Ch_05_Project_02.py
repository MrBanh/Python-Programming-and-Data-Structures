'''
(Financial application: compute future tuition)

Suppose that the tuition for a university is $10,000 this year and increases
5% every year. In one year, the tuition will be $10,500. Write a program that
displays the tuition in 10 years and the total cost of 4 years’ worth of
tuition starting after the 10th year.
'''
tuition = 10000.00
tuition_rate = 0.05
num_of_years = 14
total_cost = 0
tuition_10th_year = 0

for year in range(1, num_of_years):
    tuition += (tuition * .05)
    if year >= 10:
        total_cost += tuition

    if year == 10:
        tuition_10th_year = tuition

print("Tuition in ten years: $", format(tuition_10th_year, ".2f"))
print("Total cost for four years' worth of tuition after the tenth year: $",
      format(total_cost, ".2f"))
