#!/usr/bin/python
 
import os, sys

def sovp(file_name, pkg_name):
  sovp_count = 0
  file_name_open = open(file_name, 'r')
  file_line = file_name_open.readline()
  while file_line != '':
    if pkg_name in file_line:
      sovp_count = sovp_count + 1
    file_line = file_name_open.readline()
  return sovp_count
