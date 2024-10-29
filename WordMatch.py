def MatchWord(Words):
    Ctr=0
    List=[]
    for Word in Words:
        if len(Word)>1 and Word[0]==Word[-1]:
            Ctr+=1
            List.append(Word)
    print("List of words with first and last character same \n",List)
    return Ctr
Count=MatchWord(["Gul","Groot","January","WoW","27"])



