from collections import defaultdict
from time import time
user=defaultdict(list)
order=defaultdict(list)
n=4
rest={'A':[['drinks',40],['starter',70],['main course',120]],
        'B' : [['drinks',40],['south indian',50],['thali',220]],
        'C' : [['tea',10],['chainese',85]]
        }
capacity={'A':0,'B':0,'C':0}
class User:
    def __init__(self,name,number):
        self.name =name
        self.number=number
        user[name]=number
        
    def print_(self):
        t=0
        for i in user.keys():
            if i==self.name and user[i]!='None':
                t=1
                print(f"Name : {i}\nContact : {user[i]}\nPrevious orders are : ")
                for j in order[i]:
                    print(f'Restaurant : {j[0] } , Item : {j[1]}')
        if t==0:
            print("User deleted this account previously")
        print('-----------------')
    def update(self):
        ty=self.name
        if user[ty]=='None':
            print("User deleted this account previously")
        else :
            user[ty]=input("Enter new contact number : ")
            print('Contact is updated')
    def delete(self):
        ty=self.name
        user[ty]='None'
    def Order(self):
        while True : 
            c=1
            print("List of restaurant : ")
            for i in rest.keys():
                print(f"{c}.{i}",end='\t')
                c+=1
            while True :
                rname=input("\nSearch by name of restaurant : ")
                if capacity[rname]<n:
                    break
                print(f"Capacity of {rname} is full please try another restaurant ")
            capacity[rname]+=1
            print("=================\nWelcome select the order from menu")

            for i in rest[rname]:
                print(f'{i[0]} : {i[1]}/-')

            choice = input('Enter your choice : ')
            order_time=int(time())
            order[self.name].append((rname,choice,order_time))
            print(f'----------------\nThank you {self.name},Your order of {choice} have been placed\n------------------')
            if (input("Press any key to continue and 0 to exit : "))=="0":
                break
    def track(self):
        curr=time()
        print('Status of food : ')
        for i in reversed(order[self.name]):
            if (curr-i[2])<20:
                print(f'restaurant : {i[0]}, item : {i[1]}, status : Food is Preparing')
            elif (curr-i[2])<30:
                print(f'restaurant : {i[0]}, item : {i[1]}, status : Out for Delivery')
            else:
                print(f'restaurant : {i[0]}, item : {i[1]}, status : Delivered')
                    



        
class Rest:
    def __init__(self):
        pass
    def add(self):
        ty=input('Enter the name of Resturant in which you want to add item : ')
        item=input('Enter the name of item : ')
        price = input("Enter the price of item : ")
        rest[ty].append([item,price])
    def update(self):
        ty=input('Enter the name of Resturant in which you want to add item : ')
        name = input("Enter the name of item : ")
        price = input("Enter the new price of item : ")
        try:
            for i in range(len(rest[ty])):
                if rest[ty][i][0]==name:
                    rest[ty][i][1]=price
                    break
        except:
            print("This restaurant is not added")


while True:

    in_= int (input("Enter which type of operation you want to perform\n0.Exit\n1.User\n2.Resturant\n-> "))
    if in_==0:
        break
    elif in_==1:
        name= input('Please enter your name : ')
        number= input('Please enter your number : ') 
        print('=================')
        u=User(name , number)
        
        while True:
            ty=int(input("0.Exit\n1.See user details\n2.Update exist record\n3.Delete record\n4.Order food\n5.Track your order\n6.Switch User\n-> "))
            if ty==0:
                print("Thank you for using our servies hope you enjoyed")
                break
            elif ty==1:
                u.print_()
            elif ty==2:
                u.update()
            elif ty==3:
                u.delete()
            elif ty==4:
                u.Order()
            elif ty==5:
                u.track()
            elif ty==6:
                name= input('Please enter your name : ')
                number= input('Please enter your number : ') 
                print('=================')
                u=User(name , number)
            else:
                print("Invalid input please try again")
    elif in_==2:
        r=Rest()
        while True:
            ty=int(input("Enter the operation\n0.Exit\n1.Add food item\n2.Update\n-> "))
            if ty==0:
                print("Thank you for using our servies hope you enjoyed")
                break
            elif ty==1:
                r.add()
            elif ty==2:
                r.update()
            else :
                print("Invalid input please try again")


