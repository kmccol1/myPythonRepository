import os
import os.path
import shutil
from datetime import datetime
from os.path import getmtime

folder_path = "/home/user/Desktop/Source"
destination = "/home/user/Desktop/Destination"

#file_path = folder_path + "/" + image
images = [f for f in os.listdir ( folder_path ) if os.path.isfile ( os.path.join(folder_path , f ))]

for image in images:
	print (datetime.fromtimestamp(os.path.getmtime ( folder_path + "/" + image )).strftime("%m/%Y") )
	folder_name = (datetime.fromtimestamp(os.path.getctime ( folder_path + "/" + image)).strftime("%m:%Y"))
	new_path = os.path.join ( destination , folder_name )
	if not os.path.exists ( new_path ):
		os.makedirs ( new_path )
		print ( "Directory " , new_path , " created ")
	else:
		print ( "Directory " , new_path , " already exists." )

	old_image_path = os.path.join ( folder_path , image)
	new_image_path = os.path.join ( new_path , image ) 

#	shutil.move ( old_image_path , new_image_path )
	shutil.copy2 ( old_image_path , new_image_path ) 

arr= os.listdir ( folder_path )
print (arr)



