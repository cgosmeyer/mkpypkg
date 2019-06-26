#!/usr/bin/env python

""" Creates empty Python package.

Authors:
	
	 C.M. Gosmeyer
"""

import argparse

from mkpypkg.mkpypkg import reorgpkg


def parse_args():
    """ Parses command line arguments.
    """
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--l', dest='pkg_loc', default='',
        action='store', required=False,
        help="Location of the package. Defaults to current location.") 

    args = parser.parse_args()
     
    return args

if __name__=='__main__':
	args = parse_args()

	reorgpkg(args.pkg_loc)