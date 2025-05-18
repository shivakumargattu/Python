produts=("Mobile","Laptop","Ear Buds")
print(produts)

def mobile_Price():
    print("Mbole Rice 15000")

def product_prices(mobile_Price,selactItem):
    if selactItem =="Mobile":
        print("Mobile 140000")
    else:
        print("Not matched products")
        
    

def selactItem():
    user_Input=input("Please Enter the Product: ")
    product_prices(selactItem, mobile_Price)
    
selactItem()

    
    