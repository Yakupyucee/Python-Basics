def letterAverageCalculate(line):
    list = line.split(':')
    studentName = list[0]
    gradelist = list[1].split(',')
    average = (int(gradelist[0]) + int(gradelist[1]) + int(gradelist[2])) / 3

    lettergrade = ''

    if average > 90:
        lettergrade = 'AA'
    elif average > 80 :
        lettergrade = 'BA'
    elif average > 70 :
        lettergrade = 'BB'
    elif average > 60 :
        lettergrade = 'CB'
    elif average > 50 :
        lettergrade = 'CC'
    elif average > 40 :
        lettergrade = 'DC'
    elif average > 35 :
        lettergrade = 'DD'
    else :
        lettergrade = 'FF'
    
    return (studentName + ' : ' + lettergrade)


def gradeRegister():
    with open('student.txt','a',encoding='utf-8') as file:
        name = input('Enter student name: ')
        surname = input('Enter student surname: ')
        while True:
            try:
                grade1 = int(input('Enter student Grade-1: '))
                grade2 = int(input('Enter student Grade-2: '))
                grade3 = int(input('Enter student Grade-3: '))
                break
            except ValueError:
                print('Please enter integer value')
                continue
        file.write(name + ' ' + surname + ':' + str(grade1) + ',' + str(grade2) + ',' + str(grade3) + '\n')


def readGrade():
    with open('student.txt', 'r', encoding='utf-8') as file:
        list = file.readlines()

        for line in list:
            print(letterAverageCalculate(line))


def averageRegister():
    try:
        with open('student.txt','r',encoding='utf-8') as file:
            list = file.readlines()
            letterList = []
            for line in list:
                letterList.append(letterAverageCalculate(line)+ '\n')

            with open('letterGrade.txt', 'w', encoding= 'utf-8') as letterFile:
                letterFile.writelines(letterList)
        print('Registration completed successfully.')
    except:
        print("An error occurred. It was not saved.")


def main():
    while True:
        process = input('1-) Grade registering\n2-) Read grades\n3-) Average registering\n4-) Exit\n')
        if process == '1':
            gradeRegister()
        elif process == '2':
            readGrade()
        elif process =='3':
            averageRegister()
        elif process == '4':
            break
        else:
            print('Please press a valid key.')


main()