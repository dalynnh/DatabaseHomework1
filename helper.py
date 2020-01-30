numRecords = 0
recordSize = 0

def getRecord(data, recordNum):
    record = ''
    global numRecords, recordSize
    if recordNum >= 1 and recordNum <= numRecords:
        data.seek(recordNum * recordSize, 0)
        record = data.readline()
    return record

def binarySearch(data, name, totalRecords, size):
    global numRecords, recordSize
    numRecords = totalRecords
    recordSize = size
    low = 0
    high = totalRecords -1
    record = ''
    found = False
    while not found and high >= low:
        middle = (low + high) / 2
        record = getRecord(data, int(middle))
        recordName = record[4:38]
        recordName = recordName.replace('-', '')
        print(recordName)
        if recordName == name:
            found = True
        elif recordName < name:
            low = middle
        else: 
            high = middle
    if (found):
        return record
    else:
        return 'Could not find record.'
    