import database

def printMenu():
    print('1) Create new database')
    print('2) Open database')
    print('3) Close database')
    print('4) Display record')
    print('5) Update record')
    print('6) Create report')
    print('7) Add record')
    print('8) Delete record')
    print('9) Quit')

def main():
    printMenu()
    choice = input()
    if choice == '1':
        database.createDB()
    elif choice == '2':
        print('Open db')
    elif choice == '3':
        print('Close db')
    elif choice == '4':
        print('Display record')
    elif choice == '5':
        print('Update record')
    elif choice == '6':
        print('Create report')
    elif choice == '7':
        print('Add record')
    elif choice == '8':
        print('Delete record')
    elif choice == '9':
        global run
        run = False
    else:
        print('Choice not valid')

run = True
while run:
    main()