#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 09:13:35 2019

@author: rohittalukdar
"""

#!/usr/bin/python3
import urllib
import csv
import requests
import reader
import prettytable

csv_url="https://raw.githubusercontent.com/trohit/prettytables/master/data.csv"

def bytes_from_str(my_str):
    as_bytes = str.encode(my_str)
    return as_bytes

def str_from_bytes(my_bytes):
    as_str = my_bytes.decode()
    return as_str

def get_pretty_table_from_url(csv_url):
    pt = prettytable.PrettyTable()
    response = urllib.request.urlopen(csv_url)
    line_count = 0
    for line_bytes in response:
        line_count = line_count + 1
        #print("processing line " + str(line_count))
        #print(line_bytes.decode().strip().split(','))
        if line_count == 1:
            hdr_bytes = line_bytes
            hdr_ll_str = hdr_bytes.decode().strip().split(',')
            new_hdr = [z.replace('"','') for z in hdr_ll_str]
            print(new_hdr)
            pt.field_names = new_hdr 
        else:
            row_bytes = line_bytes
            row_ll_str = row_bytes.decode().strip().split(',')
            new_row = [z.replace('"','') for z in row_ll_str]
            pt.add_row(new_row)
    return pt        
    
if __name__ == "__main__":
    print("******start*****")
    print(get_pretty_table_from_url(csv_url))
    print("~~~~~~end~~~~~~")
    
