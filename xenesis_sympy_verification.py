"""
XENESIS v4.1 — SymPy Verification
DOI: xenesis.ri/2026/tfi-aks/v4.1
Author: Alberto Martínez Hernández (Vaan Ahetis)
"""
from sympy import *
from fractions import Fraction

eps = Rational(1, 5)

# All Ki* values — exact fractions
manifolds = {
    'Cylinder':  (1, 0),
    'Mobius':    (1, 1),
    'Torus_T2':  (2, 0),
    'Klein_K2':  (2, 1),
    'Klein_SU3': (8, 1),
    'Klein_SU2': (3, 1),
}

print("Ki* values (exact fractions):")
for name, (b1, w1) in manifolds.items():
    chi = (1 + b1) * (1 + eps * w1)
    ki  = 1 - Rational(1, 1) / chi
    print(f"  {name}: Ki* = {ki} = {float(ki):.8f}")

# Uniqueness of epsilon
eps_var = symbols('epsilon', positive=True)
Ki_e = Rational(1, 2)
Ki_q = 1 - 1 / (3 * (1 + eps_var))
solution = solve(Eq(Ki_e / Ki_q, Rational(9, 13)), eps_var)
print(f"\nUniqueness: solve(Ki_e/Ki_q=9/13) → epsilon = {solution}")

# SU(N) formula
N = symbols('N', positive=True, integer=True)
Ki_SUN = simplify(1 - Rational(5) / (6 * N**2))
print(f"\nKi*(SU(N)) = {Ki_SUN}")
