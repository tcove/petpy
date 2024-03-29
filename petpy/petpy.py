"""
Petrophysics equations
"""

def gardner(vp, alpha=310, beta=0.25):
    """
    Compute bulk density (in kg/m^3) from vp (in m/s).
    """
    return alpha * vp ** beta

def impedance(vp, rho):
    """
    Compute acoustic impedance.
    """
    return vp * rho

def shear_impedance(vs, rho):
    """
    Compute shear impedance.
    """
    return vs * rho
