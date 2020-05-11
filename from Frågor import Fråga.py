from Frågor import Fråga

#Namn = (input("Hej , Vad heter du ? \n "))

#print( " Tjena " + Namn + " Välkomen till frågasporten som handlar om Fotboll. \n Lycka till !! \n Vi börjar Med fråga nr 1.") 

fråga_prompt = [ 
          "Vilket lag vann Champions league 2018 ? \na) Realmadrid \nb) Barcelona \nc) Arsenal",
          "Hur många Ballon d'Or har Messi och C.Ronaldo vunnit ? \na) 5 \nb) 11 \nc) 15",
          "Vilket lag är det som inte spelar i La Liga ? \na) Sevilla \nb) Chelsea  \nc) Real Sociedad "
]

frågor = [ 
         Fråga(fråga_prompt [0], "a"), 
         Fråga(fråga_prompt [1], "b"),
         Fråga(fråga_prompt [2], "b"),
         ] 

def run_test(frågor):
    poäng = 0 
    for fråga in frågor:
        svar = input(fråga_prompt)
        if svar == fråga.svar:
            poäng += 1
            print("Du fick" + str(poäng) + "/" + str(len(frågor)) + " rätt!")

run_test(frågor)

