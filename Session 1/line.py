import matplotlib.pyplot as plt

years = [2010, 2011, 2012, 2013,2020,2023]
population = [8.5, 9, 9, 10.5,10.3, 8.5]

plt.plot(years, population, marker = "o", linestyle = "--", color = "green")
plt.xlabel("Year")
plt.ylabel("Population (in billions)")
plt.title("Population Growth Over Years")

plt.show()
