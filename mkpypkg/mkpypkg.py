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
	os.mkdir(os.path.join(pkg_loc, pkg_name, 'docs'))
	os.mkdir(os.path.join(pkg_loc, pkg_name, 'notebooks'))
	os.mkdir(os.path.join(pkg_loc, pkg_name, 'scripts'))

	# Create __init__.py
	open(os.path.join(pkg_loc, pkg_name, pkg_name, '__init__.py'), 'a').close()

	# Create setup.py
	setup_name = os.path.join(pkg_loc, pkg_name, 'setup.py')
	shutil.copy2(os.path.join(mkpypkg_loc, 'setup.py'), setup_name)
	#edit_setup(setup_name)

	# Create empty README.md
	readme_name = os.path.join(pkg_loc, pkg_name, 'README.md')
	open(readme_name, 'a').close()
	edit_readme(readme_name, pkg_name)

	# Create filled MIT license
	shutil.copy2(os.path.join(mkpypkg_loc, 'LICENSE'), os.path.join(pkg_loc, pkg_name, 'LICENSE'))

	# Create filled .gitignore
	gitignore_name = os.path.join(pkg_loc, pkg_name, '.gitignore')
	shutil.copy2(os.path.join(mkpypkg_loc, '.gitignore'), gitignore_name)
	#edit_gitignore(gitignore_name)

	# Create template CITATION.cff
	citation_name = os.path.join(pkg_loc, pkg_name, 'CITATION.cff')
	shutil.copy2(os.path.join(mkpypkg_loc, 'CITATION.cff'), citation_name)
	#edit_citation(citation)

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

def edit_setup(setup):
	"""
	"""

def edit_citation(citation):
	"""
	"""

def edit_gitignore(gitignore):
	""" Edit to remove mkpypkg-specific lines.
	"""

def edit_readme(readme, pkg_name):
	"""
	"""
	with open(readme, 'a') as f:
		f.write('# {}\n'.format(pkg_name))
		f.write("\n")
		f.write('Useful things here about the `` package!\n'.format(pkg_name))
		f.write("\n")
		f.write('## Installation\n')
		f.write("\n")
		f.write('    Run setup.py:\n')
		f.write("\n")
		f.write('\t```\n')
		f.write('\tpython setup.py develop\n')
		f.write('\t```\n')



