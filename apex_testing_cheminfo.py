import csv
from sqlalchemy import text

from emnengr.apex.emnphysprop2 import ChemInfo, ApexSession

# ans = {}
# for i in range()
# with ApexSession() as session:
#     component = ChemInfo.from_id(1252, session)
#     vp_coeff = component.getTDepCoeffSets(['VP'], session)

# print(component)

# apple = 1


column_names = ChemInfo.__table__.columns.keys()

with ApexSession() as session:
    result = session.execute(text("SELECT * FROM ChemInfo"))
    chem_info_list = [dict(row._mapping) for row in result]

header_written = False

output = []
for i in range(len(chem_info_list)):
    try:
        with open('apex_cheminfo.csv', 'a', newline='') as csvfile:
            writer = csv.DictWriter(f=csvfile, fieldnames=column_names)
            if not header_written:
                writer.writeheader()
            header_written = True
            output.append(chem_info_list[i])
            writer.writerows(output)
            output = []
    except Exception as e:
        print(f'*******\n\n\nidx: {i}\nrow: {chem_info_list[i]}\nexception: {e}\n\n\n')


apple = 1
