""" Energy levels of the CPB and the transmon approximation """

#%%

import numpy as np
import math
import scipy.linalg as la
import matplotlib.pyplot as plt
import cpb 

#%%
""" Data """

ec_ref = 0.25 # [GHz]
ec = 1 
ej = 50 
ng = 0 
qubit = cpb.CPB(ec, ej, ng, ec_ref)


# %%
