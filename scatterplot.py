import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer

# Number of data points
numberofpoints = 124700000 # 124.7 million

# Generate x values
total_time_total = default_timer()
x_value_time_total = default_timer()
x_values = np.arange(numberofpoints)
x_value_time = default_timer() - float(x_value_time_total)
print("X values completed, took "+ str(x_value_time)+" seconds")

# Generate y values with some random noise, but not less than 0
y_value_time_total = default_timer()
y_values = np.maximum(0, numberofpoints - x_values + np.random.normal(0, (numberofpoints/2), numberofpoints))
y_value_time = default_timer() - float(y_value_time_total)
print("Y values completed, took "+ str(y_value_time)+" seconds")

# Adjust the range and step size for x_ticks and y_ticks
tick_time_total = default_timer()
y_ticks = np.arange(0, int(np.max(y_values))+1, int(np.max(y_values)//10))  # 10 ticks on the y-axis
tick_time = default_timer() - float(tick_time_total)
print("Ticks completed, took "+ str(tick_time)+" seconds")

fig, ax = plt.subplots()
# Plot the values

scatter_timer_total = default_timer()
plt.scatter(x_values, y_values, s=.0001, color = "black")
scatter_timer = default_timer() - float(scatter_timer_total)
print("Points scattered, took "+str(scatter_timer)+" seconds")

style_time_total = default_timer()
fig.set_facecolor('black')
ax.set_xlabel("Person's Age (0-100)", color="white")
ax.set_ylabel("Times 'why' is said in one year", color="white")
plt.xticks([])  # No x-ticks
plt.yticks(y_ticks)
style_time = default_timer() - float(style_time_total)
print("Styles completed, took " + str(style_time)+" seconds")

label_time_total = default_timer()
for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_color('white')
label_time = default_timer() - float(label_time_total)
total_time = default_timer() - float(total_time_total)
print("Labels completed, took "+str(label_time)+" seconds")
print("Graph completed, took " + str(total_time)+ " total")
plt.show()
