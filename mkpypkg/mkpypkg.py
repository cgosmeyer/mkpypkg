"""
"""

import os
import shutil

from mkpypkg_config import mkpypkg_loc #, name, orcid

def mkpypkg(pkg_name, pkg_loc):
	"""
	"""
	# Create package directory structure.
	os.mkdir(os.path.join(pkg_loc, pkg_name))
	os.mkdir(os.path.join(pkg_loc, pkg_name, pkg_name))
	os.mkdir(os.path.join(pkg_loc, 'docs'))
	os.mkdir(os.path.join(pkg_loc, 'notebooks'))
	os.mkdir(os.path.join(pkg_loc, 'scripts'))

	# Create __init__.py
	open(os.path.join(pkg_loc, pkg_name, pkg_name, '__init__.py'), 'a').close()

	# Create setup.py
	shutil.copy2(os.path.join(mkpypkg_loc, 'setup.py'), os.path.join(pkg_loc, pkg_name, 'setup.py'))
	# edit setup.py

	# Create empty README.md
	open(os.path.join(pkg_loc, pkg_name, 'README.md'), 'a').close()

	# Create filled MIT license
	shutil.copy2(os.path.join(mkpypkg_loc, 'LICENSE'), os.path.join(pkg_loc, pkg_name, 'LICENSE'))

	# Create filled .gitignore
	shutil.copy2(os.path.join(mkpypkg_loc, '.gitignore'), os.path.join(pkg_loc, pkg_name, '.gitignore'))
	# Edit to remove mkpypkg-specific lines.

	# Create template CITATION.cff
	shutil.copy2(os.path.join(mkpypkg_loc, 'CITATION.cff'), os.path.join(pkg_loc, pkg_name, 'CITATION.cff'))
	# edit CITATION.cff

	# End with message on how to push new package to GitHub/Lab
	print("COMPLETE!")
	print("")
	print("Open your new files to check all is correct and modify if necessary. Add info to README.md.")
	print("")
	print("To add local git tracking:")
	print("		git init")
	print("		git add *")
	print("		git commit 'initial commit'")
	print("")
	print("To add to GitHub/Lab: ")
	print("1. Go to your account.")
	print("2. Click 'Create repository' button and ignore all offers to create README, etc (you have them already).")
	print("3. Back on command line in your new project, follow the similar instructions GitHub/Lab gives you:")
	print(" 	git remote add origin git@github.com:username/{}".format(pkg_name))
	print("		git push origin master")
	print("4. Check GitHub/Lab for your new commits.")
