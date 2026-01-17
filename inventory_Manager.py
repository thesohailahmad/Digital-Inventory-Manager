inventory = [ "Tomatto", "broccli" , "potato", "apple" , "banana"]
quantity = [5 , 7 , 15 , 10 , 20]
while True:
      print("\n----The Digital Inventory----")       
      print("1.Show items")
      print(" 2. Add Items ")
      print(" 3.Remove ")
      print(" 4.Exit ")
      choice = int(input("Enter your Number :"))
      if choice==1:
          for i in range(len(inventory)):
              print({inventory[i]} , {quantity[i]})
      elif choice==2:
          inv = input("Enter the name of thing :")
          qty = int(input("Enter the quantity: "))
          inventory.append(inv)
          quantity.append(qty )
          print("Your item added Succesfully")
      elif choice==3:
          name = input("Enter the name which you want to remove :")
          if name in inventory:
            index=inventory.index(name)
            inventory.pop(index)
            quantity.pop(index)
            print("Your Item is Removed")
          else:
            print("Item do not found")     
      elif choice==4:
          print("You Exit Succesfully")
          break
      else:
          print("Invalid Choice")