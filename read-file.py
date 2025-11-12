def read_file():
     try:
          filename = input("Enter file name: ")
          rff = open(filename,"r")
     except FileNotFoundError as err:
          print("There was an error: ",err)
     line = rff.readline()
     while(line != ''):
          line = line.rstrip("\n")
          print(line)
          line = rff.readline()
     rff.close()
     print("End of file.")

read_file()
