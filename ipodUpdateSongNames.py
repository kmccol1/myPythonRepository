#*****************************************************************************************
#    Author: Kyle McColgan
#    Date: 03 February 2023
#    Filename: ipodUpdateSongNames.py
#    Description: Python script to copy and rename files based on audio metadata (title).
#*****************************************************************************************

import os
import os.path
import shutil
from datetime import datetime
from os.path import getmtime
import eyeD3

#*****************************************************************************************

def main ( ):

    sourceFilePath = "/home/kyle/ipod-documents-folder/iPod_Control/Music/"
    destinatonFilePath = "/home/kyle/ipod-documents-updated"

    fileList = []
    filePathList = os.listdir(path= sourceFilePath)

    for aPath in filePathList:
        print (aPath + ' ') #list of file paths e.g. F00, F01, F02,... F13

        for aFileEntry in filePathList:
            songFolder = os.listdir(path = sourceFilePath + aPath)
            
            for song in songFolder: #randomly named mp3/m4a? files...
                fullyQualifiedFilePathName = sourceFilePath + aPath + '/' + song
                shutil.copy2(fullyQualifiedFilePathName, destinatonFilePath) #copy2() preserves metadata
                print('Successfully copied file: ' + song + ' to the new destination.')
                #copy all files first to destination, rename upon transfer

    copiedDataFiles = []
    copiedDataFiles = os.listdir(destinatonFilePath)

    print ('All files copied successfully.')
    print ('Renaming files...')

    for song in copiedDataFiles:
        audioFile = eyeD3.load(song)
        os.rename(song, audioFile.tag.title)
        print('Successfully renamed file: ' + song + ' to the new name: ' + audioFile.tag.title)


    print ('All files copied and renamed successfully. Enjoy!')
    print('\n***Goodbye***\n')

#*****************************************************************************************

if __name__ == '__main__':
    main()