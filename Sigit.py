# Global Variables:
PassCode = '1234'
Balance = 50000
TriesLeft = 3

# Exrecise 1:
def ATM_Interface():
    # The ATM Interface:
    global Balance, PassCode, TriesLeft
    TriesLeft = 3
    flag = input('Enter 1 for check balance, 2 for withdrawal, 3 to change the pass code or 4 to exit: ')
    if flag == '1':
        print('Your balance: ' + str(Balance))
    elif flag == '2':
        amount = input('Enter amount of cash to withdrawal in multiplications of 20 or / and 50: ')
        if amount.isdigit():
            if int(amount) % 20 == 0 or int(amount) % 50 == 0:
                if (Balance - int(amount)) >= 0:
                    print('You'
                          ' have withdrawal ' + amount + ' shekels! ')
                    Balance -= int(amount)
                else:
                    print('There is not enough money!')
            else:
                print('The number is not in multiplications of 20 or / and 50! ')

        else:
            print('Invalid amount')
    elif flag == '3':
        pass1 = input('Enter new password ')
        PassCode = pass1
        print("You have changed your password! ")

    elif flag == '4':
        exit(0)

    else:
        print('Invalid input! ')

    return


# Exrecise 2 A :
# List input interface
def CalcSum():
    ls = []
    num1 = input("Enter num : ")
    while num1 != 'stop':
        if num1.isdigit():
            ls.append(int(num1))
        else:
            print("Invalid num")
        num1 = input("Enter num : ")
    n = SumOfList(ls)
    print ("Sum : " + str(n))
    return

# Exrecise 2 B :
# Summing list function
def SumOfList(ls):
    sum = 0
    for i in range(len(ls)):
        sum += ls[i]
    return sum


# Exrecise 3:
# Tic Tac Toe Exrecise:
def TicTacToe(Mat):
    Pos = 0 # 0 represent Tie , 1 win for player 1 , 2 win for player 2
    if Mat[0][0] == Mat[1][0] == Mat[2][0] and Mat[0][0] != 0:
        Pos = Mat[0][0]
    elif Mat[0][1] == Mat[1][1] == Mat[2][1] and Mat[0][1] != 0:
        Pos = Mat[0][1]
    elif Mat[0][2] == Mat[1][2] == Mat[2][2] and Mat[0][2] != 0:
        Pos = Mat[0][2]
    elif Mat[0][0] == Mat[0][1] == Mat[0][2] and Mat[0][0] != 0:
        Pos = Mat[0][0]
    elif Mat[1][0] == Mat[1][1] == Mat[1][2] and Mat[1][0] != 0:
        Pos = Mat[1][0]
    elif Mat[2][0] == Mat[2][1] == Mat[2][2] and Mat[2][0] != 0:
        Pos = Mat[2][0]
    elif Mat[0][0] == Mat[1][1] == Mat[2][2] and Mat[0][0] != 0:
        Pos = Mat[0][0]
    elif Mat[0][2] == Mat[1][1] == Mat[2][0] and Mat[0][2] != 0:
        Pos = Mat[0][2]

    if Pos == 0:
        print("Tie")
    else:
        print("Player " + str(Pos) + " has won")
    return


# Exrecise 4:
# String contraction Exrecise:
def ContractionString(st):
    if len(st) == 0:
        return ""
    count = 0
    let = st[0]
    for letter in st:
        if letter == let:
            count += 1
        else:
            break
    return "" + str(let) + "" + str(count) + "" + str(ContractionString(st[count:]))


def main():
    # Main function:
    # checks the pass code and the TriesLeft
    """
    global TriesLeft
    while True:
        pass1 = input('Enter pass code here: ')
        if pass1 == PassCode:
            ATM_Interface()
        elif TriesLeft == 0:
            print('Too many fails, Exits...')
            exit(0)
        else:
            print('Wrong pass code, ' + str(TriesLeft) + ' tries left!')
            TriesLeft -= 1
    # Exreicse 2 init:
    CalcSum()

    # Exrecise 3 init (player 1 win situtation):
    Mat = [[1,0,2],
           [1,0,2],
           [1,2,0]]
    TicTacToe(Mat)
    """
    st = "aabbbbcdddeaaaaa"
    st = ContractionString(st)
    print(st)


if __name__ == '__main__':
    main()






