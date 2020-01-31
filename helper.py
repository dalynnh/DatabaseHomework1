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
            return Record(record, fields, middle * recordSize)
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
        record = Record(line, fields, pos)
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
            while(range(fields[name] - len(write))):
                write = write + '-'
        final += write
    data.seek(record.position)
    data.write(final)
    new = Record(getRecord(data, record.position / recordSize), fields, record.position)
    print('Here is the updated record')
    new.printRecord()

def addRecord(data, overflow, fields):
    setGlobals(fields)
    final = ''
    for name in fields:
        if name != 'totalRecordSize' and name != 'numRecords':
            print('Please enter a value for ' + name)
            field = input()
            if len(field) > fields[name]:
                write = field[:fields[name]]
            else:
                write = field
                while(range(fields[name] - len(write))):
                    write = write + '-'
            final += write
    num = data.seek(0, 2) + recordSize
    overflow.write(final + '\n')
    new = Record(getRecord(overflow, num / recordSize), fields, num)
    print('Here is the new record')
    new.printRecord()
    if num / recordSize > 4:
        print('Merging overflow into data file...')
        mergeData(data, overflow, fields)

def mergeData(data, overflow, fields):
    overflow.seek(0)
    records = []
    for record in overflow.readlines():
        records.append(record)
    records.sort(key=recordName)
    num = int(data.seek(0, 2) / recordSize)
    for i in range(num):
        data.seek(num * recordSize)
        line = data.readline()
        data.seek(num * recordSize)
        dataName = recordName(line)
        record = recordName(records[0])
        if dataName < record:
            data.write(line)
        else:
            data.write(records.pop(0))
            count = 0
            for i in records:
                record = recordName(i)
                if dataName < record:
                    records.insert(count, line)
                count += 1
    for record in records:
        data.write(record)



def recordName(record):
    return record[4:38].replace('-', '').lower()
            
def setGlobals(fields):
    global numRecords, recordSize
    numRecords = fields['numRecords']
    recordSize = fields['totalRecordSize']