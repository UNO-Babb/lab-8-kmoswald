#ProcessData.py
#Name: Kaitlyn Oswald
#Date: 11/2/25
#Assignment: Lab 8

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()

  for line in inFile:
    data = line.split()
    first = data[0]
    last = data[1]
    idNum = data[3]
    year = data[5]
    major = data[6]

    student_id = makeID(first, last, idNum) 
    makeYear = convert_year(year)
    makeMajor = major[:3]
    majorYear = makeMajor + "-" + makeYear

    output = last + "," + first + "," + student_id + "," + majorYear + "\n"
    outFile.write(output)
    

  print(student_id)

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

def makeID(first, last, idNum):
  print(first, last, idNum)
  idLen = len(idNum)

  while len(last) < 5:
    last = last + "X"

  id = first[0] + last + idNum[idLen - 3: ]

  return id

def convert_year(year):
    if year == "Freshman":
      return "FR"
    if year == "Sophomore":
      return "SO"
    if year == "Junior":
      return "JR"
    if year == "Senior":
      return "SR"



if __name__ == '__main__':
  main()
