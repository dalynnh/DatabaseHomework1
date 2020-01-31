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

def binarySearch(data, name, fields):
    global numRecords, recordSize
    numRecords = fields['numRecords']
    recordSize = fields['totalRecordSize']
    low = 0
    high = numRecords - 1
    record = ''
    while high >= low:
        middle = int((low + high) / 2)
        record = getRecord(data, middle)
        recordName = record[4:38].replace('-', '').lower()
        if recordName == name:
            return Record(record, fields, middle * recordSize)
        elif recordName < name:
            low = middle + 1
        else: 
            high = middle - 1
    return False

def linearSearch(data, name, fields):
    return False

def updateRecord(data, record: Record, fields):
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