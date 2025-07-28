# PIP

import numpy as np
import pandas as pd
import requests

print(np.version.version)
print(pd.__version__)

array = np.array([1,2,3,4])
print(array * 10)

# pip list
# pip show librery

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

print(response.json())

from my_package import aritmetics

print(aritmetics.sum(5,12))