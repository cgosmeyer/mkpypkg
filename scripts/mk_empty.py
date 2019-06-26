#!/usr/bin/env python

""" Creates empty Python package.

Authors:
	
	 C.M. Gosmeyer
"""

import argparse

from mkpypkg.mkpypkg import mkpypkg


def parse_args():
    """ Parses command line arguments.
    """
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--n', dest='pkg_name',
        action='store', required=True,
        help="Name of the package.")
    parser.add_argument('--l', dest='pkg_loc', default='',
        action='store', required=False,
        help="Location of the package. Defaults to current location.") 

    args = parser.parse_args()
     
    return args

if __name__=='__main__':
	args = parse_args()

	mkpypkg(args.pkg_name, args.pkg_loc)