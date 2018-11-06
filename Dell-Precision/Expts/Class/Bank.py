from CustomerAccount import *
from OtherInfo import *

jeff = Customer('Jeff Knupp',1000)
jeff.address, jeff.otherinfo = CustomerAddress(jeff)

#print(CustomerAddress(jeff))

print(jeff.name)
print(jeff.balance)
print(jeff.address)
print(jeff.otherinfo)
