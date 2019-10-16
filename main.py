import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(os.getcwd() + '/data/pitchData2019.csv', error_bad_lines=False)
print (data)
