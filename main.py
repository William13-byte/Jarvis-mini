 #Before starting / Loading in

#Looking if all required modules is installed
from functions.tools.downloadModules import moduleTestLoad
moduleTestLoad()

#import functions.settingsGui

import os
from functions.startUp import Startsequvens
from functions.wikiSearchArticle import wikiSearchArticle
from functions.tools.updateSettings import *
from functions.findFiles import openSearchFiles
from functions.tools.googleTranslate import transText
from functions.tools.ttsTool import tts
from functions.tools.STP import *
from functions.settingsGui import settings



#Checking if there is a startup script
osName = os.getlogin()
startUpPath = 'C:/Users/' + osName + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startUpFileJarvisMini.bat'

directory = os.getcwd()

if os.path.isfile(startUpPath) == False:
    startUp = open('C:/Users/' + osName + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startUpFileJarvisMini.txt', "w")
    #startUp.write("import os\n")
    #print(directory)
    #startUp.write("os.system('cmd /c cd ' + r'" + directory + "'+' & dir')")
    startUp.write("cd " + directory + "\nmain.py")
    startUp.close()
    base = os.path.splitext('C:/Users/' + osName + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startUpFileJarvisMini.txt')[0]
    #os.rename('C:/Users/' + osName + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startUpFileJarvisMini.txt', base + ".py")
    os.rename('C:/Users/' + osName + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/startUpFileJarvisMini.txt', base + ".bat")


#Loading username
if returnSetting(0) == "null":
    changeSetting(0, osName)


#Responses that the bot is looking for

responseForWiki = [
    "wiki",
    "wikipedia",
    "search on wikipedia",
    "wiki search",
    "wikipedia search"
    ]

responseForSettings = [
    "setting",
    "settings",
    "open setting",
    "open settings",
    "settings open",
    "setting open"
]

#All commands
Startsequvens()
tts(transText("What can I help you with?"))
while True:
    continueToSearch = True
    inputAnswer = input().lower()
    #inputAnswer = None
    #while inputAnswer==None:
        #inputAnswer = returnstp()
    print(inputAnswer)


    if continueToSearch:
        for wiki in range(len(responseForWiki)):
            if inputAnswer == transText(responseForWiki[wiki]):
                tts(transText("What do you want to search for?"))
                wikiSearchArticle(str(input(transText("Article:") + " ")))
                continueToSearch == False
                break
    
    if continueToSearch:
        for setting in range(len(responseForSettings)):
            if inputAnswer == transText(responseForSettings[setting]):
                #settings()
                continueToSearch == False
                break

    


    
    if inputAnswer == "exit":
        break

    #If response can not be found
    if continueToSearch:
        print("Error: ", end="")
        tts(transText("Can not do that"))

    tts(transText("Can I help with anything else?"))