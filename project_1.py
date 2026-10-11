import matplotlib.pyplot as plt
import numpy as np
from math import floor

stepdif = 5.0/16.0

out_1 = [0.00009095, 0.31259, 0.60984, 0.92234,
         1.28, 1.59, 1.89, 2.2, 
         2.5, 2.81, 3.11, 3.42, 
         3.78, 4.09, 4.39, 4.7]
out_2 = [0.00009095, 0.31259, 0.62509, 0.93759,
         1.25, 1.56, 1.88, 2.19, 
         2.5, 2.81, 3.13, 3.44, 
         3.75, 4.06, 4.38, 4.69]
out_ideal = np.arange(0 , 5 , stepdif)

step = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
out1 = np.array(out_1)
steps = np.array(step)



plt.xlabel("Binary step")
plt.ylabel("Vout")
plt.title("Vout for Ideal Transfer function and Perfect Tranfer function")


#step function y=a*floor(x-h)+k where a is step difference 
perfect_x = np.linspace(0, 15, 500)
perfect_y = [(stepdif*floor(i)) for i in perfect_x]


#plot ideal 
plt.plot(steps, out_ideal, linewidth = 1)

#plot perfect
plt.plot(perfect_x, perfect_y)
plt.legend(["ideal", "perfect"], loc="lower right")
plt.show()







#plot 1
plt.xlabel("Binary step")
plt.ylabel("Vout")
plt.title("Vout for Binary Weighted and Ideal Transfer function")
plt.plot(steps, out_ideal, linewidth = 1)
plt.plot(steps, out_1)
plt.legend(["ideal", "Binary"], loc="lower right")
plt.show()

#plot 2
plt.xlabel("Binary step")
plt.ylabel("Vout")
plt.title("Vout for R-2R and Ideal Transfer function")
plt.plot(steps, out_ideal, linewidth = 1)
plt.plot(steps, out_2)
plt.legend(["ideal", "R-2R"], loc="lower right")
plt.show()