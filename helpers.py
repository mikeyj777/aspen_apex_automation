import numpy as np

def mole_fracts_from_mass_fracts(mass_fracts, mws):
    mol_fracts = None
    if not isinstance(mws, list) and not isinstance(mws, np.ndarray):
        return
    if not isinstance(mass_fracts, list) and not isinstance(mass_fracts, np.ndarray):
        return
    if len(mass_fracts) != len(mws):
        return
    if len(mass_fracts) == 0:
        return
    if sum(mws) == 0:
        return
    mass_np = np.array(mass_fracts)
    mw_np = np.array(mws)
    try:
        mol_fracts = mass_np / mw_np
        mol_fracts /= mol_fracts.sum()
    except Exception as e:
        print(f'could not calculate mol fractions.  error: {e}')
    return mol_fracts.tolist()

def mass_fracts_from_mole_fracts(mole_fracts, mws):
    mass_fracts = None
    if not isinstance(mws, list) and not isinstance(mws, np.ndarray):
        return
    if not isinstance(mole_fracts, list) and not isinstance(mole_fracts, np.ndarray):
        return
    if len(mole_fracts) != len(mws):
        return
    if len(mole_fracts) == 0:
        return
    if sum(mws) == 0:
        return
    mole_np = np.array(mole_fracts)
    mw_np = np.array(mws)
    try:
        mass_fracts = mole_np * mw_np
        mass_fracts /= mass_fracts.sum()
    except Exception as e:
        print(f'Could not calculate mass fractions.  Error: {e}')
    return mass_fracts.tolist()

if __name__ == '__main__':
    print(mole_fracts_from_mass_fracts([0.23724519090467566, 0.7627548090953243], [18.01528, 28.96]))
    print(mass_fracts_from_mole_fracts([0.4456031768306043,  0.5543968231693956], [18.01528, 28.96]))