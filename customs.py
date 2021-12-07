import csv
file = open("PB.csv", "r")
reader = csv.DictReader(file, delimiter=";")
data = list(reader)
from datetime import datetime
import datetime as dt
from os import system as s

flag = 0
outputFile = open("output.txt", "w")
while True:
    if flag == 1:
        iscontinue = input("Druk op enter om door te gaan of typ 'x' om te stoppen")
        if iscontinue == "x":
            break
    s("cls")
    choice = input("\nKies een optie:\n1. Gemiddelde boetebedrag\n2. Top 10 langst openstaande boetes\n3. Aantal fout geparkeerde auto's\n4. Ernstige boetebedragen\nW. Alle info naar bestand \nX. Exit\n")

    if choice == "w":
        print(f"Statistieken berekend op {dt.datetime.now()}", file=outputFile)

    if choice == "x":
        s("cls")
        print("Bye!\n")
        break

    if choice == "1" or choice == "w":
        totalFine = 0
        for fine in data:
            totalFine += int(fine["bedrag"])
        numFines = len(data)
        averageFine = totalFine / numFines
        s("cls")
        if choice == "w":
            print(f"1. Gemiddelde boetebedrag:\n{averageFine}", file=outputFile)
        else:
            print(f"\n1. Gemiddelde boetebedrag:\n{averageFine}\n\n")
        flag = 1

    if choice == "2" or choice == "w":
        cutoffDate = datetime.strptime('01/01/2000', '%d/%m/%Y')
        sortedData = sorted(data, key=lambda row: datetime.strptime(row["uiterste_betaaldatum"], '%d/%m/%Y'), reverse=False)
        s("cls")
        if choice == 'w':
            print("2. Top 10 langst openstaande boetes:", file=outputFile)
        else:
            print("\n2. Top 10 langst openstaande boetes:")
        for i in range(10):
            if choice == "w":
                print (f'ID {sortedData[i]["id"]} heeft een lange openstaande boete sinds {sortedData[i]["uiterste_betaaldatum"]}', file=outputFile)
            else:
                print (f'ID {sortedData[i]["id"]} heeft een lange openstaande boete sinds {sortedData[i]["uiterste_betaaldatum"]}')

        print('\n\n')
        flag = 1

    if choice == "3" or choice == "w":
        numCarParkedWrong = 0
        for car in data:
            if car["reden"] == "Dubbel geparkeerd":
                numCarParkedWrong += 1
        s("cls")
        if choice == "w":
            print(f"3. Aantal fout geparkeerde auto's\n{numCarParkedWrong}", file=outputFile)
        else:
            print(f"\n3. Aantal fout geparkeerde auto's\n{numCarParkedWrong}\n\n")
        flag = 1

    if choice == "4" or choice == "w":
        numHighFine = 0
        for highFine in data:
            if int(highFine["bedrag"]) > 100:
                numHighFine += 1
        s("cls")
        if choice == "w":
            print(f"4. Ernstige boetebedragen\n{numHighFine}", file=outputFile)
        else:
            print(f"\n4. Ernstige boetebedragen\n{numHighFine}\n\n")
        flag = 1

    if choice == "w":
        print("\nFile written!\n\n")
        outputFile.close()
        flag = 1