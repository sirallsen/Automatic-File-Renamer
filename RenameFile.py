import os

#All folders with items to be changed
workingDir = ["Folder1", "Folder2", "Folder3", "Folder4", "Folder5"]

for dir in workingDir:
    os.chdir('C:/Users/SirAllsen/Project/'+ dir)
    print("Changing directory to {}!!".format(dir))

    for item in os.listdir():
        fileName, fileExt = os.path.splitext(item)
        newName = ""
        #Sand
        if(fileName == "C5BBAE"):
            newName = "CEC8BC"
        #Off White
        elif (fileName == "CBBFA2"):
            newName = "FAF9F4"
        #Khaki
        elif (fileName == "958B84"):
            newName = "BFB4AD"
        #Gum
        elif (fileName == "C4A647"):
            newName = "B79C65"
        #Cinnamon
        elif (fileName == "C4A647"):
            newName = "937852"
        #Glacial Gray
        elif (fileName == "AEACA1"):
            newName = "BCBCBC"
        #Dark Gray
        elif (fileName == "646762"):
            newName = "696969"
        #Sea
        elif (fileName == "2B3042"):
            newName = "1C334E"
        #Coffee
        elif (fileName == "4E403B"):
            newName = "4E3F38"
        #Caramel
        elif (fileName == "704822"):
            newName = "97693B"
        #Military-Green
        elif (fileName == "444940"):
            newName = "3A443F"
        #Royal Blue
        elif (fileName == "005A92"):
            newName = "0D3875"
        #Yellow
        elif (fileName == "F7B718"):
            newName = "F7B718"
        #Blood
        elif (fileName == "9B1B30"):
            newName = "9B1C1C"

        if(newName != ""):
            print("{}{}".format(fileName, fileExt))
            print(newName+fileExt)
            os.rename(item, newName+fileExt)