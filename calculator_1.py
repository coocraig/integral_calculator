import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.integrate import quad


def rec_rule_int_calc(lower_bound, upper_bound, func, accuracy = 100000, graph = True, progress = True):
    
    # Creating array of segments between lower and upper bound points
    sequence = np.linspace(lower_bound, upper_bound, accuracy)

    # Finding the "width" of that block
    seq_width = sequence[1] - sequence[0]

    # The running total area of the strips taken
    total = 0

    for index, item in enumerate(sequence):
        total = total + func(item) * seq_width

        if(progress and index % 1000000 == 0):
            perc = 100 * round((index / len(sequence)), 4)
            print(f"{perc}%")
    print(total)

    if(graph):
        plt.plot(np.linspace(0, upper_bound*3, 1000), func(np.linspace(0, upper_bound*3, 1000)))

        # Shade the area under the curve between two points (e.g., between x=2 and x=6)
        plt.fill_between(sequence, func(sequence), where=(sequence >= lower_bound) & (sequence <= upper_bound), color='skyblue', alpha=0.4)

        # Add gridlines
        plt.grid(True)

        # Set x-axis and y-axis limits to make the plot larger than the shaded area
        plt.xlim(lower_bound, upper_bound * 1.1)
        plt.ylim(0, func(upper_bound * 1.1))


        if(min(func(sequence))<0):
            plt.ylim(min(func(sequence))*1.1, func(upper_bound * 1.1))

        # Configure the ticks for unit square grid boxes
        plt.xticks(np.arange(0, upper_bound * 1.1 + 5, 1))  # Set x-axis ticks at intervals of 1

        # Adjust y-ticks based on the function's values
        plt.yticks(np.arange(0, func(upper_bound * 1.1) + 5, 1))  # Set y-axis ticks at intervals of 1


        # Add labels and a title
        plt.title(f'Plot of function with Shaded Area, Area = {round(total,2)}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.show()
    
    result, error = quad(func, lower_bound, upper_bound)

    return (total, result)




def func1(x):
    # return (2*x)
    # return (1/math.sqrt(2*math.pi))*math.e**(-(x**2/2))
    # return np.sin(1000*x)
    return np.exp(-x**2)


answers = rec_rule_int_calc(-5, 25, func1, accuracy=9999999, graph=False)

print(f"Estimated integral value: {round(answers[0],8)}")
print(f"Calculated using scipy  : {round(answers[1],8)}")

# min(func(sequence))