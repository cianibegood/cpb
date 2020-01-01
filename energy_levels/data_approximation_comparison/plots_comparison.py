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
""" Plot E01 4th vs 6th and RWA order expansion """

plt.style.use('default')
colors = ['orangered', 'darkslateblue']
fig1, ax1 = plt.subplots(figsize=(6,6))
ax1.plot(ej_vec, d_e10_four, linewidth=2.0, color = colors[0], \
    label='4th order')
ax1.plot(ej_vec, d_e10_four_rwa, '--', linewidth=2.0, color = colors[0], \
    label='4th order RWA')
ax1.plot(ej_vec, d_e10_six, linewidth=2.0, color = colors[1], \
    label='6th order')
ax1.plot(ej_vec, d_e10_six_rwa, '--', linewidth=2.0, color = colors[1], \
    label='6th order RWA')
ax1.set_xlabel('$E_J/E_C$', fontsize=16)
ax1.set_ylabel('$\\Delta  \\omega_{01} /\\omega_{01}$', fontsize=16)
plt.legend(fontsize=14)
fig1.savefig(path+'omega01_fourth_vs_six.pdf', bbox_inches="tight")
plt.show()

#%%

plt.style.use('default')
colors = ['orangered', 'darkslateblue']
fig1_log, ax1_log = plt.subplots(figsize=(6,6))
ax1_log.semilogy(ej_vec, np.abs(d_e10_four), linewidth=2.0, color = colors[0], \
    label='4th order')
ax1_log.semilogy(ej_vec, np.abs(d_e10_four_rwa), '--', linewidth=2.0, color = colors[0], \
    label='4th order RWA')
ax1_log.semilogy(ej_vec, np.abs(d_e10_six), linewidth=2.0, color = colors[1], \
    label='6th order')
ax1_log.semilogy(ej_vec, np.abs(d_e10_six_rwa), '--', linewidth=2.0, color = colors[1], \
    label='6th order RWA')
ax1_log.set_xlabel('$E_J/E_C$', fontsize=16)
ax1_log.set_ylabel('$| \\Delta  \\omega_{01} /\\omega_{01} |$', fontsize=16)
plt.legend(fontsize=14)
fig1_log.savefig(path+'omega01_fourth_vs_six_log.pdf', bbox_inches="tight")
plt.show()

#%%
""" Plot anharmonicity 4th vs 6th and RWA order expansion """

plt.style.use('default')
colors = ['orangered', 'darkslateblue']
fig2, ax2 = plt.subplots(figsize=(6,6))
ax2.plot(ej_vec, d_anh_four, linewidth=2.0, color = colors[0], \
    label='4th order')
ax2.plot(ej_vec, d_anh_four_rwa, '--', linewidth=2.0, color = colors[0], \
    label='4th order RWA')
ax2.plot(ej_vec, d_anh_six, linewidth=2.0, color = colors[1], \
    label='6th order')
ax2.plot(ej_vec, d_anh_six_rwa, '--', linewidth=2.0, color = colors[1], \
    label='6th order RWA')
ax2.set_xlabel('$E_J/E_C$', fontsize=20)
ax2.set_ylabel('$\\Delta | \\delta |/|\\delta|$', fontsize=16)
plt.legend(fontsize=14)
fig2.savefig(path+'anharmonicity_fourth_vs_six.pdf', bbox_inches="tight")
plt.show()

#%%
""" Plot anharmonicity 4th vs 6th and RWA order expansion """

plt.style.use('default')
colors = ['orangered', 'darkslateblue']
fig2_log, ax2_log = plt.subplots(figsize=(6,6))
ax2_log.semilogy(ej_vec, np.abs(d_anh_four), linewidth=2.0, color = colors[0], \
    label='4th order')
ax2_log.semilogy(ej_vec, np.abs(d_anh_four_rwa), '--', linewidth=2.0, color = colors[0], \
    label='4th order RWA')
ax2_log.semilogy(ej_vec, np.abs(d_anh_six), linewidth=2.0, color = colors[1], \
    label='6th order')
ax2_log.semilogy(ej_vec, np.abs(d_anh_six_rwa), '--', linewidth=2.0, color = colors[1], \
    label='6th order RWA')
ax2_log.set_xlabel('$E_J/E_C$', fontsize=20)
ax2_log.set_ylabel('$|\\Delta | \\delta |/\\delta|$', fontsize=16)
plt.legend(fontsize=14)
fig2_log.savefig(path+'anharmonicity_fourth_vs_six_log.pdf', bbox_inches="tight")
plt.show()

# %%
