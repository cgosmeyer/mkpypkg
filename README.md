# mkpypkg

Initializes an empty Python package or reorganizes existing directory into Python package.

Assumptions:

	MIT LICENSE

	All Python for .gitignore

## Installation

	1. Run setup.py:

		python setup.py develop

	2. Modify the mkpypkg_config with your information. For example:
	
	"""
	mkpypkg_loc = "/full/path/to/mkpypkg"
	given_name = "Isaac"
	family_name = "Newton"
	orcid = "optional orcid so you can get cited properly"
	github_user = "inewton"
	"""

## To make an empty Python package

	1. Decide where you want your new package to be created and what to name it.

	2. Run `/scripts/mk_empty.py`:

		python mk_empty.py --n 'your-pkg' --l '/path/to/your/pkg'

	3. Now in that location you should see the following structure

	your-pkg/
		your-pkg/
			__init__.py
		docs/
		notebooks/
		scripts/
		.gitignore
		CITATION.cff
		LICENSE
		README.md
		setup.py

## To reorganize an existing directory into Python package

	1. Locate the directory of Python files you wish to organize into a package. 
	The package name will assumed to be that of the base directory.

	2. Run `/scripts/mk_reorg.py`:

		python mk_reorg.py --l '/path/to/your/dir'

	3. The organization should match that of the example above. 
	This script is only meant to get you part-way there, so be sure to check 
	that all the files are where you expect!

## To retain a nice Python package structure

	1. Write your modules in the subdirectory `your-dir`. *No scripts (command-
	line run Python files) should be in this subdirectory!* This subdirectory can
	have sub-sub-directories (and all levels need to contain an `__init__.py`!).
	Use whatever organization works best for your code. 

	For instance, the following structure 

		your-dir/your-dir/cool-utilities/stuff.py

	will result with the following module-level import statement

		from your-dir.cool-utilities import stuff

	2. All Python files that are not meant to have importable functions and 
	classes, but instead are the ones importing from your package's other Python 
	files (i.e., scripts) should be stored at the top-level or in a subdirectory 
	named something like `scripts`.  Likewise, example files and docs need to be
	in directories at the top level. You might end up with a package look like 
	this:

	your-dir/
		your-dir/
			__init__.py
		example_data/
			example.txt
		docs/
			sphinx-stuff.rst
		tests/
			test.py
		scripts/
			run_this_thing.py
		setup.py
		.gitignore
		README.md
		LICENSE
		CITATION.cff



