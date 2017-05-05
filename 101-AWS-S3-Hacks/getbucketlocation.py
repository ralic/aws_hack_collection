#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the Location of the s3 bucket
- Info   : The bucket eu-west-1.101-s3-aws is in AWS region eu-west-1
           Did you know if you do not specify the host it still works ?????? Yes it works.
"""

import boto

def searchabucket():
   bucket = conn.lookup("eu-west-1.101-s3-aws")
   print bucket.get_location()

if __name__ == "__main__":
   conn = boto.connect_s3(host='s3-eu-west-1.amazonaws.com')
   searchabucket()
