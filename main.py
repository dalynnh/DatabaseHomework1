print('1) Create new database')
print('2) Open database')
print('3) Close database')
print('4) Display record')
print('5) Update record')
print('6) Create report')
print('7) Add record')
print('8) Delete record')
print('9) Quit')
choice = input()

if choice == '1':
    print('Create db')
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
    print('Quitting...')
else:
    print('Choice not valid')