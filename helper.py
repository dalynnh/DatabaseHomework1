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
    print(fields)
    numRecords = fields['numRecords']
    recordSize = fields['totalRecordSize']
    low = 0
    high = numRecords - 1
    record = ''
    while high >= low:
        print(low)
        print(high)
        middle = int((low + high) / 2)
        record = getRecord(data, middle)
        recordName = record[4:38].replace('-', '').lower()
        if recordName == name:
            return record
        elif recordName < name:
            low = middle + 1
        else: 
            high = middle - 1
    return False

def linearSearch(data, name, fields):
    return False
    
def printRecord(record, fields):
    count = 0
    for name in fields:
        if name != 'totalRecordSize' and name != 'numRecords':
            value = record[count:fields[name] + count].replace('-', '')
            print(name + ': ' + value)
            count += fields[name]