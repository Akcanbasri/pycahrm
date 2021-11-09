print("For Mouse hit '1'\nFor Keyboard hit '2'\nFor Headphone hit '3'\nFor pencil hit '4'\n")

products = {"Mouse": "10$", "Keyboard": "10$", "Headphone": "20$", "Pencil": "5$\n"}

print(products)

Mouse = 10
Keyboard = 10
Headphone = 20
Pencil = 5

try:
      users_product = int(input("Please enter which product you want to buy"))
      client_email = input("Please enter your email: ")
      client_phone = input("Please enter your phone: ")


      if users_product == 1:
            price = 10 + 10 * 0.23
            print("Your basket:")
            print("Mouse/ "+ "Net price: {}/ ".format(price) + "Gross price: {}/ ".format(Mouse) + "Your email: {}/ ".format(client_email) + "Your Phone: {}".format(client_phone))
      elif users_product == 2:
            price = 10 + 10 * 0.23
            print("Your basket:")
            print("Keyboard/ "+ "Net price: {}/ ".format(price) + "Gross price: {}/ ".format(Keyboard) + "Your email: {}/ ".format(client_email) + "Your Phone: {} ".format(client_phone))
      elif users_product == 3:
            price = 20 + 20 * 0.23
            print("Your basket:")
            print("Headphone/ "+ "Net price: {}/ ".format(price) + "Gross price: {}/ ".format(Headphone) + "Your email: {}/ ".format(client_email) + "Your Phone: {} ".format(client_phone))
      elif users_product == 4:
            price = 5 + 5 * 0.23
            print("Your basket:")
            print("pencil "+ "Net price: {} ".format(price) + "Gross price: {} ".format(Pencil) + "Your email: {} ".format(client_email) + "Your Phone: {} ".format(client_phone))
      else:
            print("You Entered wrong operation...\nYou need to start order again.")
            raise Exception()
except:
      print("Process interrupted. Bad data type. ")