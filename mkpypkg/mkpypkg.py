"""
"""

import datetime
import os
import shutil

from mkpypkg_config import mkpypkg_loc, given_name, family_name, orcid, github_user

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
	open(setup_name, 'a').close()
	edit_setup(setup_name, pkg_name)

	# Create empty README.md
	readme_name = os.path.join(pkg_loc, pkg_name, 'README.md')
	open(readme_name, 'a').close()
	edit_readme(readme_name, pkg_name)

	# Create filled MIT license
	license_name = os.path.join(pkg_loc, pkg_name, 'LICENSE')
	shutil.copy2(os.path.join(mkpypkg_loc, 'LICENSE'), license_name)
	edit_license(license_name)

	# Create filled .gitignore
	gitignore_name = os.path.join(pkg_loc, pkg_name, '.gitignore')
	shutil.copy2(os.path.join(mkpypkg_loc, '.gitignore'), gitignore_name)
	edit_gitignore(gitignore_name)

	# Create template CITATION.cff
	citation_name = os.path.join(pkg_loc, pkg_name, 'CITATION.cff')
	open(citation_name, 'a').close()
	edit_citation(citation_name, pkg_name)

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



def edit_citation(citation, pkg_name):
	"""
	"""
	with open(citation, 'a') as f:
		f.write("cff-version: 1.0.3\n")
		f.write("message: If you use this software, please cite it as below.\n")
		f.write("authors:\n")
		f.write("  - family-names: {}\n".format(family_name))
		f.write("    given-names: {}\n".format(given_name))
		f.write("    orcid: https://orcid.org/{}\n".format(orcid))
		f.write("title: {}\n".format(pkg_name.upper()))
		f.write("version: 1.0\n")
		f.write("doi: N/A\n")
		f.write("date-released: N/A\n")

def edit_gitignore(gitignore):
	""" Edit to remove mkpypkg-specific lines.
	"""
	gittemp = os.path.join(mkpypkg_loc, 'temp')
	shutil.move(gitignore, gittemp)
	f = open(gitignore, 'a')
	with open(gittemp, 'r') as ftemp:
		for line in ftemp.readlines():
			if 'mkpypkg' not in line:
				f.write(line)
	f.close()
	os.remove(gittemp)

def edit_license(license):
	"""
	"""
	year = datetime.datetime.now().year
	licensetemp = os.path.join(mkpypkg_loc, 'temp')
	shutil.move(license, licensetemp)
	f = open(license, 'a')
	with open(licensetemp, 'r') as ftemp:
		for line in ftemp.readlines():
			if 'Copyright' in line:
				f.write("Copyright (c) {} {}. {}\n".format(year, given_name[0], family_name))
			else:
				f.write(line)
	f.close()
	os.remove(licensetemp)	

def edit_readme(readme, pkg_name):
	"""
	"""
	with open(readme, 'a') as f:
		f.write('# {}\n'.format(pkg_name))
		f.write("\n")
		f.write('Useful things here about the `{}` package!\n'.format(pkg_name))
		f.write("\n")
		f.write('## Installation\n')
		f.write("\n")
		f.write('    Run setup.py:\n')
		f.write("\n")
		f.write('\tpython setup.py develop\n')
		f.write("\n")

def edit_setup(setup, pkg_name):
	"""
	"""
	with open(setup, 'a') as f:
		f.write("#!/usr/bin/env python\n")
		f.write("\n")
		f.write("from setuptools import find_packages\n")
		f.write("from setuptools import setup\n")
		f.write("\n")
		f.write("setup(name = '{}',\n".format(pkg_name))
		f.write("      description = 'Describe this package!',\n")
		f.write("      author = '{} {}',\n".format(given_name, family_name))
		f.write("      url = 'https://github.com/{}/{}',\n".format(github_user, pkg_name))
		f.write("      packages = find_packages())\n")

