import helper

data = None
config = None
overflow = None
databaseName = ''

def createDB():
    print('Which csv file would you like to create the database out of?')
    csvFilename = input()
    fields = {
        'rank': 4,
        'name': 35,
        'city': 20,
        'state': 2,
        'zip': 5,
        'employee': 10,
        'totalRecordSize': 77
    }
    numRecords = 0
    csvFile = open(csvFilename + '.csv', 'r')
    data = open(csvFilename + '.data', 'w')
    for line in csvFile:
        record = line.replace('\n', '').split(',')
        i = 0
        for field in fields:
            if field != 'totalRecordSize':
                if len(record[i]) > fields[field]:
                    write = record[i][:fields[field]]
                else:
                    write = record[i]
                    while(range(fields[field] - len(write))):
                        write = write + '-'
                data.write(write)
                i += 1
        data.write('\n')
        numRecords += 1
    data.close()
    csvFile.close()
    config = open(csvFilename + '.config', 'w')
    for name in fields:
        config.write(name + ',' + str(fields[name]) + '\n')
    config.write('numRecords,' + str(numRecords))
    config.close()
    overflow = open(csvFilename + '.overflow', 'w')
    overflow.close()

def openDB():
    global data, config, overflow, databaseName
    if data:
        print(databaseName + ' is currently open. Please close before opening a new DB.')
    else:
        print('Which database would you like to open?')
        databaseName = input()
        data = open(databaseName + '.data')
        config = open(databaseName + '.config')
        overflow = open(databaseName + '.overflow')

def closeDB():
    global data, config, overflow, databaseName
    if data:
        print('Closing the database ' + databaseName)
        databaseName = ''
        data.close()
        data = None
        config.close()
        config = None
        overflow.close()
        overflow = None
    else:
        print('There are no databases currently open.')

def displayRecord():
    global data, config, overflow
    fields = {}
    if data:
        print('Enter the name of the record you would like to search for. Limited to 35 characters.')
        name = input()
        for line in config.readlines():
            lineArr = line.split(',')
            fields[lineArr[0]] = int(lineArr[1])
        if not helper.binarySearch(data, name, fields):
            if not helper.linearSearch(overflow, name):
                print('Could not find record.')
    else:
        print('There are no databases currently open. Please open a database to display a record.')

def createReport():
    global data, config, overflow

    report = open(report.txt,'w')

    for i in range(10):
        