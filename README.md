# mkpypkg
Initializes an empty Python package to my own tastes.

The LICENSE assumes MIT. 

The .gitignore assumes all Python.

## Installation

	1. Run setup.py:

		python setup.py develop

	2. Modify the mkpypkg_config with your information.

## To make an empty package

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

## To retain a nice Python package structure

	1. Write your modules in the subdirectory `your-dir`. *No scripts (command-line run Python files) should be in this subdirectory!* This subdirectory can have sub-sub-directories (and all levels need to contain an `__init__.py`!).  Use whatever organization works best for your code. 

	For instance, the following structure 

		your-dir/your-dir/cool-utilities/stuff.py

	will result with the following module-level import statement

		from your-dir.cool-utilities import stuff

	2. All Python files that are not meant to have importable functions and classes, but instead are the ones importing from your package's other Python files (i.e., scripts) should be stored at the top-level or in a subdirectory named something like `scripts`.  Likewise, example files and docs need to be in directories at the top level. You might end up with a package look like this:

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

## To make a package from an existing Python project


