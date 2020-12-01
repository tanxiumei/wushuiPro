
#获取csv文件里的内容，返回一个包含list的list
import csv
from faker import Faker
from xpinyin import Pinyin
def getData(filePath):
    setDate(filePath)
    csvFile = filePath
    print(csvFile)
    with open(csvFile) as f:
        rows = csv.reader(f)
        myData = []
        temp = []
        for row in rows:
            temp.extend(row)
            myData.append(temp)
            temp = []
    return myData
def setDate(filePath):
    faker = Faker(locale='zh_CN')

    file = open(filePath, 'w', newline='')
    fwrite = csv.writer(file)
    p = Pinyin()
    faker1 = Faker()
    for i in range(1,2):
        tanname = faker.name()
        phoneNum = faker.phone_number()
        username = faker1.first_name()
        password = '111111'
        picFile = 'C:\\Users\\dell\\Pictures\\mingxing\\44.png'
        fwrite.writerow([tanname, phoneNum, username, password, picFile])
    file.close()
