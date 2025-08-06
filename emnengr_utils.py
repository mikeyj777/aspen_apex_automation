from property_abbrev import PropertyAbbrev

from sqlalchemy import text
from emnengr.apex.emnphysprop2 import Databank, ApexSession, BinCoeffSet, ChemInfo, ConstValueData, Property


def get_chem_id_from_cas(cas_number: str):
    with ApexSession() as session:
        query = text("SELECT ChemID FROM ChemInfo WHERE CASN = :cas_number")
        result = session.execute(query, {"cas_number": cas_number}).fetchone()
    if result is None:
        return None
    return result.ChemID  # or result[0]

def get_property_id(property_abbrev):
    with ApexSession() as session:
        property_data = session.query(Property).filter(Property.Abbr == property_abbrev).all()
        if property_data is None:
            return None
        if not isinstance(property_data, list):
            return None
        if len(property_data) != 1:
            return None
        prop = property_data[0]
        ans = None
        try:
            ans = prop.TypeID
        except Exception as e:
            print(f'could not get property id for {property_abbrev}.  error: {e}')
        return ans

def get_constant_values(chem_id_list, prop_id):
    with ApexSession() as session:
        const_values = (
            session.query(ConstValueData)
            .filter(
                ConstValueData.ChemID.in_(chem_id_list),
                ConstValueData.PropertyID == prop_id
            )
            .all()
        )
        if const_values is None:
            return None
        if not isinstance(const_values, list):
            return None
        if len(const_values) != len(chem_id_list):
            return None
        ans_out = []
        for const, chem_id in zip(const_values, chem_id_list):
            if const.ChemID == chem_id:
                ans_out.append(const.Value)
        return ans_out
        
def get_mws(chem_id_list):
    mw_id = get_property_id(property_abbrev=PropertyAbbrev.MW)
    if mw_id is None:
        return None
    mws = get_constant_values(chem_id_list, mw_id)
    return mws

def get_databanks(databank_name_list = None, description_contains = None):
    with ApexSession() as session:
        # Query all rows from the Databank table
        if databank_name_list is None:
            return session.query(Databank).all()
        if description_contains is None:
            return session.query(Databank).filter(Databank.Name.in_(databank_name_list)).all()
        return session.query(Databank).filter(
            Databank.Name.in_(databank_name_list),
            Databank.Description.contains(description_contains)
        ).all()