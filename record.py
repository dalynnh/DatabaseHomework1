class Record:
    def __init__(self, record, fields, position):
        count = 0
        for name in fields:
            if name != 'totalRecordSize' and name != 'numRecords':
                value = record[count:fields[name] + count].replace('-', '')
                count += fields[name]
                self.value[name] = value
        self.position = position
    
    position = 0
    value = {}

    def printRecord(self):
        for name in self.value:
            print('{}: {}'.format(name, self.value[name]))

    def updateRecord(self):
        for name in self.value:
            if name != 'name':
                print('The current {} is {}. Enter the new value or just press enter for no change.'.format(name, self.value[name]))
                update = input()
                if update != '':
                    self.value[name] = update