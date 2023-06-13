import pickle
from cell_phone import CellPhone
import os

phone = CellPhone('Armer', 'Sony', '199.99')

# with open(os.path.join(os.getcwd(), 'cellphones.dat'), 'wb') as file:
#     pickle.dump(phone, file)


with open(os.path.join(os.getcwd(), 'cellphones.dat'), 'rb') as file:
    pickle_phone = pickle.load(file)
    print(pickle_phone.get_manufact())
    print(pickle_phone.get_model())
    print(pickle_phone.get_retail_price())
