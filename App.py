import random
import Classes 
Product=Classes.Product
def ensure():
 global yesorno
 yesorno=input(str("Are you sure.(y/n)\n"))
 while yesorno!='y' and yesorno!='n':
  print("Incorrect Input. Please Enter 'y' or 'n' ")
  yesorno=input("Are you sure\n")
def sure(function):
 function()
 ensure()   
 while yesorno=='n':
  function()
  ensure()
def sure2(product):
 addition=input(product)
 ensure()   
 while yesorno=='n':
  addition=input(product)
  ensure()
 return addition
def choice():
   global procode
   global proName
   global proManu
   global prosalePrice
   global Stoklev
   global MonUnit
   #,sure2(("Enter the product name: ")),(sure2(("Enter product sale price: "))),(sure2(("""Enter product manufacture cost: """))), (sure2(("Enter Stock level: "))), (sure2(("Enter estimated monthly units: "))))
   procode=(sure2(("Enter the product code: ")))
   while type(procode)==str:
    while procode.isdigit()==True: 
       procode=int(procode)
       if procode<100 or procode>1000:
        print("The product number you Have inputted is not a whole number between 100-1000\nPlease Try Again")
        procode=(sure2(("Enter the product code: ")))
       else:   
         break    
    if type(procode)==str:
     while procode.isdigit()!=True:
      print("The product number you Have inputted is not a whole number between 100-1000\nPlease Try Again")
      procode=(sure2(("Enter the product code: ")))
      while procode.isdigit()==True:
       procode=float(procode)
       if procode<100 or procode>1000:
        print("The product number you Have inputted is not a whole number between 100-1000\nPlease Try Again")
        procode=(sure2(("Enter the product code: ")))
       else:
         break
      break
    else:
      break
   proName=(sure2(("Enter the product name: ")))
   while proName=='':
    print("Please enter a name for your product")
    proName=(sure2(("Enter the product name: ")))
   prosalePrice=(sure2(("Enter product sale price: ")))
   while type(prosalePrice)==str:
    while prosalePrice.isdigit()==True or prosalePrice.isdecimal()==False:
      prosalePrice=float(prosalePrice) 
      if prosalePrice<0:
       print("Incorrect Product Sale Price. Please input a number greater than zero ")
       prosalePrice=(sure2(("Enter product sale price: ")))
      else:
         break
    if type(prosalePrice)==str:
     while prosalePrice.isdigit()!=True or prosalePrice.isdecimal()!=False:
      print("Incorrect Product Sale Price. Please input a number greater than zero ")
      prosalePrice=(sure2(("Enter product sale price: ")))
   proManu=(sure2(("""Enter product manufacture cost: """)))
   while type(proManu)==str:
    while proManu.isdigit()==True or proManu.isdecimal()==False:
      proManu=float(proManu) 
      if proManu<=0:
       print("Incorrect Product Manufacuture Cost. Please input a number greater than zero ")
       proManu=(sure2(("Enter Product Manufacuture Cost: ")))
      else:
         break
    if type(proManu)==str:
     while proManu.isdigit()!=True or proManu.isdecimal()!=False:
      print("Incorrect Product Manufacuture Cost. Please input a number greater than zero ")
      proManu=(sure2(("Enter Product Manufacuture Cost: ")))
   Stoklev=(sure2(("Enter Stock level: ")))
   while type(Stoklev)==str:
    while Stoklev.isdigit()==True:
      Stoklev=int(Stoklev) 
      if Stoklev<0:
       print("Incorrect Stock Level. Please input a number greater than or equal to zero ")
       Stoklev=(sure2(("Enter product Stock Level: ")))
      else:
         break
    if type(Stoklev)==str:
     while Stoklev.isdigit()!=True :
      print("Incorrect Stock Level. Please input a number greater than or equal to zero ")
      Stoklev=(sure2(("Enter Stock Level: ")))
   MonUnit=(sure2(("Enter estimated monthly units: ")))
   while type(MonUnit)==str:
    while MonUnit.isdigit()==True :
      MonUnit=int(MonUnit) 
      if MonUnit<=0:
       print("Incorrect Monthly Units. Please input a number greater than or equal to zero ")
       MonUnit=(sure2(("Enter Monthly Units: ")))
      else:
         break
    if type(MonUnit)==str:
     while MonUnit.isdigit()!=True :
      print("Incorrect Monthly Units. Please input a number greater than or equal to zero ")
      MonUnit=(sure2(("Enter Monthly Units: ")))
print("--------------------------------------------------------------------\nProduct Sales Predictor\n--------------------------------------------------------------------\n")
choice()
item=Product(procode,proName,prosalePrice,proManu,Stoklev,MonUnit)
print("Product Code:",item.procode,"\nProduct Name:",item.proName,"\nSale Price:",item.proSalePrice,"\nManufacture Cost:",item.proManu,"\nMonthly Production:",item.MonUnit)
Manu=item.MonUnit
soldTotal=0
for i in range(1,13):
   print("--------------------------------------------------------------------\nMonth",i,":")
   y=random.randint(-10,10)
   item.Stoklev-=y
   print("  Manufactured:",Manu,"\n  Units Sold:",Manu+y,"\n  Stock:",item.Stoklev)
   soldTotal+=Manu+y
print("--------------------------------------------------------------------\nThe total units sold over 12 months is",soldTotal,"\nThe total units made over the 12 months are",12*item.MonUnit)
print("Net Profit:",round(soldTotal*item.proSalePrice-12*item.MonUnit*item.proManu))
   

  


