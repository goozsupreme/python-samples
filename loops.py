strloop = "Y"

while(strloop == "Y"):
     strask = input("a cur, b volts, c res, d quit ")
     strask = strask.lower()
     
     if(strask == "a"):
          z = int(input("Enter res "))
          q = int(input("Enter volts "))
          v = q / z
          print("Current is",v)
     
     elif(strask == "b"):
           v = int(input("Enter cur "))
           z = int(input("Enter res "))
           q = v * z
           print("Volts is",q)
     
     elif(strask == "c"):
          q= int(input("Enter volts "))
          v =int(input("Enter cur "))
          z = q / v
          print("Res is",z)
     
     elif(strask == "d"):
         strloop = "X"
     
     else:
         print("Bad data input")
