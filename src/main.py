from lxml import etree
from io import StringIO
import os




def validate_fsa029(sample_path, schema_folder):
    #locating main schema file
    schema_paths = os.listdir(schema_folder)
    for path in schema_paths:
        if "FSA029-Schema.xsd" in path:
            fsa_schema_path = schema_folder + '/' + path
            
            
    #formulating schema object       
    with open(fsa_schema_path) as schema_file:
        fsa_schema_doc = etree.parse(schema_file)
    fsa_schema = etree.XMLSchema(fsa_schema_doc)
     
     
    #forming a xml object   
    with open(sample_path) as sample_file:
        sample_text = etree.parse(sample_file)
    
    
            
    try:
        #if data conforms to schema, then print a success message and return True
        if fsa_schema.validate(sample_text):
            print("The data and schema match")
            return True
        else:
            #else statement will causes exception to raise
            fsa_schema.assertValid(sample_text)
    #return failure message and if validation fails
    except etree.DocumentInvalid as invalid_error:
        print("The data and schema do not match")
        raise invalid_error
    #catch other errors
    except Exception as error:
        print("There has been an error")
        raise error
        
        
        
    
    

    
if __name__ == "__main__":
    sample_valid = "data/FSA029-Sample-Valid.xml"
    sample_full = "data/FSA029-Sample-Full.xml"
    schema_folder = "CommonTypes/v14"
    
    
    print(validate_fsa029(sample_valid, schema_folder))
    #print(validate_fsa029(sample_full, schema_folder))