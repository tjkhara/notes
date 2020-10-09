# How to clone a specific commit from a repo?

	# make a new blank repository in the current directory
	git init

	# add a remote
	git remote add origin url://to/source/repository

	
	git remote add origin https://github.com/miguelgrinberg/microblog.git

	# fetch a commit (or branch or tag) of interest
	# Note: the full history up to this commit will be retrieved unless 
	#       you limit it with '--depth=...' or '--shallow-since=...'
	git fetch origin <sha1-of-commit-of-interest>

	# reset this repository's master branch to the commit of interest
	git reset --hard FETCH_HEAD

# How to get a zip file from a certain SHA?

	https://github.com/miguelgrinberg/microblog/archive/98e909b108236df945d8de0125f138426eb161fa.zip

Format is:

	https://github.com/{username}/{projectname}/archive/{sha}.zip