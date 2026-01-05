#intermidiate level
products={1:["Gaming Laptop",55000,"Electronics"],2:["Wireless Earbud",2500,"Electronics"],3:["Running Shoes",4500,"Fashion"],4:["Coffee Maker",1800,"Home Appliance"]}
product1=products.get(1)
product2=products.get(2)
product3=products.get(3)
product4=products.get(4)
user_name = input("Enter your name: ")
print(f"Available Products: \n 1.{product1[0]}-₹{product1[1]}({product1[2]}) \n2.{product2[0]}-₹{product2[1]}({product2[2]}) \n3.{product3[0]}-₹{product3[1]}({product3[2]}) \n4.{product4[0]}-₹{product4[1]}({product4[2]}) ")
user_choice1=int(input("Select Product 1 (1-4) : "))
user_choice2=int(input("Select Product 2 (1-4) : "))
user_choice3=int(input("Select Product 3 (1-4) : "))
product_name=[product1[0],product2[0],product3[0],product4[0]]
product_price=[product1[1],product2[1],product3[1],product4[1]]
product_category=[product1[2],product2[2],product3[2],product4[2]]
name_list=[]
name_list.append(product_name[user_choice1-1])
name_list.append(product_name[user_choice2-1])
name_list.append(product_name[user_choice3-1])
price_list=[]
price_list.append(product_price[user_choice1-1])
price_list.append(product_price[user_choice2-1])
price_list.append(product_price[user_choice3-1])
category_list=[]
category_list.append(product_category[user_choice1-1])
category_list.append(product_category[user_choice2-1])
category_list.append(product_category[user_choice3-1])
product_price_dict={name_list[0]:price_list[0],name_list[1]:price_list[1],name_list[2]:price_list[2]}
category_set=(category_list[0],category_list[1],category_list[2],)
payment=input("Enter payment method (UPI/Card/COD): ")
#Calculating Total Cart Value
value=sum(price_list)
#Apply discount 
if value>=5000:
	discount=20
elif 2000<=value<5000:
	discount=10
else:
	discount=0
final_price=value-((value*discount)/100)
#Apply payment rules
if payment=="Card" and final_price>30000:
	discount+=5
	final_price = final_price-((final_price*5)/100)
#printing output
print("PURCHASE SUMMARY")
print(f"User : {user_name}")
print(f"Products : {name_list}")
print(f"Categories : {category_set}")
print(f"Cart Total : {value}")
print(f"Discount% : {discount}")
print(f"Final Price : {final_price}")
if payment=="COD" and category_set==("Electronics"):
	print(" Status -Order not allowed")
