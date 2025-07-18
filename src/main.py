from lxml import etree
import os




def validate_fsa029(sample_path, schema_folder):
    """
    This function takes a path for a schema folder and xml data,
    and checks if the xml data is valid under the schema. 
    If it is valid it returns a True value and success message, 
    but if it fails it returns a useful exception which highlights which part 
    of the xml document caused the error to rise.

    Args:
        sample_path (string): a path to the xml sample data that.
        schema_folder (string): a path to the directory which contains the schemas

    Raises:
        DocumentInvalid: Raises an exception which highlights the invalid part of the xml document.

    Returns:
        True: Returns True if the data is valid under the schema.
    """
    #locating main schema file
    schema_paths = os.listdir(schema_folder)
    for path in schema_paths:
        if "FSA029-Schema.xsd" in path:
            fsa_schema_path = schema_folder + '/' + path
            
            
    #formulating schema object       
    with open(fsa_schema_path) as fsa_schema_file:
        fsa_schema_doc = etree.parse(fsa_schema_file)
    fsa_schema = etree.XMLSchema(fsa_schema_doc)
     
     
    #forming a xml object   
    with open(sample_path) as sample_file:
        sample_xml = etree.parse(sample_file)
    
    
            
    try:
        #if data conforms to schema, then print a success message and return True
        if fsa_schema.validate(sample_xml):
            print("The data is valid.")
            return True
        else:
            #else statement will causes exception to raise
            fsa_schema.assertValid(sample_xml)
    #return failure message and if validation fails
    except etree.DocumentInvalid as invalid_error:
        print("The data is invalid.")
        raise invalid_error
        
        
        
    
    

    
if __name__ == "__main__":
    sample_valid = "data/FSA029-Sample-Valid.xml"
    sample_full = "data/FSA029-Sample-Full.xml"
    schema_folder = "CommonTypes/v14"
    
    
    print(validate_fsa029(sample_valid, schema_folder))
    #print(validate_fsa029(sample_full, schema_folder))