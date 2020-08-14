def findtotalcostoftile(wid,hei,cost):
    totalsquarefootage=float((wid*hei)+(wid*hei)*0.10)
    print("selecting 12*12 inch tile which covers 10 square feet")
    totalcost=(totalsquarefootage/10)*float(cost)
    return totalcost
width = input("Enter the width of your floor plan in feet >> ")
height = input("Enter the height of your floor plan in feet >> ")
Costpertile = input("Enter the cost of one tile you are selecting >> ")
if width.isdigit and float(width)>0 and height.isdigit and float(height)>0 and Costpertile.isdigit and float(Costpertile)>0:
    print(findtotalcostoftile(float(width),float(height),float(Costpertile)))
else:
    print("Given input is not in correct format, please try again")

