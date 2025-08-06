from emnengr.apex.emnphysprop2 import ChemInfo, ApexSession, MixtureChemInfo, MixtureVLEDataType, plot_vle_data

# Create a session and download component 1252.
with ApexSession() as session:
    mixture = MixtureChemInfo.from_chems((1252, 1921), session)
    tpxy_data_sets = mixture.getMixtureData(session, dataType=MixtureVLEDataType.TPxy)
    tpxy_set = tpxy_data_sets[0]
    print(tpxy_set.Ref)