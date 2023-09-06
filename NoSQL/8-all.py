#!/usr/bin/env python3
'''pymongo list'''



def list_all(mongo_collection)-> list:
    '''list all elements in a collection'''
    
    return[document for document in mongo_collection.find()]
