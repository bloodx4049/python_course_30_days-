p1 = "Make a Lot of Money" 
p2 = "buy now"
p3 = "Limited time offer!!!"    
p4 = "Click this link"
p5 = "subscribe this channel"

massages = input("Enter your massage: ")

if (p1 in massages) or (p2 in massages) or (p3 in massages) or (p4 in massages) or (p5 in massages):
    print("This is a spam massage")
else:
    print("This is not a spam massage")

