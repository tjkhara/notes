# This allows us to upload pictures

import os
from PIL import Image
from flask import url_for, current_app

def add_profile_pic(pic_upload, username):
	filename = pic_upload.filename # The picture name becomes the file name
	# "mypicture.jpg"
	# grab the jpg - this will tell us if it is a jpg or png
	ext_type = filename.split('.')[-1]
	# storage filename
	# This will produce something like tkhara.jpg
	storage_filename = str(username) + '.' + ext_type

	filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)

	output_size = (200,200)

	pic = Image.open(pic_upload)

	# thumbnail allows you to squeese a pic into a certain size
	pic.thumbnail(output_size)

	pic.save(filepath)

	return storage_filename