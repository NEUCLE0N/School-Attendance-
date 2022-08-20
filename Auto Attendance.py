#190051232 Assignemnt 2d list
date ="11/9/21"
attendance = [
    ['ihfaz',1],
    ['alamin',0],
    ['nihal', 1],
    ['sazid', 0],
    ['adrian',0]
]
def atten():  
    for i in range(len(attendance)):
        validInput = False
        while not validInput:
            print(f"{attendance[i][0]} present(1) or absent(0)?")
            pres =int(input("Input 1 for present 0 for absent :"))
            if pres == 1 or pres == 0:
                attendance[i][1] = pres
                validInput = True
            else:
                print("\nInvalid input")
                print("please input 1 or 0 only\n")

        

f = atten()


def check():
   present = []
   absent = []
   for a in attendance:
      attend = a[1]
      name = a[0]
      if attend == 1:
          present.append(name)
      else:
          absent.append(name)

   print(f"Students that were present on {date} ",present)
   print(f"Students that were absent on {date} ",absent)

print("\n")
for i in attendance:
    print(i,end='\n')

check()
