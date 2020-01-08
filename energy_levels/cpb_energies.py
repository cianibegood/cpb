""" Energy levels of the CPB and the transmon approximation """

#%%

import numpy as np
import math
import scipy.linalg as la
import matplotlib
import matplotlib.pyplot as plt
import sys
import os
sys.path.append('/home/ciani/Work/python/github_repos/cpb')
sys.path.append(os.getcwd())
import cpb
import time
matplotlib.rcParams['mathtext.fontset'] = 'cm'
import multiprocessing 
from functools import partial
import itertools
import qutip
import importlib


#%%
def compute_delta(ec, ng, ec_ref, n_charges, n_fock, ej):
    """ Functions for the parallel loop """
    q = cpb.CPB(ec, ej, ng, ec_ref)
    n_lev = 3
    evals = q.eigenenergies(n_charges)[0:n_lev]
    evals_four = q.h_cpb_approx(4, n_fock).eigenenergies()[0:n_lev]
    evals_four_rwa = q.h_cpb_rwa(4, n_fock).eigenenergies()[0:n_lev]
    evals_four_rwa_next = q.h_cpb_next_rwa(4, n_fock).eigenenergies()[0:n_lev]
    evals_six_rwa_next = q.h_cpb_next_rwa(6, n_fock).eigenenergies()[0:n_lev]
    evals_six = q.h_cpb_approx(6, n_fock).eigenenergies()[0:n_lev]
    evals_six_rwa = q.h_cpb_rwa(6, n_fock).eigenenergies()[0:n_lev]
    evals = evals - evals[0]
    evals_four = evals_four - evals_four[0]
    evals_four_rwa = evals_four_rwa - evals_four_rwa[0]
    evals_four_rwa_next = evals_four_rwa_next - evals_four_rwa_next[0]
    evals_six = evals_six - evals_six[0]
    evals_six_rwa = evals_six_rwa - evals_six_rwa[0]
    evals_six_rwa_next = evals_six_rwa_next - evals_six_rwa_next[0]
    delta = evals[2] - 2*evals[1]
    delta_four = evals_four[2] - 2*evals_four[1]
    delta_four_rwa = evals_four_rwa[2] - 2*evals_four_rwa[1]
    delta_four_rwa_next = evals_four_rwa_next[2] - 2*evals_four_rwa_next[1]
    delta_six = evals_six[2] - 2*evals_six[1]
    delta_six_rwa = evals_six_rwa[2] - 2*evals_six_rwa[1]
    delta_six_rwa_next = evals_six_rwa_next[2] - 2*evals_six_rwa_next[1]
    d_e10_four = (evals_four[1] - evals[1])/evals[1]
    d_e10_four_rwa = (evals_four_rwa[1] - evals[1])/evals[1]
    d_e10_four_rwa_next = (evals_four_rwa_next[1] - evals[1])/evals[1]
    d_e10_six = (evals_six[1] - evals[1])/evals[1]
    d_e10_six_rwa = (evals_six_rwa[1] - evals[1])/evals[1]
    d_e10_six_rwa_next = (evals_six_rwa_next[1] - evals[1])/evals[1]
    d_anh_four = (np.abs(delta_four) - np.abs(delta))/np.abs(delta)
    d_anh_four_rwa = (np.abs(delta_four_rwa) - np.abs(delta))/np.abs(delta)
    d_anh_four_rwa_next = (np.abs(delta_four_rwa_next) - \
        np.abs(delta))/np.abs(delta)
    d_anh_six = (np.abs(delta_six) - np.abs(delta))/np.abs(delta)
    d_anh_six_rwa = (np.abs(delta_six_rwa) - np.abs(delta))/np.abs(delta)
    d_anh_six_rwa_next = (np.abs(delta_six_rwa_next) - \
        np.abs(delta))/np.abs(delta)
    y = np.array([d_e10_four, d_e10_four_rwa, d_e10_four_rwa_next, \
        d_e10_six, d_e10_six_rwa, d_e10_six_rwa_next, \
            d_anh_four, d_anh_four_rwa, d_anh_four_rwa_next, \
                d_anh_six, d_anh_six_rwa,  d_anh_six_rwa_next])
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
n_order = 6


# %%
""" Exact and approximate eigenenergies """

evals = qubit.eigenenergies(n_charges)
evals_approx = qubit.h_cpb_approx(n_order, n_fock).eigenenergies()
evals_rwa = qubit.h_cpb_rwa(n_order, n_fock).eigenenergies()
evals_next_rwa = qubit.h_cpb_next_rwa(n_order, n_fock).eigenenergies()
evals +=- evals[0]
evals_approx += -evals_approx[0]
evals_rwa += -evals_rwa[0]
evals_next_rwa += -evals_next_rwa[0]
delta = evals[2] - 2*evals[1]
delta_approx = evals_approx[2] - 2*evals_approx[1]
delta_rwa = evals_rwa[2] - 2*evals_rwa[1]
delta_next_rwa = evals_next_rwa[2] - 2*evals_next_rwa[1]

# %%
""" Printing results """

print('Exact E01 = ' + str(np.real(evals[1])))
print('Approximate order ' + str(n_order) + 'th E01 = ' + \
    str((evals_approx[1])))
print('Approximate rwa order ' + str(n_order) + 'th E01 = ' + \
    str((evals_rwa[1])))
print('Approximate next rwa order ' + str(n_order) + 'th E01 = ' + \
    str((evals_next_rwa[1])))
print('Exact anharmonicity = ' + str(delta))
print('Approximate order ' + str(n_order) + 'th anharmonicity = ' + \
    str(delta_approx))
print('Approximate rwa order ' + str(n_order) + 'th = ' + \
    str(delta_rwa))
print('Approximate next rwa order ' + str(n_order) + 'th = ' + \
    str(delta_next_rwa))

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

results = np.reshape(results, (n_points, 12)).transpose()

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
plt.show(block=False)

# %%
""" Saving data """
answer = input("Do you want to save?y/N ")
if answer != 'y' and answer != 'N':
    raise Exception('The answer must be either y or N!')
if answer == 'y':
    path = os.getcwd()+'/energy_levels/data_approximation_comparison'
    print(path)
    try:
        os.mkdir(path)
    except OSError:
        print ("Creation of the directory %s \
             failed: the directory might already exist" % path)
    else:
        print ("Successfully created the directory %s " % path)
    name_list = ['d_e10_four', 'd_e10_four_rwa', 'd_e10_four_rwa_next', \
        'd_e10_six', 'd_e10_six_rwa', 'd_e10_six_rwa_next', \
            'd_anh_four', 'd_anh_four_rwa', 'd_anh_four_rwa_next', \
                'd_anh_six', 'd_anh_six_rwa', 'd_anh_six_rwa_next']
    for k in range(0, len(name_list)):
        np.save(path + '/' + name_list[k], results[k, :])
    np.save(path + '/ej_vec', ej_vec)
    param_file=open(path+'/parameters.txt', "w+")
    param_file.write('The data where generated using ' + str(os.path.basename(__file__)) + \
        ' with the \n')
    param_file.write('following parameters. \n')
    param_file.write('Parameters: \n')
    param_file.write('n_fock= %f' % n_fock + '\n')
    param_file.write('n_charges= %f' % n_charges + '\n')
    param_file.write('EJ_min= %f' % ej_min + '\n')
    param_file.write('EJ_max= %f' % ej_max + '\n')
    param_file.write('n_points= %f' % n_points + '\n')

    





# %%
