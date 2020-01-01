""" File with plots of the comparison between the various approximations """
#%%

import numpy as np 
import matplotlib.pyplot as plt
import os
from matplotlib import cm
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

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
""" Plot 4th vs 6th order expansion """

plt.style.use('default')
colors = ['darkslateblue', 'darkorange']
fig1, ax1 = plt.subplots(figsize=(6,6))
ax1.semilogy(ej_vec, d_anh_four, linewidth=2.0, color = colors[0], \
    label='$|\\Delta \\delta_{01}/\\delta_{01}|^{(4th)}$')
ax1.semilogy(ej_vec, d_anh_six, '--', linewidth=2.0, color = colors[0], \
    label='$|\\Delta \\delta_{01}/\\delta_{01}|^{(6th)}$')
ax1.semilogy(ej_vec, d_e10_four, linewidth=2.0, color = colors[1], \
    label='$|\\Delta \\omega_{01}/\\omega_{01}|^{(4th)}$')
ax1.semilogy(ej_vec, d_e10_six, '--', linewidth=2.0, color = colors[1], \
    label='$|\\Delta \\omega_{01}/\\omega_{01}|^{(6th)}$')
ax1.set_xlabel('$E_J/E_C$', fontsize=20)
plt.legend(fontsize=14)
fig1.savefig(path+'fourth_vs_six.pdf')
plt.show()


# %%
""" Plot 4th vs 4th RWA """

plt.style.use('default')
fig2, ax2 = plt.subplots(figsize=(6,6))
ax2.semilogy(ej_vec, d_anh_four, linewidth=2.0, color = colors[0], \
    label='$|\\Delta \\delta_{01}/\\delta_{01}|^{(4th)}$')
ax2.semilogy(ej_vec, d_anh_four_rwa, ':', linewidth=2.0, color = colors[0], \
    label='$|\\Delta \\delta_{01}/\\delta_{01}|_{\\mathrm{RWA}}^{(4th)}$')
ax2.semilogy(ej_vec, d_e10_four, linewidth=2.0, color = colors[1], \
    label='$|\\Delta \\omega_{01}/\\omega_{01}|^{(4th)}$')
ax2.semilogy(ej_vec, d_e10_four_rwa, ':', linewidth=2.0, color = colors[1], \
    label='$|\\Delta \\omega_{01}/\\omega_{01}|_{\\mathrm{RWA}}^{(4th)}$')
ax2.set_xlabel('$E_J/E_C$', fontsize=20)
plt.legend(fontsize=14)
fig2.savefig(path+'fourth_vs_fourth_RWA.pdf')
plt.show()

# %%
""" Plot 6th vs 6th RWA """

plt.style.use('default')
colors = ['darkslateblue', 'darkorange']
fig3, ax3 = plt.subplots(figsize=(6,6))
ax3.semilogy(ej_vec, d_anh_six, '--', linewidth=2.0, color = colors[0], \
    label='$|\\Delta \\delta_{01}/\\delta_{01}|^{(6th)}$')
ax3.semilogy(ej_vec, d_anh_six_rwa, ':', linewidth=2.0, color = colors[0], \
    label='$|\\Delta \\delta_{01}/\\delta_{01}|_{\\mathrm{RWA}}^{(6th)}$')
ax3.semilogy(ej_vec, d_e10_six, '--', linewidth=2.0, color = colors[1], \
    label='$|\\Delta \\omega_{01}/\\omega_{01}|^{(6th)}$')
ax3.semilogy(ej_vec, d_e10_six_rwa, ':', linewidth=2.0, color = colors[1], \
    label='$|\\Delta \\omega_{01}/\\omega_{01}|_{\\mathrm{RWA}}^{(6th)}$')
ax3.set_xlabel('$E_J/E_C$', fontsize=20)
plt.legend(fontsize=14)
fig3.savefig(path+'six_vs_six_RWA.pdf')
plt.show()


# %%
