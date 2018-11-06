import numpy as np

def CustomerAddress(name):
    name.address = "HouseNo, Street, City, State, Zip"
    name.accountno = np.array([1,2345])
    return name.address, name.accountno