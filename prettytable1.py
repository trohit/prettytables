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


def read_from_url_csv(csv_url):
    response = urllib.request.urlopen(csv_url)
    cr = csv.reader(response)
    print(type(cr))
    print(dir(cr))
    r = requests.get(csv_url)
    text = r.iter_lines()
    reader = csv.reader(text, delimiter=',')
    print(type(cr))
    return cr

def read_from_url(url):
    dd = urllib.request.urlopen(csv_url)
    for l in dd:
        pp = l.strip().split(',')
        print(l)

def pretty_print_table_from_file(csv_file):    
    # from url
    # http://winterolympicsmedals.com/medals.csv
    # as a file
    with open(csv_file, "r") as fp: 
        x = prettytable.from_csv(fp)    
    print(x)
    
if __name__ == "__main__":
    print("******start*****")
    rr = read_from_url_csv(csv_url)
    print("~~~~~~end~~~~~~")
    
    #csv_file = "/Users/rohittalukdar/data/medals.csv"
    #pretty_print_table_from_file(csv_file)
    #print("~~~~~~ the end~~~~~~")
    
