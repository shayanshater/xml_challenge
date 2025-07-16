from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import xmlschema

sample_valid = "data/sample_data/FSA029-Sample-Valid.xml"
schema = "data/FSA029-Schema.xsd"

def read_fsa029(filepath,schema):
    xsd  = xmlschema.XMLSchema(schema)
    
    if xsd.validate(filepath):
        print("valid")
    else:
        print("not")
    
    
    
    
    
    
read_fsa029(sample_valid, schema)