#!/usr/bin/env python
import argparse
import os,sys,shutil
sdk_root = "C:/Nokia/Devices/Nokia_SDK_2_0_Java"
pj = os.path.join

class SdkControl:
	def __init__(self, sdk_root):
		self.root = sdk_root
		self.fsroot = pj(sdk_root, "bin/storage/2000")

ctr = SdkControl(sdk_root)

def reset_cmd(args):
	print "reset",args
	assert os.path.isdir(ctr.fsroot)
	print "Nuking", ctr.fsroot
	shutil.rmtree(ctr.fsroot)
	
def emu_cmd(args):
	print "Launch emulator"
	os.startfile(pj(ctr.root, "bin/emulator.exe"))


def handle_args():

	parser = argparse.ArgumentParser(description='Operate Nokia JME SDK')
	subparsers = parser.add_subparsers(help='sub-command help', dest="subparser_name")
	parser_a = subparsers.add_parser('reset', 
		help='Reset the file system (factory reset)')
	#parser_a.set_defaults(func=reset_cmd)
	pb = subparsers.add_parser('emu', 
		help='Launch emulator')

	opts = parser.parse_args(sys.argv[1:])
	sp = opts.subparser_name

	if sp == 'reset':
		reset_cmd(opts)
	if sp == 'emu':
		emu_cmd(opts)



	print opts



	
handle_args()

assert os.path.isdir(sdk_root)

