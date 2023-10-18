from home.models import *

P1data = Psub1.objects.filter(Table_Id = 1).values_list('Teacher',flat=True)
for P1data in P1data:
    P1 = (P1data[0:2])
    

P2data = Psub2.objects.filter(Table_Id = 1).values_list('Teacher',flat=True)
for P2data in P2data:
    P2 = (P2data[0:2])