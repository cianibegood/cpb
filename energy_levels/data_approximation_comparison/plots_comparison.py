""" File with plots of the comparison between the various approximations """
#%%

import numpy as np 
import matplotlib.pyplot as plt
import os
import matplotlib
matplotlib.rcParams['mathtext.fontset'] = 'cm'

#%%
path = os.getcwd()+'/energy_levels/data_approximation_comparison/'
ej_vec = np.load(path + 'ej_vec.npy')
d_e10_four = np.load(path + 'd_e10_four.npy')
d_e10_four_rwa = np.load(path + 'd_e10_four_rwa.npy')
d_e10_four_rwa_next = np.load(path + 'd_e10_four_rwa_next.npy')
d_e10_six = np.load(path + 'd_e10_six.npy')
d_e10_six_rwa = np.load(path + 'd_e10_six_rwa.npy')
d_e10_six_rwa_next = np.load(path + 'd_e10_six_rwa_next.npy')
d_anh_four = np.load(path + 'd_anh_four.npy')
d_anh_four_rwa = np.load(path + 'd_anh_four_rwa.npy')
d_anh_four_rwa_next = np.load(path + 'd_anh_four_rwa_next.npy')
d_anh_six = np.load(path + 'd_anh_six.npy')
d_anh_six_rwa = np.load(path + 'd_anh_six_rwa.npy')
d_anh_six_rwa_next = np.load(path + 'd_anh_six_rwa_next.npy')
lw = 2.5
t = 14



# %%
""" Plot E01 4th vs 6th and RWA order expansion """

colors = ['darkorange', 'mediumblue']
fig1, ax1 = plt.subplots(figsize=(6,6))
ax1.plot(ej_vec, d_e10_four, \
    linewidth=lw, color = colors[0], label='$4$-th order')
ax1.plot(ej_vec, d_e10_four_rwa, '--', \
    linewidth=lw, color = colors[0], label='$4$-th order RWA')
ax1.plot(ej_vec, d_e10_six, \
    linewidth=lw, color = colors[1], label='$6$-th order')
ax1.plot(ej_vec, d_e10_six_rwa, '--', \
    linewidth=lw, color = colors[1], label='$6$-th order RWA')
ax1.set_xlabel('$E_J/E_C$', fontsize=20)
ax1.set_ylabel('$\\Delta  \\omega_{01} /\\omega_{01}$', fontsize=20)
ax1.tick_params(axis='both', labelsize=t)
plt.legend(loc='lower right', fontsize=14)
fig1.savefig(path+'omega01_fourth_vs_six.pdf', bbox_inches="tight")
plt.show()

#%%

fig1_log, ax1_log = plt.subplots(figsize=(6,6))
ax1_log.semilogy(ej_vec, np.abs(d_e10_four), \
    linewidth=lw, color = colors[0], label='$4$-th order')
ax1_log.semilogy(ej_vec, np.abs(d_e10_four_rwa), '--', \
    linewidth=lw, color = colors[0], label='$4$-th order RWA')
ax1_log.semilogy(ej_vec, np.abs(d_e10_six), \
    linewidth=lw, color = colors[1], label='$6$-th order')
ax1_log.semilogy(ej_vec, np.abs(d_e10_six_rwa), '--', \
    linewidth=lw, color = colors[1], label='$6$-th order RWA')
ax1_log.set_xlabel('$E_J/E_C$', fontsize=20)
ax1_log.set_ylabel('$| \\Delta  \\omega_{01} /\\omega_{01} |$', fontsize=20)
plt.legend(loc='lower right', fontsize=14)
ax1_log.tick_params(axis='both', labelsize=t)
fig1_log.savefig(path+\
    'omega01_fourth_vs_six_log.pdf', bbox_inches="tight")
plt.show()

#%%
""" Plot E01 4th vs 6th RWA order expansion vs next RWA """

fig1_next, ax1_next = plt.subplots(figsize=(6,6))
ax1_next.plot(ej_vec, d_e10_four_rwa, '--', \
    linewidth=lw, color = colors[0], label='$4$-th order RWA')
ax1_next.plot(ej_vec, d_e10_four_rwa_next, ':', \
    linewidth=lw, color = colors[0], label='$4$-th order next RWA')
ax1_next.plot(ej_vec, d_e10_six_rwa, '--', \
    linewidth=lw, color = colors[1], label='$6$-th order RWA')
ax1_next.plot(ej_vec, d_e10_six_rwa_next, ':', \
    linewidth=lw, color = colors[1], label='$6$-th order next RWA')
ax1_next.set_xlabel('$E_J/E_C$', fontsize=20)
ax1_next.set_ylabel('$\\Delta  \\omega_{01} /\\omega_{01}$', fontsize=20)
plt.legend(loc='lower right', fontsize=14)
ax1_next.tick_params(axis='both', labelsize=t)
fig1_next.savefig(path+\
    'omega01_fourth_vs_six_rwa_next.pdf', bbox_inches="tight")
plt.show()

#%%

fig1_next_log, ax1_next_log = plt.subplots(figsize=(6,6))
ax1_next_log.semilogy(ej_vec, np.abs(d_e10_four_rwa), '--', \
    linewidth=lw, color = colors[0], label='$4$-th order RWA')
ax1_next_log.semilogy(ej_vec, np.abs(d_e10_four_rwa_next), ':', \
    linewidth=lw, color = colors[0], label='$4$-th order next RWA')
ax1_next_log.semilogy(ej_vec, np.abs(d_e10_six_rwa), '--', \
    linewidth=lw, color = colors[1], label='$6$-th order RWA')
