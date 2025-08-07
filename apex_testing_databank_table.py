from property_abbrev import PropertyAbbrev

from emnengr_utils import *
from helpers import *

chem_mix = [
    '64-19-7',
    '7732-18-5',
]

mass_comp = [
    0.7,
    0.3
]

chem_mix_by_id = [get_chem_id_from_cas(cas_no) for cas_no in chem_mix]

mws = get_mws(chem_mix_by_id)

molar_comp = mol

databank_name_list = ['ASPEN VLE-IG', 'ASPEN VLE-HOC', 'ASPEN VLE-RK']

banks = get_databanks(databank_name_list=databank_name_list, description_contains="WILSON")



apple = 1

# databank IDs


with ApexSession() as session:
    # Query BinCoeffSet entries for the specified DatabankIDs
    bin_coeff_sets = session.query(BinCoeffSet).filter(BinCoeffSet.DatabankID.in_(databank_ids)).all()

    # Example: Print some identifying info for each binary coefficient set
    for coeff_set in bin_coeff_sets:
        print(f"ID: {coeff_set.ID}, DatabankID: {coeff_set.DatabankID}, Components: {coeff_set.ChemID_i}, {coeff_set.ChemID_j}")



header_written = False

apple = 1