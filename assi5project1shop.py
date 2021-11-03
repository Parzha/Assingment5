def add(list):
    global total
    global basket
    global basket_id

    while(True):
        x,y=input("Please enter the product id and quantity").split()
        x_int = int(x); y_int = int(y)
        index = x_int - 1


        available_product = list[index][2]

        con_int=int(available_product)

        if con_int < y_int:
            print("Not enough of this product avaialbe try again current amount=",con_int)
        else:
           CustomerList = []
           total+= int(list[index][1]) * y_int
           CustomerList.append(list[index][0])
           CustomerList.append(y)
           update_add(list,y_int,index)
           basket.append(CustomerList)
           basket_id.append(index)
           break

def update_add(list,count,index):
    product_update = int(list[index][2])-count
    list[index][2]=str(product_update)




def remove(list,user_basket,basket_id):

    if user_basket == []:
        print("Your current basket is empty")
    else:
        user_choice = int(input("please enter the id of the product you want to remove"))
        index1 = user_choice-1
        user_basket_quantity = int(user_basket[index1][1])
        user_basket.pop(index1)
        update_remove(list,user_basket_quantity,basket_id,index1)
        basket_id.pop(index1)

def update_remove(list,user_basket_quantity,basket_id,index):
    global total
    index_list = basket_id[index]
    result=int(list[index_list][2])+user_basket_quantity
    list[index_list][2]=str(result)
    total = total - (int(list[index_list][1])*user_basket_quantity)









def showlist(list):
    print("<ID> <NAME> <PRICE> <QUANTITY>")
    i=1
    for item in list:
        print(i,end=' ')
        for j in item:
            print(j,end=' ')
        i += 1
        print("\n")


def currentList_totalPrice(basket , total_price):
    str_basket= ""
    print("<ID> <NAME> <QUANTITY>")
    i=1
    for item in basket:
         print(i," ",end="")
         str_basket=' '.join(item)
         print(str_basket,end=' ')
         print("\n")
         i+=1
    print("total price is =",total_price)




def file_editor(list):
    password=input("ENTER PASSWORD").lower()
    f = open("myText.txt",'a')

    if password == "admin":
        while(True):
            manager_choice = int(input("For removing enter 1/for adding enter 2/for editing enter 3"))
            if manager_choice == 1:
                remove_item = int(input("Which item from the list you wanna remove"))
                list.pop(remove_item-1)

                break
            elif manager_choice ==2 :
                newProduct=[]
                x,y,z = input("enter the name/price/quantity").split(" ")
                newProduct.append(x);newProduct.append(y);newProduct.append(z)
                list.append(newProduct)
                str_holder1 = ''.join(newProduct)
                f.write(str_holder1)
                break
            elif manager_choice == 3:
                edit_input = int(input("Which product from the list you want to edit(ID) "))
                index = edit_input-1
                x,y,z = input("Please enter the new name/price/quantity").split(" ")
                list[index][0]=x ;  list[index][1]=y ;  list[index][2]=z
                break
            else:
                print("Try again input not valid")

    else:
        print("PASSWORD INCORRECT")

    f.close()

def searchByname(list,name):

    for item in list:
      if name in item:
          return list.index(item)
      else:
          print("Product doesn't exist")










basket = []
basket_id =[]
total = 0
def mainShop():
    global basket
    f = open('myText','r')
    my_list = []
    my_list = f.read().split("\n")
    my_list2 = [item.split(' ') for item in my_list]

    print("""Welcome to our shop  Please choose option to continue
          1- Show List of prducts
          2- add item to basket
          3- your current basket and total price
          4- remove item from basket 
          5- edit product database (MANAGER ONLY NEED PASSWORD)
          6- search by the name 
          7- exit""")
    print("Enter your choice =",end='')

    while(True):
        user_choice = int(input())
        if user_choice == 1:
            showlist(my_list2)
            print("task complete... enter your next choice from the list above")
        elif user_choice == 2:
            add(my_list2)
            print("task complete... enter your next choice from the list above")

        elif user_choice == 3:
            currentList_totalPrice(basket, total)
            print("task complete... enter your next choice from the list above")

        elif user_choice == 4:
            remove(my_list2,basket, basket_id)
            print("task complete... enter your next choice from the list above")

        elif user_choice == 5:
            file_editor(my_list2)
            print("task complete... enter your next choice from the list above")

        elif user_choice == 6:
            name = input("please enter the name of the product").lower()
            name_id=searchByname(my_list2,name)
            print("The product id is",name_id+1,"\n")
            print("task complete... enter your next choice from the list above")


        elif user_choice == 7:
            print("Thank for buying from out shop and goodbye")
            break
        else:
            print("Try again invalid input")

    f.close()



if __name__ == '__main__':
    mainShop()







