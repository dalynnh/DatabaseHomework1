from record import *

numRecords = 0
recordSize = 0

def getRecord(data, recordNum):
    record = ''
    global numRecords, recordSize
    if recordNum >= 1 and recordNum <= numRecords:
        data.seek(recordNum * recordSize, 0)
        record = data.readline()
    return record

def searchRecord(data, overflow, name, fields):
    record = binarySearch(data, name, fields)
    if record:
        return record
    else:
        record = linearSearch(overflow, name, fields)
        if record:
            return record
    return False

def binarySearch(data, name, fields):
    setGlobals(fields)
    low = 0
    high = numRecords - 1
    record = ''
    while high >= low:
        middle = int((low + high) / 2)
        record = getRecord(data, middle)
        dataName = recordName(record)
        if dataName == name:
            return Record(record, fields, middle * recordSize, False)
        elif dataName < name:
            low = middle + 1
        else: 
            high = middle - 1
    return False

def linearSearch(data, name, fields):
    setGlobals(fields)
    pos = 0
    data.seek(0)
    for line in data.readlines():
        record = Record(line, fields, pos, True)
        if record.value['name'].lower() == name.lower():
            return record
        pos += recordSize
    return False

def updateRecord(data, record, fields):
    record.updateRecord()
    final = ''
    for name in record.value:
        if len(record.value[name]) > fields[name]:
            write = record.value[name][:fields[name]]
        else:
            write = record.value[name]
            while (range(fields[name] - len(write))):
                write = write + '-'
        final += write
    data.seek(record.position)
    data.write(final)
    new = Record(getRecord(data, record.position / recordSize), fields, record.position, record.overflow)
    print('Here is the updated record')
    new.printRecord()

def addRecord(data, overflow, config, fields):
    setGlobals(fields)
    final = ''
    for name in fields:
        if name != 'totalRecordSize' and name != 'numRecords':
            print('Please enter a value for ' + name)
            field = input().upper()
            if len(field) > fields[name]:
                write = field[:fields[name]]
            else:
                write = field
                while(range(fields[name] - len(write))):
                    write = write + '-'
            final += write
    num = overflow.seek(0, 2)
    overflow.write(final + '\n')
    flag = (num + recordSize) / recordSize > 4
    new = Record(getRecord(overflow, num / recordSize), fields, num, not flag)
    print('Here is the new record')
    new.printRecord()
    if flag:
        print('Merging overflow into data file...')
        mergeData(data, overflow, config, fields)

def mergeData(data, overflow, config, fields):
    overflow.seek(0)
    records = []
    for record in overflow.readlines():
        records.append(record)
    add = len(records)
    records.sort(key=recordName)
    num = int(data.seek(0, 2) / recordSize)
    print(num)
    for i in range(num):
        data.seek(i * recordSize)
        line = data.readline()
        data.seek(i * recordSize)
        dataName = recordName(line)
        record = recordName(records[0])
        if dataName < record:
            data.write(line)
        else:
            data.write(records.pop(0))
            insert = 0
            for i in range(len(records)):
                if insert == 0:
                    record = recordName(records[i])
                    if dataName < record:
                        insert = i
            records.insert(insert, line)
    data.writelines(records)
    data.seek(0)
    data.readline()
    overflow.truncate(0)
    pos = config.seek(0, 2) - 14
    config.seek(pos)
    config.write('numRecords' + ',' + str(num + add))
    config.seek(0)
    config.read()

def recordName(record):
    return record[4:38].replace('-', '').lower()

def deleteRecord(data, overflow, config, record, fields):
    name = record.value['name'] + '(deleted)'
    if len(name) > fields['name']:
        write = name[:fields['name']]
    else:
        write = name
        for _ in range(fields['name'] - len(name)):
            write += '-'
    if record.overflow:
        overflow.seek(record.position)
        writeDeleted(overflow, write, fields)
        overflow.seek(record.position)
        overflow.readline()
    else: 
        data.seek(record.position)
        writeDeleted(data, write, fields)
        data.seek(record.position)
        data.readline()
    pos = config.seek(0, 2) - 14
    config.seek(pos)
    num = config.readline().split(',')
    config.seek(pos)
    config.write('numRecords' + ',' + str(int(num[1]) - 1))
    config.seek(0)
    config.read()
    

def writeDeleted(data, write, fields):
    for field in fields:
        if field != 'totalRecordSize' and field != 'numRecords' and field != 'name':
            for _ in range(fields[field]):
                data.write(' ')
        elif field == 'name':
            data.write(write)
            
def setGlobals(fields):
    global numRecords, recordSize
    numRecords = fields['numRecords']
    recordSize = fields['totalRecordSize']