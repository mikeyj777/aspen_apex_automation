import csv
from sqlalchemy import text

from emnengr.apex.emnphysprop2 import Databank, ApexSession, BinCoeffSet, ChemInfo, ConstValueData, Property

chem_mix = [
    '64-19-7',
    '7732-18-5',
]

mass_comp = [
    0.7,
    0.3
]

def get_chem_id_from_cas(cas_number: str):
    with ApexSession() as session:
        query = text("SELECT ChemID FROM ChemInfo WHERE CASN = :cas_number")
        result = session.execute(query, {"cas_number": cas_number}).fetchone()
    if result is None:
        return None
    return result.ChemID  # or result[0]

chem_mix_by_id = [get_chem_id_from_cas(cas_no) for cas_no in chem_mix]

def get_property_id(property_abbrev):
    with ApexSession() as session:
        property_data = session.query(Property).filter(Property.Abbr.in_([property_abbrev]))
        properties = list(session.query(Property))
        if property_data is None:
            return None
        
        return property_data.TypeID

get_property_id("MW")

with ApexSession() as session:
    # Query BinCoeffSet entries for the specified DatabankIDs
    const_values = session.query(ConstValueData).filter(ConstValueData.ChemID.in_(chem_mix_by_id)).all()

    # Example: Print some identifying info for each binary coefficient set
    for const_value in const_values:
        print(const_value)
        


apple = 1

# databank IDs
# ID: 1000001, Name: ASPEN VLE-IG
# ID: 1000002, Name: ASPEN VLE-HOC
# ID: 1000003, Name: ASPEN VLE-RK

databank_ids = [1000001, 1000002, 1000003] 

with ApexSession() as session:
    # Query BinCoeffSet entries for the specified DatabankIDs
    bin_coeff_sets = session.query(BinCoeffSet).filter(BinCoeffSet.DatabankID.in_(databank_ids)).all()

    # Example: Print some identifying info for each binary coefficient set
    for coeff_set in bin_coeff_sets:
        print(f"ID: {coeff_set.ID}, DatabankID: {coeff_set.DatabankID}, Components: {coeff_set.ChemID_i}, {coeff_set.ChemID_j}")



header_written = False


output = []
for i in range(len(databank_list)):
    try:
        with open('apex_databank.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(f=csvfile, fieldnames=column_names)
            if not header_written:
                writer.writeheader()
            header_written = True
            output.append(databank_list[i])
            writer.writerows(output)
            output = []
    except Exception as e:
        print(f'*******\n\n\nidx: {i}\nrow: {databank_list[i]}\nexception: {e}\n\n\n')


apple = 1