#Find the cost and wallet amount
#then find the change
#Grady Rowedder
#CS 1030
#2/7/2022
run1=1
run2=1
runall=1
change=0
while runall==1:
    while run1==1:
        cost =input("How much does the item cost? ")
        try:
            cost=float(cost)
        except ValueError:
            print("Not a number, try again")
            continue
        if cost <= 0:
            print("You cant buy something that doesn't cost anything, try again")
            continue
        run1=0
        
    while run2==1:
        wallet=input("How much is in your wallet? ")
        try:
            wallet=float(wallet)
        except ValueError:
            print("Not a number, try again")
            continue
        
        if round (cost,2)!=cost:
            iscostrounded=1
        else:
            iscostrounded=0
        if round (wallet,2)!=wallet:
            iswalletrounded=1
        else:
            iswalletrounded=0
        cost=round(cost,2)
        wallet=round(wallet,2)
        if cost>wallet:
            print("Not enough money in wallet, try again")
            continue
        print()

        change=wallet-cost
        dollars=change//1
        quarters=(change-dollars)//.25
        dimes=(change-dollars-(quarters*.25))//.10
        nickels=(change-dollars-(quarters*.25)-(dimes*.1))//.05
        pennies=(change-dollars-(quarters*.25)-(dimes*.1)-(nickels*.05))//.01
        if iscostrounded==0 and iswalletrounded==0:
            print("Your change from your purchase is:", round(change,2))
        elif iscostrounded==1 and iswalletrounded==0:
            print("The cost was rounded and your change is:", round(change,2))
        elif iscostrounded==1 and iswalletrounded==1:
            print("The cost was rounded along with the wallet amount to give the change of:", round(change,2))
        elif iscostrounded==0 and iswalletrounded==1:
            print("Your wallet amount was rounded, and your change is:", round(change,2))
            
        print(int(dollars), "dollars,", int(quarters), "quarters,", int(dimes),
              "dimes," ,int(nickels), "nickels,",int(pennies), "pennies")
        print()
        run2=0
    again=input("Want to run it again? Y/N ")
    if again =='y' or again=='Y' or again=='Yes' or again== 'yes':
        print()
        run1=1
        run2=1
        continue
    else:
        runall=0

