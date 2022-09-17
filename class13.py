#!/usr/bin/env python3
#Script Name    Python Requests Library
#Author      sujan thapa magar
#Date of last revision  09/15/2022


import requests

desURL=""

desURL = input("Please enter a URL of your choice:")

httpmeth = input("Please select a HTTP method of the following options: get, post, put, delete. head, patch, options:")

if httpmeth == 'get':
        method = requests.get
        print(requests.get)
elif httpmeth == 'post':
        method = requests.post
        print(requests.post)
elif httpmeth == 'put':
        method = requests.put
        print(requests.put)
elif httpmeth == 'delete':
        method = requests.delete
        print(requests.delete)
elif httpmeth == 'head':
        method = requests.head
        print(requests.head)
elif httpmeth == 'patch':
        method = requests.patch
        print(requests.patch)
elif httpmeth == 'options':
        method =requests.options
        print(requests.options) 
else:
    print("invalid selection; a get request has been selected")
    method = requests.get
    print(requests.get)
