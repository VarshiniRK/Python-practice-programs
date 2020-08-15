cost=float(input("Enter the cost in INR : "))
amount=float(input("Enter the given amount in INR : "))
change=amount - cost
if change==0:
    print("No change needed")
elif change>0:
    num_2000,num_500,num_100,num_50,num_10,num_1,num_25p,num_50p=0,0,0,0,0,0,0,0
    rupees=int(change)
    paise=(change-rupees)*100
    if rupees>2000:
        num_2000=int(rupees/2000)
        rupees=rupees%2000
    if rupees>500:
        num_500=int(rupees/500)
        rupees=rupees%500
    if rupees>100:
        num_100=int(rupees/100)
        rupees=rupees%100
    if rupees>50:
        num_50=int(rupees/50)
        rupees=rupees%50
    if rupees>10:
        num_10=int(rupees/10)
        rupees=rupees%10
    if rupees>1:
        num_1=int(rupees/1)
        rupees=rupees%1
    if paise>50:
        num_50p=int(paise/50)
        paise=paise%50
    if paise>25:
        num_25p=int(paise/25)
        paise=paise%25
    print(f"change to be provided {round(change,2)} \n {num_2000} 2000 rupees, \n {num_500} 500 rupees, \n {num_100} 100 rupees, \n {num_50} 50 rupees,\n {num_10} 10 rupees,\n {num_1} 1 rupees, \n {num_25p} 25 paise, \n {num_50p} 50 paise.")
else:
    print("Amount is less than cost")