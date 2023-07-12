import matplotlib.pyplot as plt

categories = ["Category A", "Category B", "Category C", "Catergory D","Category E"]
percentages = [15, 25, 12, 15,30]

explode = [0, 0.1, 0, 0, 0.2]
colors = ["red", "blue", "green", "orange", "black"]

plt.pie(percentages,  explode = explode, labels = categories, colors = colors, shadow = True)
plt.title("Percentage Destribution")
plt.legend(categories)
plt.show()
