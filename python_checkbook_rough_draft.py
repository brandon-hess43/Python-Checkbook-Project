import os

def view_balance(user_input):
    if os.path.exists('balance.txt'):
        with open('balance.txt') as f:
            data = f.read()
        print(f'Your balance is:{data}')
    else:
        with open('balance.txt','w') as f:
            f.write('$1.00')
        print(f'Your balance is: {data}')
        
def record_debit(user_input):
    with open('balance.txt') as f:
        data = f.read()
    clean_balance = data.strip('$').replace(',','')
    clean_balance = float(clean_balance)
    print(f'Current Balance: ${clean_balance}')
    withdraw = input(f'How much would you like to withdraw? $')
    new_balance = clean_balance - float(withdraw)
    with open('balance.txt','w') as f:
        f.write(f'${new_balance}')
    with open('balance.txt') as f:
        data = f.read()
    print(f'New Balance:{data}')

    
def record_credit(user_input):
    with open('balance.txt') as f:
        data = f.read()
    clean_balance = data.strip('$').replace(',','')
    clean_balance = float(clean_balance)
    print(f'Current Balance: ${clean_balance}')
    deposit = input(f'How much would you like to deposit? $')
    new_balance = clean_balance + float(deposit)
    with open('balance.txt','w') as f:
        f.write(f'${new_balance}')
    with open('balance.txt') as f:
        data = f.read()
    print(f'New Balance:{data}')
      
        
        
cont = 'yes'
while cont == 'yes':
    
    
    
    print("\n~~~ Welcome to your terminal checkbook! ~~~")
    print("What would you like to do?\n")
    print("1) view current balance")
    print("2) record a debit (withdraw)")
    print("3) record a credit (deposit)")
    print("4) exit")
    
    user_input = input('Your Choice? ')

    if user_input == '1':
        view_balance(user_input)
    elif user_input == '2':
        record_debit(user_input)
    elif user_input == '3':
        record_credit(user_input)
    elif user_input == '4':
        print("Thanks, have a great day!")
        break
    else:
        Print('Invalid input')
        continue
    cont = input('Would you like to continue (yes/no)?')