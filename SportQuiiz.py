import requests, json, random #

Rätt = 0 # definar vad jag kommer använda senare i koden
Fel = 0 
färdiga_frågor = []

Namn = (input("Hej , Vad heter du ? \n "))

print( " Tjena " + Namn + " Välkomen till frågasporten som handlar om sport. \n Lycka till !! \n Vi börjar Med fråga nr 1.") 

url = "https://opentdb.com/api.php?amount=10&category=21&difficulty=hard&type=multiple" #länken där jag hämtar mina frågor ifrån(api)

Frågorna = requests.get(url).json()

for x in Frågorna["results"]:
    fråga= {}
    fråga["fråga"] = (
        x["question"]
    )
    svar =([])

    svar.append(x["correct_answer"])

    for a in x["incorrect_answers"]:
        svar.append(a)

    randomIndex = random.randint(0, 2)
    svar[0], svar[randomIndex] = svar[randomIndex], svar[0]

    fråga["svar"] = svar
    fråga["correctIndex"] = randomIndex

    färdiga_frågor.append(fråga)

for i in färdiga_frågor:
    svaren = i["svar"]

    Svaret = input(
                i["fråga"]
                + "\n-Svars alternativ : 1, "
                + svaren[0]
                + " 2, "
                + svaren[1]
                + " 3, "
                + svaren[2]
                + "\n>"
            )
    try:
        if (int(Svaret) == i["correctIndex"]):
            print("Rätt svar")
            Rätt = Rätt + 1
        else:
            print("Fel svar")
            Fel = Fel + 1

    except:
        print("Välj ett av alternativen")

print("Du fick", Rätt, "rätt svar och", Fel,"fel svar")
