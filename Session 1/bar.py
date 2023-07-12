import matplotlib.pyplot as plt

products = ['Product 1', 'Product 2', 'Product 3', 'Product 4']
sales = [320, 250, 430, 510]

plt.bar(products,sales, color = ['red', 'blue','green','orange'])
plt.xlabel("Products")
plt.ylabel("Slaes")


plt.show()