ax1_next_log.semilogy(ej_vec, np.abs(d_e10_six_rwa_next), ':', \
    linewidth=lw, color = colors[1], label='$6$-th order next RWA')
ax1_next_log.set_xlabel('$E_J/E_C$', fontsize=20)
ax1_next_log.set_ylabel('$| \\Delta  \\omega_{01} /\\omega_{01} |$', fontsize=20)
plt.legend(loc='lower right', fontsize=14)
ax1_next_log.tick_params(axis='both', labelsize=t)
fig1_next_log.savefig(path+\
    'omega01_fourth_vs_six_rwa_next_log.pdf', bbox_inches="tight")
plt.show()


#%%
""" Plot anharmonicity 4th vs 6th and RWA order expansion """

fig2, ax2 = plt.subplots(figsize=(6,6))
ax2.plot(ej_vec, d_anh_four, \
    linewidth=lw, color = colors[0], label='$4$-th order')
ax2.plot(ej_vec, d_anh_four_rwa, '--', \
    linewidth=lw, color = colors[0], label='$4$-th order RWA')
ax2.plot(ej_vec, d_anh_six, \
    linewidth=lw, color = colors[1], label='$6$-th order')
ax2.plot(ej_vec, d_anh_six_rwa, '--', \
    linewidth=lw, color = colors[1], label='$6$-th order RWA')
ax2.set_xlabel('$E_J/E_C$', fontsize=20)
ax2.set_ylabel('$\\Delta | \\delta |/|\\delta|$', fontsize=20)
plt.legend(loc='lower right', fontsize=14)
ax2.tick_params(axis='both', labelsize=t)
fig2.savefig(path+\
    'anharmonicity_fourth_vs_six.pdf', bbox_inches="tight")
plt.show()

#%%
""" Plot anharmonicity 4th vs 6th and RWA order expansion """

fig2_log, ax2_log = plt.subplots(figsize=(6,6))
ax2_log.semilogy(ej_vec, np.abs(d_anh_four), \
    linewidth=lw, color = colors[0], label='$4$-th order')
ax2_log.semilogy(ej_vec, np.abs(d_anh_four_rwa), '--', \
    linewidth=lw, color = colors[0], label='$4$-th order RWA')
ax2_log.semilogy(ej_vec, np.abs(d_anh_six), \
    linewidth=lw, color = colors[1], label='$6$-th order')
ax2_log.semilogy(ej_vec, np.abs(d_anh_six_rwa), '--', \
    linewidth=lw, color = colors[1], label='$6$-th order RWA')
ax2_log.set_xlabel('$E_J/E_C$', fontsize=20)
ax2_log.set_ylabel('$|\\Delta | \\delta |/\\delta|$', fontsize=20)
plt.legend(loc='lower right', fontsize=14)
ax2_log.tick_params(axis='both', labelsize=t)
fig2_log.savefig(path+\
    'anharmonicity_fourth_vs_six_log.pdf', bbox_inches="tight")
plt.show()

# %%
""" Plot anharmonicity 4th. 6th order RWA vs next RWA """

fig2_next, ax2_next = plt.subplots(figsize=(6,6))
ax2_next.plot(ej_vec, d_anh_four_rwa, '--', \
    linewidth=lw, color = colors[0], label='$4$-th order RWA')
ax2_next.plot(ej_vec, d_anh_four_rwa_next, ':', \
    linewidth=lw, color = colors[0], label='$4$-th order next RWA')
ax2_next.plot(ej_vec, d_anh_six_rwa, '--', \
    linewidth=lw, color = colors[1], label='$6$-th order RWA')
ax2_next.plot(ej_vec, d_anh_six_rwa_next,':', \
    linewidth=lw, color = colors[1], label='$6$-th order next RWA')
ax2_next.set_xlabel('$E_J/E_C$', fontsize=20)
ax2_next.set_ylabel('$\\Delta | \\delta |/|\\delta|$', fontsize=20)
plt.legend(loc='lower right', fontsize=14)
ax2_next.tick_params(axis='both', labelsize=t)
fig2_next.savefig(path+\
    'anharmonicity_fourth_vs_six_rwa_next.pdf', bbox_inches="tight")
plt.show()

#%%

fig2_next_log, ax2_next_log = plt.subplots(figsize=(6,6))
ax2_next_log.semilogy(ej_vec, np.abs(d_anh_four_rwa), '--', \
    linewidth=lw, color = colors[0], label='$4$-th order RWA')
ax2_next_log.semilogy(ej_vec, np.abs(d_anh_four_rwa_next), ':', \
    linewidth=lw, color = colors[0], label='$4$-th order next RWA')
ax2_next_log.semilogy(ej_vec, np.abs(d_anh_six_rwa), '--', \
    linewidth=lw, color = colors[1], label='$6$-th order RWA')
ax2_next_log.semilogy(ej_vec, np.abs(d_anh_six_rwa_next), ':', \
    linewidth=lw, color = colors[1], label='$6$-th order next RWA')
ax2_next_log.set_xlabel('$E_J/E_C$', fontsize=20)
ax2_next_log.set_ylabel('$|\\Delta | \\delta |/\\delta|$', fontsize=20)
plt.legend(loc='lower right', fontsize=14)
ax2_next_log.tick_params(axis='both', labelsize=t)
fig2_next_log.savefig(path+\
    'anharmonicity_fourth_vs_six_rwa_next_log.pdf', bbox_inches="tight")
plt.show()
