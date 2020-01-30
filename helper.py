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
    found = False
    while not found and high >= low:
        middle = (low + high) / 2
        record = getRecord(data, int(middle))
        recordName = record[4:38]
        recordName = recordName.replace('-', '')
        if recordName == name:
            count = 0
            for name in fields:
                if name != 'totalRecordSize' and name != 'numRecords':
                    value = record[count:fields[name] + count].replace('-', '')
                    print(name + ': ' + value)
                    count += fields[name]
            found = True
        elif recordName < name:
            low = middle
        else: 
            high = middle
    return found

def linearSearch(data, name):
    print(name)
    