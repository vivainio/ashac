#!/usr/bin/env python
import argparse
import os,sys,shutil
import mglob

sdk_root = "C:/Nokia/Devices/Nokia_SDK_2_0_Java"
pj = os.path.join

class SdkControl:
	def __init__(self, sdk_root):
		self.root = sdk_root

		self.storage = pj(sdk_root, "bin/storage")

	def storages(self):
		return [pj(self.storage, b) for b in os.listdir(self.storage) if b.isdigit()]

	def get_fs(self):
		s = self.storages()
		if not s:
			print "Error: no emulators initialized"
			return None
		return s[0]




ctr = SdkControl(sdk_root)

def killemu():
	os.system("taskkill /im Nokia_SDK_2_0_Java_em.exe /f")



def reset_cmd(args):
	print "reset",args
	storages = [pj(ctr.storage, b) for b in os.listdir(ctr.storage) if b.isdigit()]
	print "Storages found:", storages
	killemu()
	for s in storages:
		print "Nuking",	s
		shutil.rmtree(s)
	
def emu_cmd(args):
	print "Launch emulator"
	os.startfile(pj(ctr.root, "bin/emulator.exe"))

def kill_cmd(args):
	print "Kill emulator"
	killemu()

def open_cmd(args):
	os.startfile(ctr.get_fs())

def myapps_cmd(args):
	print "myapps_cmd",args
	files = mglob.expand(args.file)
	tg = pj(ctr.get_fs(), "C/predefjava/predefcollections")

	print "Copying",files, "to",tg
	for f in files:
		shutil.copy(f, tg)




def handle_args():

	parser = argparse.ArgumentParser(description='Operate Nokia JME SDK')
	subparsers = parser.add_subparsers(help='sub-command help', dest="subparser_name")
	parser_a = subparsers.add_parser('reset', 
		help='Reset the file system (factory reset)')
	#parser_a.set_defaults(func=reset_cmd)
	pb = subparsers.add_parser('emu', 
		help='Launch emulator')

	pc = subparsers.add_parser('kill', 
		help = "Kill emulator")

	pc = subparsers.add_parser('open', 
		help = "Open storage location in explorer")

	pd = subparsers.add_parser('myapps', 
		help = "Copy files to 'myapps' in emulator file system")

	pd.add_argument('file', type = str, nargs = "+")
	opts = parser.parse_args(sys.argv[1:])
	sp = opts.subparser_name

	if sp == 'reset':
		reset_cmd(opts)
	elif sp == 'emu':
		emu_cmd(opts)
	elif sp == 'kill':
		kill_cmd(opts)
	elif sp == 'open':
		open_cmd(opts)
	elif sp == 'myapps':
		myapps_cmd(opts)




	#print opts



	
handle_args()

assert os.path.isdir(sdk_root)

