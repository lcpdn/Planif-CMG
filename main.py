import datetime
import sys




def week0a5(dateBegin):
	jour1="2 / 3 / 2 / 2 / min 3"
	jour2="3 / 4 / 2 / 3 / min 4"
	jour3="4 / 5 / 4 / 4 / min 5"
	jour4="5 / 6 / 4 / 4 / min 6"
	jour5="5 / 6 / 4 / 4 / min 7"
	jour6="5 / 7 / 5 / 5 / min 7"

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	datejour4=(dateBegin + datetime.timedelta(days=6)).strftime('%Y-%m-%d')
	daterepos4=(dateBegin + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
	datejour5=(dateBegin + datetime.timedelta(days=8)).strftime('%Y-%m-%d')
	daterepos5=(dateBegin + datetime.timedelta(days=9)).strftime('%Y-%m-%d')
	datejour6=(dateBegin + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
	daterepos6=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')
	daterepos62=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	print(datejour4+" : "+jour4)
	print(daterepos4+" : Repos")
	print(datejour5+" : "+jour5)
	print(daterepos5+" : Repos")
	print(datejour6+" : "+jour6)
	print(daterepos6+" : Repos")
	print(daterepos62+" : Repos")
	week6a10(dateBegin+datetime.timedelta(days=12))

def week6a10(dateBegin):
	jour1="5 / 6 / 4 / 4 / min 5"
	jour2="6 / 7 / 6 / 6 / min 7"
	jour3="8 / 10 / 7 / 7 / min 10"
	jour4="9 / 11 / 8 / 8 / min 11"
	jour5="10 / 12 / 9 / 9 / min 13"
	jour6="12 / 13 / 10 / 10 / min 15"

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	datejour4=(dateBegin + datetime.timedelta(days=6)).strftime('%Y-%m-%d')
	daterepos4=(dateBegin + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
	datejour5=(dateBegin + datetime.timedelta(days=8)).strftime('%Y-%m-%d')
	daterepos5=(dateBegin + datetime.timedelta(days=9)).strftime('%Y-%m-%d')
	datejour6=(dateBegin + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
	daterepos6=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')
	daterepos62=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	print(datejour4+" : "+jour4)
	print(daterepos4+" : Repos")
	print(datejour5+" : "+jour5)
	print(daterepos5+" : Repos")
	print(datejour6+" : "+jour6)
	print(daterepos6+" : Repos")
	print(daterepos62+" : Repos")
	week11a20(dateBegin+datetime.timedelta(days=12))

def week11a20(dateBegin):
	jour1="8 / 9 / 7 / 7 / min 8"
	jour2="9 / 10 / 8 / 8 / min 10"
	jour3="11 / 13 / 9 / 9 / min 13"
	jour4="12 / 14 / 10 / 10 / min 15"
	jour5="13 / 15 / 11 / 11 / min 17"
	jour6="14 / 16 / 13 / 13 / min 19"

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	datejour4=(dateBegin + datetime.timedelta(days=6)).strftime('%Y-%m-%d')
	daterepos4=(dateBegin + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
	datejour5=(dateBegin + datetime.timedelta(days=8)).strftime('%Y-%m-%d')
	daterepos5=(dateBegin + datetime.timedelta(days=9)).strftime('%Y-%m-%d')
	datejour6=(dateBegin + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
	daterepos6=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')
	daterepos62=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	print(datejour4+" : "+jour4)
	print(daterepos4+" : Repos")
	print(datejour5+" : "+jour5)
	print(daterepos5+" : Repos")
	print(datejour6+" : "+jour6)
	print(daterepos6+" : Repos")
	print(daterepos62+" : Repos")
	print("Bareme CCPG : 20 pompes=2/20")
	week21a25(dateBegin+datetime.timedelta(days=12))

def week21a25(dateBegin):
	jour1="12 / 17 / 13 / 13 / min 17"
	jour2="14 / 19 / 14 / 14 / min 19"
	jour3="16 / 21 / 15 / 15 / min 21"
	jour4="18 / 22 / 16 / 16 / min 21"
	jour5="20 / 25 / 20 / 20 / min 23"
	jour6="23 / 28 / 22 / 22 / min 25"

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	datejour4=(dateBegin + datetime.timedelta(days=6)).strftime('%Y-%m-%d')
	daterepos4=(dateBegin + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
	datejour5=(dateBegin + datetime.timedelta(days=8)).strftime('%Y-%m-%d')
	daterepos5=(dateBegin + datetime.timedelta(days=9)).strftime('%Y-%m-%d')
	datejour6=(dateBegin + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
	daterepos6=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')
	daterepos62=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	print(datejour4+" : "+jour4)
	print("Bareme CCPG : 22 pompes=4/20")
	print(daterepos4+" : Repos")
	print(datejour5+" : "+jour5)
	print(daterepos5+" : Repos")
	print(datejour6+" : "+jour6)
	print("Bareme CCPG : 24 pompes=6/20")
	print(daterepos6+" : Repos")
	print(daterepos62+" : Repos")
	week26a30(dateBegin+datetime.timedelta(days=12))

def week26a30(dateBegin):
	jour1="14 / 18 / 14 / 14 / min 20"
	jour2="20 / 25 / 15 / 15 / min 23"
	jour3="20 / 27 / 18 / 18 / min 25"
	jour4="21 / 25 / 21 / 21 / min 27"
	jour5="25 / 29 / 25 / 25 / min 30"
	jour6="29 / 33 / 29 / 29 / min 33"

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	datejour4=(dateBegin + datetime.timedelta(days=6)).strftime('%Y-%m-%d')
	daterepos4=(dateBegin + datetime.timedelta(days=7)).strftime('%Y-%m-%d')
	datejour5=(dateBegin + datetime.timedelta(days=8)).strftime('%Y-%m-%d')
	daterepos5=(dateBegin + datetime.timedelta(days=9)).strftime('%Y-%m-%d')
	datejour6=(dateBegin + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
	daterepos6=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')
	daterepos62=(dateBegin + datetime.timedelta(days=11)).strftime('%Y-%m-%d')

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	print(datejour4+" : "+jour4)
	print("Bareme CCPG : 27 pompes=8/20")
	print(daterepos4+" : Repos")
	print(datejour5+" : "+jour5)
	print("Bareme CCPG : 30 pompes=10/20")
	print(daterepos5+" : Repos")
	print(datejour6+" : "+jour6)
	print(daterepos6+" : Repos")
	print(daterepos62+" : Repos")
	week31a35(dateBegin+datetime.timedelta(days=12))

def week31a35(dateBegin):
	jour1="17 / 19 / 15 / 15 / min 20"
	jour2="10 / 10 / 13 / 13 / 10 / 10 / 9 / min 25"
	jour3="13 / 13 / 15 / 15 / 12 / 12 / 10 / min 30"

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	week36a40(dateBegin+datetime.timedelta(days=6))

def week36a40(dateBegin):
	jour1="22 / 24 / 20 / 20 / min 25"
	jour2="15 / 15 / 18 / 18 / 15 / 15 / 14 / min 30"
	jour3="18 / 18 / 20 / 20 / 17 / 17 / 15 / min 35"

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print("Bareme CCPG : 34 pompes=12/20")
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	week41a45(dateBegin+datetime.timedelta(days=6))

def week41a45(dateBegin):
	jour1="27 / 29 / 25 / 25 / min 35"
	jour2="19 / 19 / 22 / 22 / 18 / 18 / 22 / min 35"
	jour3="20 / 20 / 24 / 24 / 20 / 20 / 22 / min 40"  

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print("Bareme CCPG : 38 pompes=14/20")
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	week46a50(dateBegin+datetime.timedelta(days=6))

def week46a50(dateBegin):
	jour1="30 / 34 / 30 / 30 / min 40"
	jour2="19 / 19 / 23 / 23 / 19 / 19 / 22 / min 37 "
	jour3="20 / 20 / 27 / 27 / 21 / 21 / 21 / min 44 "  

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print("Bareme CCPG : 42 pompes=16/20")
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	week51a55(dateBegin+datetime.timedelta(days=6))


def week51a55(dateBegin):
	jour1="30 / 39 / 35 / 35  / min 42"
	jour2="20 / 20 / 23 / 23 / 20 / 20 / 18 / 18 / min 53"
	jour3="22 / 22 / 30 / 30 / 25 / 25 / 18 / 18 / min 55"  

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print("Bareme CCPG : 46 pompes=18/20")
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print("Bareme CCPG : 50 pompes=20/20")
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	print(" ")
	print("A compter de maintenant, il s'agit uniquement de se perfectionner... :)")
	print(" ")
	week56a60(dateBegin+datetime.timedelta(days=6))

def week56a60(dateBegin):
	jour1="30 / 44 / 40 / 40 / min 55"
	jour2="22 / 22 / 27 / 27 / 24 / 23 / 18 / 18 / min 58"
	jour3="26 / 26 / 33 / 33 / 26 / 26 / 22 / 22 / min 60"  

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")
	week60a100(dateBegin+datetime.timedelta(days=6))


def week60a100(dateBegin):
	jour1="35 / 49 / 45 / 45 / min 55"
	jour2="22 / 22 / 30 / 30 / 24 / 24 / 18 / 18 / min 59"
	jour3="28 / 28 / 35 / 35 / 27 / 27 / 23 / 23 / min 60"  

	datejour1=(dateBegin + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
	daterepos1=(dateBegin + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
	datejour2=(dateBegin + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
	daterepos2=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	datejour3=(dateBegin + datetime.timedelta(days=3)).strftime('%Y-%m-%d')
	daterepos3=(dateBegin + datetime.timedelta(days=4)).strftime('%Y-%m-%d')
	daterepos32=(dateBegin + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
	

	print(datejour1+" : "+jour1)
	print(daterepos1+" : Repos")
	print(datejour2+" : "+jour2)
	print(daterepos2+" : Repos")
	print(datejour3+" : "+jour3)
	print(daterepos3+" : Repos")
	print(daterepos32+" : Repos")



date=(datetime.datetime.now() + datetime.timedelta(days=0)).strftime('%Y-%m-%d')
print("Debut du programme le :"+date)
print("Vous êtes en capacité de réaliser "+str(sys.argv[1])+" pompes")
print("Courage à vous !")

if (int(sys.argv[1])<6):
	week0a5(datetime.datetime.now())
elif (int(sys.argv[1])>5) and (int(sys.argv[1])<11):
	week6a10(datetime.datetime.now())
elif (int(sys.argv[1])>10) and (int(sys.argv[1])<21):
	week11a20(datetime.datetime.now())
elif (int(sys.argv[1])>20) and (int(sys.argv[1])<26):
	week21a25(datetime.datetime.now())
elif (int(sys.argv[1])>25) and (int(sys.argv[1])<31):
	week26a30(datetime.datetime.now())
elif (int(sys.argv[1])>30) and (int(sys.argv[1])<36):
	week31a35(datetime.datetime.now())
elif (int(sys.argv[1])>35) and (int(sys.argv[1])<40):
	week36a40(datetime.datetime.now())
elif (int(sys.argv[1])>40) and (int(sys.argv[1])<46):
	week41a45(datetime.datetime.now())
elif (int(sys.argv[1])>45) and (int(sys.argv[1])<51):
	week46a50(datetime.datetime.now())
elif (int(sys.argv[1])>50) and (int(sys.argv[1])<56):
	week51a55(datetime.datetime.now())
elif (int(sys.argv[1])>55) and (int(sys.argv[1])<61):
	week56a60(datetime.datetime.now())
elif (int(sys.argv[1])>60):
	week60a100(datetime.datetime.now())
else :
	print("Oups. Essayez avec un nombre entier...")
