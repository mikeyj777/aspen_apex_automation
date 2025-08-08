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

molar_comp = mole_fracts_from_mass_fracts(mass_fracts=mass_comp, mws=mws)

databank_name_list = ['ASPEN VLE-IG', 'ASPEN VLE-HOC', 'ASPEN VLE-RK']

banks = get_databanks(databank_name_list=databank_name_list, description_contains="WILSON")

coeff_sets_info = get_coeff_sets_info(chem_ids=chem_mix_by_id, databanks=banks)

coeff_sets = get_coeff_sets(coeff_sets_info)

apple = 1