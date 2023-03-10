import numpy as np
import scipy
from scipy.optimize import minimize_scalar
from scipy.interpolate import interp1d
file_1 = "./I_q_IPA_exp.npy"
file_2 = "./I_q_IPA_model.npy"

data1= np.load(file_1)
data2= np.load(file_2)
f = lambda: (x-2) * (x+2) **2
res = minimize_scalar(f, bounds = (-100,100), method="bounded")



