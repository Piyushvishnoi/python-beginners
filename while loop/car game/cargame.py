order = ""
while order.upper() != "QUIT":
    order = input("-> ")
    if order.upper() == 'START':
     print("Car started  Ready to Go!!")
    elif order.upper() == 'STOP':
     print("Car stopped!!")
    elif order.upper() =='HELP': 
        print(''' 
        Start -> To start the car
        Stop-> To stop the car    
        Quit-> to quit from game   
        ''') 
    else:
     print("command entered is wrong") 
