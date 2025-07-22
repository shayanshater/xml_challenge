from src.main import validate_fsa029
import os
import pytest
from lxml import etree




@pytest.fixture()
def sample_file_paths():
    sample_valid_path = "data/FSA029-Sample-Valid.xml"
    sample_full_path = "data/FSA029-Sample-Full.xml"
    
    
    return [sample_valid_path, sample_full_path]
    
    
@pytest.mark.describe("""Class for tests that check the 
                      integrity of the schema files.""")    
class TestSchemaDocs:
    @pytest.mark.it("""A test that checks if both of the FSA029 
                    and CommontTypes schema files are in 
                    the directory.""")
    def test_schema_files_are_in_same_directory(self):
        
        schema_files = os.listdir("Schemas")
        
        fsa_schema_file_name = "FSA029-Schema.xsd"
        common_types_file_name  = "CommonTypes-Schema.xsd"
        
        assert fsa_schema_file_name in schema_files
        assert common_types_file_name in schema_files
        
        
    @pytest.mark.it("""A test that checks if the contents 
                    of the schema files are unchanged after
                    running the validation script.""")
    def test_schema_contents_are_unchanged(self, sample_file_paths):
        with open("Schemas/FSA029-Schema.xsd", 'r') as fsa_schema_file:
            pre_run_fsa_schema_text = fsa_schema_file.read()
            
        with open("Schemas/CommonTypes-Schema.xsd", 'r') as commontypes_schema_file:
            pre_run_commontypes_schema_text = commontypes_schema_file.read()
            
            
        #run the script
        schema_folder = "Schemas"
        validate_fsa029(sample_file_paths[0], schema_folder)
        
        
        with open("Schemas/FSA029-Schema.xsd", 'r') as fsa_schema_file:
            post_run_fsa_schema_text = fsa_schema_file.read()
            
        with open("Schemas/CommonTypes-Schema.xsd", 'r') as commontypes_schema_file:
            post_run_commontypes_schema_text = commontypes_schema_file.read()
            
            
        #assert that schema contents have not changed
        assert pre_run_commontypes_schema_text == post_run_commontypes_schema_text
        assert pre_run_fsa_schema_text == post_run_fsa_schema_text
        
    def test_script_works_regardless_of_schema_file_paths(self, sample_file_paths):
        schema_folder = "Schemas"
        new_folder_path = "some/random/folder"
        os.makedirs(new_folder_path)
        
        os.rename(schema_folder + "/CommonTypes-Schema.xsd", new_folder_path+ "/CommonTypes-Schema.xsd")
        os.rename(schema_folder + "/FSA029-Schema.xsd", new_folder_path+ "/FSA029-Schema.xsd")
        
        
        assert validate_fsa029(sample_file_paths[0], new_folder_path)
        
        assert os.path.exists(new_folder_path+ "/CommonTypes-Schema.xsd")
        assert os.path.exists(new_folder_path+ "/FSA029-Schema.xsd")
        
        os.rename(new_folder_path+ "/CommonTypes-Schema.xsd", schema_folder + "/CommonTypes-Schema.xsd")
        os.rename(new_folder_path+ "/FSA029-Schema.xsd", schema_folder + "/FSA029-Schema.xsd")
        
        os.removedirs(new_folder_path)
            
            
            
        
            
@pytest.mark.describe("""Class for checking that the script 
                      passes the valid sample file""")
class TestSampleData:
    @pytest.mark.it("""A test to check if the valid 
                    sample data conforms to the given 
                    schema as it should""")
    def test_valid_sample_data(self, sample_file_paths):
        schema_folder = "Schemas"
        result = validate_fsa029(sample_file_paths[0], schema_folder)
        
        assert result == True
    
    
    @pytest.mark.it("""
                    A test to check that the full sample data raises an exception,
                    due to it having multiple entries into the capitals section.
                    """)
    def test_full_sample_data_raises_exception(self, sample_file_paths):
        schema_folder = "Schemas"
        
        
        with pytest.raises(etree.DocumentInvalid):
            result = validate_fsa029(sample_file_paths[1], schema_folder)
