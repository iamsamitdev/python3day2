# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("Hello Jupyter Notebook")

# %%
print(5**3)

# %%
# %matplotlib inline

# %%
plt.plot([2, 4, 10, 12, 9])

# %%

p = np.linspace(0, 20, 100)
plt.plot(p, np.sin(15*p))
plt.show()

# %%
df = pd.read_csv(
    'https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/iris.csv')
df.sample(10)
