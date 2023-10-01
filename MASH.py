import random
from MASH_pkg.cities import city_selction
from MASH_pkg.car_data import car_select 

#Define Variables For Each Category
MP = ["Deondre", "Brad Pitt", "Paul Hammond", "The Hulk","Peter Parker","Josh", " Tyronne","Muqadine","Abishek", " Aaron Claus"]
rand_Mpartner = random.choice(MP)
P4=[]

FP = ["Carla","Mary","Jo"]
rand_Fpartner = random.choice(FP)



'''
while True:
    gender_choice = input("Enter '1' for Male life partner and '2' for Female life partner: ")
    if gender_choice == 1:
        P4 = rand_Mpartner
        return("Computer Chosen Life Partner: ", rand_Mpartner)
    if gender_choice == 2:
        P4 = rand_Fpartner
        return(rand_Fpartner)
    else:
        print ("Please choose 1 or 2")
   # print ("Computer Selected Partner: ", partner)
'''

K = [10,5,3,1,0,9,8,6]
rand_kids = random.choice(K)

S =[38522,63080,41209,72048,40461,77531,33369,78124,45389,40311,52784,106709,312500,670000,1354765,82369]
rand_sal = random.choice(S)

job =["Graphic Designer","Software Engineer",
"Retail Store Manager",
"Project Manager in Construction",
"Office Manager",
"Attorney",
"Administrative Assistant",
"Controller",
"Executive Assistant",
"Elementary School Teacher",
"Registered Nurse",
"Pilot", 
"Astronaut",
"Bowling Instructor",
"Fitness Influencer",
"Dat Center Technician", 
"Chairman", 
"Nail Salon Owner", 
"Supply Chain Coordinator"]
rand_job = random.choice(job)


print("Welcome to MASH!\nThis is a fun fortune telling game enjoyed all over the world.\nThe rules are as follows:\n1)Choose 3 potential options for each life category\n2)The cpu will choose the 4th option in each category\n3)Start spinning the spiral\n4)However many spaces between your spiral will be your counter and decide your fate.")

#Player Inupts; L=Life Partner, 

P1, P2, P3 = input("Enter 3 names for Life Partner: ").split()
def Partner_pick(self, P4):
    gender_choice = input("Enter '1' for Male life partner and '2' for Female life partner: ")
    if gender_choice == 1:
        P4 = rand_Mpartner
        return P4
        
    if gender_choice == 2:
        P4 = rand_Fpartner
        return P4
    else:
        print ("Please choose 1 or 2")

   # print ("Computer Selected Partner: ", partner)
print("Life Partner 1: ", P1)
print("Life Partner 2: ", P2)
print("Life Partner 3: ", P3)
print("Life Partner 4: ", P4)
LP_list = [P1,P2,P3,P4]

K1, K2, K3 = input("Enter 3 options for Number of Kids: ").split()
print("Number of Kids: ", K1)
print("Number of Kids: ", K2)
print("Number of Kids: ", K3)
print("Number of Kids: ", rand_kids)
K_list = [K1, K2, K3, rand_kids]

J = [str(J) for J in input("Enter 3 options for Job: ").split()]
J.append(rand_job)
print("Job Options: ", J)

[J1, J2, J3] = input("Enter 3 options for Salary: ").split()
print("Salary 1: ", J1)
print("Salary 2: ", J2)
print("Salary 3: ", J3)
print("Salary 4: ",rand_sal)

C1, C2, C3 = input("Enter 3 options for Car: ").split()
print("Car 1: ", C1)
print("Car 2: ", C2)
print("Car 3: ", C3)
print("Car 4: ", car_select)

L1, L2, L3 = input("Enter 3 options for Location: ").split()
print("City 1: ", L1)
print("City 2: ", L2)
print("City 3: ", L3)
print("City 4: ", city_selction)
