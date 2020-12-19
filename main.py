import time

print('This is a basic Python Terminal. \tIt can preform some basic operations')
print('Enter your username for the session. \tType all the commands in lowercase')
uName = input('>>')
com = 'initialized'
print(com)
while com != 'exit':
    com = input('\n' + uName + '@basicPythonTerminal$')

    if com == 'exit':
        print('logout')

    elif com == 'help':
        print('help \t\tDisplays Help')
        print('exit \t\tExits')
        print('print \t\tInitializes the print command')
        print('calc \t\tInitializes the calculator')
        print('uname \t\tChanges the username')
        print('info \t\tIt displays information about the terminal')
        print('time \t\tDisplays the time')
        print('date \t\tDisplays the date.')
        print()
        print('The PythonTerminal is case sensitive so it is recommended to type in lowercase.')

    elif com == 'print':
        print('Enter the line to print')
        pnt = input('>>')
        print(pnt)

    elif com == 'calc':
        print('initialized calculator')
        op = '1'
        op = int(op)
        while op != 7:
            print('Enter an option. \nOptions are: \n\t1.Addition\n\t2.Substraction\n\t3.Multiplication\n\t4.Division\n\t5.Floor Division\n\t6.Power\n\t7.Exit')
            op = input('>>')
            op = int(op)
            if op == 7:
                print('exit')
            elif op == 1:
                print('Enter the first number.')
                num1 = input('>>')
                num1 = int(num1)
                print('Enter the second number.')
                num2 = input('>>')
                num2 = int(num2)
                print(num1 + num2)
                input('Press any key to continue...')
            elif op == 2:
                print('Enter the first number.')
                num1 = input('>>')
                num1 = int(num1)
                print('Enter the second number.')
                num2 = input('>>')
                num2 = int(num2)
                print(num1 - num2)
                input('Press any key to continue...')
            elif op == 3:
                print('Enter the first number.')
                num1 = input('>>')
                num1 = int(num1)
                print('Enter the second number.')
                num2 = input('>>')
                num2 = int(num2)
                print(num1 * num2)
                input('Press any key to continue...')
            elif op == 4:
                print('Enter the first number.')
                num1 = input('>>')
                num1 = int(num1)
                print('Enter the second number.')
                num2 = input('>>')
                num2 = int(num2)
                print(num1 / num2)
                input('Press any key to continue...')
            elif op == 5:
                print('Enter the first number.')
                num1 = input('>>')
                num1 = int(num1)
                print('Enter the second number.')
                num2 = input('>>')
                num2 = int(num2)
                print(num1 // num2)
                input('Press any key to continue...')
            elif op == 6:
                print('Enter the first number.')
                num1 = input('>>')
                num1 = int(num1)
                print('Enter the second number.')
                num2 = input('>>')
                num2 = int(num2)
                print(num1 ** num2)
                input('Press any key to continue...')
            else:
                print('Invalid option... \tPlease try again.')

    elif com == 'uname':
        print('Initialized uname util...')
        input('Press any key to continue...')
        print('Old user name is ' + uName)
        print('Enter the new username or leave blank to cancel.')
        cName = input('>>')
        if cName == '':
            print('Successfully canceled.')
        else:
            print('Username ' + uName + ' changed as ' + cName + '.')
            uName = cName

    elif com == 'info':
        print('Made by Titam')
        print('Version: 1.0.0')
        print('App name: PythonTerminal')
        print('Languages used: Python3')
        print('Project finish date: 13/12/2020')
        input('Press any key to continue...')

    elif com == 'time':
        cur = time.strftime('%H:%M:%S', time.localtime())
        print('The current time is ' + cur + '.')

    elif com == 'date':
        cur = time.strftime('%b %d %Y')
        print('Today is ' + cur + '.')

    else:
        print('Invalid Statement \tType `help` to get help')
