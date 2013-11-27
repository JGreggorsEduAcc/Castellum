import Zero
import Events
import Property
import VectorMath

class LoadHighscore:
    def Initialize(self, initializer):
        self.filename = "save.txt"
        self.UserDirect = Zero.GetUserDirectory()
        self.OpenFile()
        
    def OpenFile(self):
        scores = []
        listScores = []
        NameFile = open( self.UserDirect + "Castellum\\" + self.filename, "r")
        
        allText = NameFile.read().splitlines()
        NameFile.close()
        

        
        for line in allText:
            #print("LINE:  " + line)
            #line.rstrip() 
            #print("[" + line + "]")
            #test = []
            #for char in line.rstrip():
            #    test.append(char)
            
            #print("TEST: " + test)
            
            listScores.append(line.rstrip())
            
            #print("[" + str(listScores[0]) + "]")
        for i in range(1,11): #While in the range between 1-5, append the names thus finding the cogs
            scores.append(self.Space.FindObjectByName("Score"+ str(i)))
            print(scores)
            scores[i - 1].SpriteText.Text = listScores[i - 1]
            

Zero.RegisterComponent("LoadHighscore", LoadHighscore)