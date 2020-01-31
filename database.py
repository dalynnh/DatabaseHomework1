import helper

data = None
config = None
overflow = None
databaseName = ''
fields = {}

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
        data = open(databaseName + '.data', 'r+')
        config = open(databaseName + '.config', 'r+')
        overflow = open(databaseName + '.overflow', 'r+')

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
    global data, overflow, fields
    if data:
        setFields()
        print('Enter the name of the record you would like to search for. Limited to 35 characters.')
        name = input().lower()
        record = helper.binarySearch(data, name, fields)
        if record:
            record.printRecord()
        else:
            record = helper.linearSearch(overflow, name, fields)
            if record:
                record.printRecord()
            else:
                print('No record was found with name (' + name + ')')
    else:
        print('There are no databases currently open. Please open a database to display a record.')

def updateRecord():
    global data, overflow, fields
    if data:
        setFields()
        print('Enter the name of the record you would like to update. Limited to 35 characters.')
        name = input().lower()
        record = helper.binarySearch(data, name, fields)
        if record:
            helper.updateRecord(data, record, fields)
        else:
            record = helper.linearSearch(overflow, name, fields)
            if record:
                helper.updateRecord(overflow, record, fields)
            else:
                print('No record was found with name (' + name + ')')
    else:
        print('There are no databases currently open. Please open a database to update a record.')

def addRecord():
    global overflow, fields
    if overflow:
        setFields()
        helper.addRecord(overflow, fields)
    else:
        print('There are no databases currently open. Please open a database to add a record.')

def deleteRecord():
    pass

def setFields():
    global fields, config
    if not fields:
        config.seek(0)
        for line in config.readlines():
            lineArr = line.split(',')
            fields[lineArr[0]] = int(lineArr[1])