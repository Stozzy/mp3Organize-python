import os, re

os.chdir('C:\\Music')

artistName = []
albumName = []

for (root, dirs, files) in os.walk('C:\\Users\\Stanislaw Goldyn\\Music', topdown=True):
    count = 0    
    while (count < len(files)):
        fileNameStr = files[count]
        
        f_name, f_ext = os.path.splitext(fileNameStr)
        
        if f_ext == ".bmp":
            fileNameStr = re.split(" - ", fileNameStr)
            artistName.append(fileNameStr[0])
            albumName.append(fileNameStr[2])
                    
        count = count + 1
        
    print("The artists are: ")
    print(artistName)
    print('------------------------')
    print("The albums titles are: ")
    print(albumName)

#remove .bmp from album name
#add logic to mkdir for artistName; db check to see if dir exists
#add logic to mkdir for albumName; db check to see if dir exists
#move files to respective artistName and albumName dirs
