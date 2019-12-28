""" Energy levels of the CPB and the transmon approximation """

#%%

import numpy as np
import math
import scipy.linalg as la
import matplotlib.pyplot as plt
import cpb 
import time
matplotlib.rcParams['mathtext.fontset'] = 'cm'
import multiprocessing 
from functools import partial
import itertools
import qutip
import importlib
import os

#%%
def compute_delta(ec, ng, ec_ref, n_charges, n_fock, ej):
    """ Functions for the parallel loop """
    q = cpb.CPB(ec, ej, ng, ec_ref)
    n_lev = 3
    evals = q.eigenenergies(n_charges)[0:n_lev]
    evals_four = q.h_cpb_approx(4, n_fock).eigenenergies()[0:n_lev]
    evals_four_rwa = q.h_cpb_rwa(4, n_fock).eigenenergies()[0:n_lev]
    evals_six = q.h_cpb_approx(6, n_fock).eigenenergies()[0:n_lev]
    evals_six_rwa = q.h_cpb_rwa(6, n_fock).eigenenergies()[0:n_lev]
    evals = evals - evals[0]
    evals_four = evals_four - evals_four[0]
    evals_four_rwa = evals_four_rwa - evals_four_rwa[0]
    evals_six = evals_six - evals_six[0]
    evals_six_rwa = evals_six_rwa - evals_six_rwa[0]
    delta = evals[2] - 2*evals[1]
    delta_four = evals_four[2] - 2*evals_four[1]
    delta_four_rwa = evals_four_rwa[2] - 2*evals_four_rwa[1]
    delta_six = evals_six[2] - 2*evals_six[1]
    delta_six_rwa = evals_six_rwa[2] - 2*evals_six_rwa[1]
    d_e10_four = np.abs((evals_four[1] - evals[1])/evals[1])
    d_e10_four_rwa = np.abs((evals_four_rwa[1] - evals[1])/evals[1])
    d_e10_six = np.abs((evals_six[1] - evals[1])/evals[1])
    d_e10_six_rwa = np.abs((evals_six_rwa[1] - evals[1])/evals[1])
    d_anh_four = np.abs((delta_four - delta)/delta)
    d_anh_four_rwa = np.abs((delta_four_rwa - delta)/delta)
    d_anh_six = np.abs((delta_six - delta)/delta)
    d_anh_six_rwa = np.abs((delta_six_rwa - delta)/delta)
    y = np.array([d_e10_four, d_e10_four_rwa, d_e10_six, d_e10_six_rwa, \
        d_anh_four, d_anh_four_rwa, d_anh_six, d_anh_six_rwa])
    return y

#%%
""" Data """

ec_ref = 0.25 # [GHz]
ec = 1 
ej = 50
ng = 0 
qubit = cpb.CPB(ec, ej, ng, ec_ref)
n_charges = 20
n_fock = 10
n_order = 4


# %%
""" Exact and approximate eigenenergies """

evals = qubit.eigenenergies(n_charges)
evals_approx = qubit.h_cpb_approx(n_order, n_fock).eigenenergies()
evals_rwa = qubit.h_cpb_rwa(n_order, n_fock).eigenenergies()



# %%
""" Printing results """

print('Exact = ' + str(np.real(evals[0:6] - evals[0])*ec_ref))
print('Approximate order ' + str(n_order) + 'th = ' + \
    str((evals_approx[0:6] - evals_approx[0])*ec_ref))
print('Approximate rwa order ' + str(n_order) + 'th = ' + \
    str((evals_rwa[0:6] - evals_rwa[0])*ec_ref))


# %%
""" We now want to critically compare the 4th order and 6th order
approximations """

ej_min = 50
ej_max = 100
n_points = 100
ej_vec = np.linspace(ej_min, ej_max, n_points)
n_process = 2
results = np.zeros([4, n_points])





#%%
""" Parallel loop """

p = multiprocessing.Pool(n_process)

start = time.time()

func = partial(compute_delta, ec, ng, ec_ref, n_charges, n_fock)

results = p.map(func, ej_vec)

p.close()
p.join()

results = np.reshape(results, (n_points, 8)).transpose()

end = time.time()

print(f'Computation time parallel with {n_process} processes = {end - start}')


# %%
""" Plots """
lab = ["$|\Delta \omega_{10}^{4th}/\omega_{10}|$", \
    "$|\Delta \omega_{10}^{6th}/\omega_{10}|$", \
        "$|\Delta \delta^{4th}/\delta|$", \
            "$|\Delta \delta^{6th}/\delta|$"]
colors = ['red', 'darkorange', 'darkslateblue', 'cyan']
fig, ax = plt.subplots(figsize=(6,6))
for k in range(0, 4):
    ax.semilogy(ej_vec, results[k, :], linewidth=2.0, color=colors[k], label=lab[k])
ax.set_xlabel('$E_J/E_C$', fontsize=20)
plt.legend(loc='best', fontsize=16)
plt.show()

# %%
""" Saving data """

