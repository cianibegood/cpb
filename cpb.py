""" It contains functions and classes for the study of the CPB """

import numpy as np
import math
import scipy.linalg as la
from scipy import constants
import qutip 

class CPB:

    """ The class is initialized with the parameters of the CPB and
    a reference charging energy that has to be given in GHz 
    (units of h). ec and ej must be given in units of ec_ref. """



    def __init__(self, ec, ej, ng, ec_ref):
        self.ec = ec
        self.ej = ej
        self.ng = ng
        self.ec_ref = ec_ref # reference charging energy in GHz (units of h)
        self.c = constants.elementary_charge**2/2*1/ec*\
            1/(constants.h*ec_ref)*10**6 # capactiance matrix [fF]
        self.lj = 1/(4*np.pi**2)*1/ej*1/(constants.h*ec_ref)*\
            (constants.h/(2*constants.elementary_charge))**2 #ind matrix [nH]
        self.omega_p = np.sqrt(8*ec*ej)
        self.phi_zpf = (2*ec/ej)**(1/4)
    
    def h_cpb(self, n_charges):

        """ Hamiltonian of the CPB in charge basis """

        ide = np.identity(2*n_charges + 1)
        n0 = ncp(n_charges)
        jj_t = josephson_tunnel(n_charges)
        cos_jt = 1/2*(jj_t + jj_t.conj().T)
        n_tot = n0 + self.ng*ide
        kin = 4*self.ec*n_tot.dot(n_tot)
        u = self.ej*cos_jt
        h = kin - u
        return h
    
    def eigenenergies(self, n_charges):

        """ Eigenenergies of the CPB in charge basis """

        h = self.h_cpb(n_charges)
        y1 = np.linalg.eigvals(h)
        idx = y1.argsort()[::1]   
        y1 = y1[idx]
        return y1
    
    def h_cpb_approx(n_order, n_fock):

        if np.mod(n_order, 2) != 0:
            raise Exception("The order must be even.")

        ide = qeye(n_fock)
        a = destroy(n_fock)
        h = self.omega_p*(a.dag()*a + ide/2) - self.ej*ide
        phi = self.phi_zpf(a + a.dag())
        n_eff = n_order/2
        for n in range(2, n_eff + 1):
            h += self.ej*(-1)**n/(math.factorial(2*n))*phi**(2*n)
        return h




def ncp(n_charges):

    """ Charge operator in the charge basis """

    nop = np.zeros([2*n_charges + 1, 2*n_charges + 1], \
        dtype=complex)
    for k in range(0, 2*n_charges + 1):
        nop[k, k] = -n_charges + k
    return nop

def josephson_tunnel(n_charges):

    """ Josephson tunneling operator in charge basis """

    tun_op = np.zeros([2*n_charges + 1, 2*n_charges + 1], \
        dtype=complex)
    for k in range(0, 2*n_charges):
        tun_op[k + 1, k] = 1
    return tun_op
    