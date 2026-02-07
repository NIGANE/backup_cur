import matplotlib.pyplot as plt

# Your data records
data = [
    ["Dragon", 2500, "Fire"],
    ["Kraken", 2200, "Water"],
    ["Golem",  3000, "Earth"]
]
columns = ("Card Name", "Attack", "Element")

fig, ax = plt.subplots()
ax.axis('tight')
ax.axis('off')

# Creating the table record visualization
table = ax.table(cellText=data, colLabels=columns, loc='center', cellLoc='center')
table.set_fontsize(14)
table.scale(1, 2) # Makes the rows taller for readability

plt.show()