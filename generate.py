import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

distr= stats.alpha(a=3.57, loc=0.0, scale=1.0)
start = distr.ppf(0.01)
end = distr.ppf(0.99)
size = 10000

x = np.linspace(start, end, size)
y = distr.pdf(x) #pmf cdf
 
plt.xkcd()
sad = plt.text(1500,2,':(')
sad.set_rotation(-90)
sad.set_fontsize(40)
sad.set_horizontalalignment('center')
plt.text(3500,3,'/')
plt.text(4000,3.5,'I just want to be normal...')
plt.xticks([])
plt.yticks([])

plt.plot(y)
plt.show()
