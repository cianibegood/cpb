""" File with plots of the comparison between the various approximations """
#%%

import numpy as np 
import matplotlib.pyplot as plt
import os

#%%
path = os.getcwd()+'/energy_levels/data_approximation_comparison/'
ej_vec = np.load(path + 'ej_vec.npy')
d_e10_four = np.load(path + 'd_e10_four.npy')
d_e10_four_rwa = np.load(path + 'd_e10_four_rwa.npy')
d_e10_six = np.load(path + 'd_e10_six.npy')
d_e10_six_rwa = np.load(path + 'd_e10_six_rwa.npy')
d_anh_four = np.load(path + 'd_anh_four.npy')
d_anh_four_rwa = np.load(path + 'd_anh_four_rwa.npy')
d_anh_six = np.load(path + 'd_anh_six.npy')
d_anh_six_rwa = np.load(path + 'd_anh_six_rwa.npy')


# %%
