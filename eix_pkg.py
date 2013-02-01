#!/usr/bin/python

import sys, os, subprocess
from termcolor import colored, cprint

if len(sys.argv) == 1:
  print("Null argument", file=sys.stderr)
  sys.exit(1)

def pfn(pkg_name):
  pkg_full_name = ''
  try:
    subprocess.check_call(r"FORMAT='<category>/<name>\n' eix -e %s > /tmp/eix_pfn_file" % pkg_name, shell=True)
  except subprocess.CalledProcessError:
    print(colored('Package not found!!', 'red'))
    os.remove('/tmp/eix_pfn_file')
    sys.exit(1)
  else:
    eix_pfn_file_lines = len(open('/tmp/eix_pfn_file', 'r').readlines())
    eix_pfn_file = open('/tmp/eix_pfn_file', 'r')
    if eix_pfn_file_lines > 1:
      print(colored('Too many results:', 'yellow'))
      while eix_pfn_file_lines > 1:
        pkg_full_name_raw = eix_pfn_file.readline()
        print(pkg_full_name_raw.rstrip())
        eix_pfn_file_lines = eix_pfn_file_lines - 1
      print(colored('Please, add package category to request', 'yellow'))
      eix_pfn_file.close
      os.remove('/tmp/eix_pfn_file')
      sys.exit(1)    
    else:
      pkg_full_name_raw = eix_pfn_file.readline()
      pkg_full_name = pkg_full_name_raw.rstrip()
      eix_pfn_file.close
      os.remove('/tmp/eix_pfn_file')
  return pkg_full_name  

def pver_inst(pkg_name):
  pkg_pver_inst = ''
  try:
    eix_exec = subprocess.check_call(r"eix -eI %s --format '<installedversions:VERSION>' > /tmp/eix_pver_inst_file" % pkg_name, shell=True)
  except subprocess.CalledProcessError:
    print(colored('Package not found!!', 'red'))
    os.remove('/tmp/eix_pver_inst_file')
    sys.exit(1)
  else:
    eix_pver_inst_file = open('/tmp/eix_pver_inst_file', 'r')
    pkg_pver_inst_raw = eix_pver_inst_file.readline()
    pkg_pver_inst = pkg_pver_inst_raw.rstrip()
    eix_pver_inst_file.close
    os.remove('/tmp/eix_pver_inst_file')
  return pkg_pver_inst
  
  
  
  

  
  