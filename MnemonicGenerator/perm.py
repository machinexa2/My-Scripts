import os
from itertools import permutations

mnemonic_list = [
        "Electrostatus"[0],
        "State"[0],
        "Lusture"[0],
        "Malleability"[0],
        "Ductility"[0],
        "Heat"[0],
        "Density"[0],
        "Conductivity"[0],
        "PH"[0],
]
perm = permutations(mnemonic_list)
perm_list = list(perm)
for perm_tuple in perm_list:
    print("".join(perm_tuple))
