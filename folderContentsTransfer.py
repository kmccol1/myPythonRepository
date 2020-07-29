#basic tool for moving large folders and contents, renames file and sorts by date
#19-April-2020
#folderContentsTransfer.py
#Python 3.8.4

import os
import os.path
import shutil
from datetime import datetime
from os.path import getmtime

folderPath = "/home/user/Desktop/Source"
destinationPath = "/home/user/Desktop/Destination"

#filePath = folderPath + "/" + image
imageList = [f for f in os.listdir ( folderPath ) if os.path.isfile ( os.path.join(folderPath , f ))]

for image in imageList:
	print (datetime.fromtimestamp(os.path.getmtime ( folderPath + "/" + image )).strftime("%m/%Y") )
	folderName = (datetime.fromtimestamp(os.path.getctime ( folderPath + "/" + image)).strftime("%m:%Y"))
	newPath = os.path.join ( destinationPath , folderName )
	if not os.path.exists ( newPath ):
		os.makedirs ( newPath )
		print ( "Directory " , newPath , " created ")
	else:
		print ( "Directory " , newPath , " already exists." )

	oldImagePath = os.path.join ( folderPath , image)
	newImagePath = os.path.join ( newPath , image ) 

#	shutil.move ( oldImagePath , newImagePath )
	shutil.copy2 ( oldImagePath , newImagePath ) 




