#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get the tags of a S3 bucket
- Info   : Get the tags of a S3 bucket
            * 101-s3-aws
"""

import boto

def tags(name):
   bucket = conn.get_bucket(name)
   tag = bucket.get_tags()
   print tag.to_xml()

if __name__ == "__main__":
   conn = boto.connect_s3()
   bucketname = "101-s3-aws"
   tags(bucketname)
