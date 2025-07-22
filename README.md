# XML Challenge

In this document, we will walk through setting up, testing and running the xml_challenge repo.


## Setup
To begin, open your terminal(bash) and change directory to your desired location. e.g:

```bash
cd Desktop/Code
```

This will take you to the `Code` folder inside of Desktop. Once you are in the desired location, clone this repo using

```bash
git clone https://github.com/shayanshater/xml_challenge
```

Then change directory into this repo:

```bash
cd xml_challenge
```

And we are ready to setup the python requirements (make sure you python installed)! Start by creating a virtual environment and installing the requirements into it


```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Once all of the preceding steps are done, We are ready to move and test the integrity of the script.

## Testing

To check the integrity of the script, there is a series of test which the script must pass in order for its behavior to be as desired. We start by exporting the python path using:

```bash
export PYTHONPATH=$(pwd)
```

Then we are ready to run the tests. This is done with the following:

```bash
pytest -vv --testdox
```

A successful output looks like:

```
test/test_main.py                                                                                                                                                                                                            
Class for tests that check the
integrity of the schema files.
 ✓ A test that checks if both of the FSA029
   and CommontTypes schema files are in
   the directory.
 ✓ A test that checks if the contents
   of the schema files are unchanged after
   running the validation script.
                                                                                                                                                                                                           
Class for checking that the script
passes the valid sample file
 ✓ A test to check if the valid
   sample data conforms to the given
   schema as it should
 ✓ A test to check that the full sample data raises an exception,
   due to it having multiple entries into the capitals section.


============================================================================================ 4 passed in 0.09s ============================================================================================
```

## Using the main Script

The main script is located in <code>src/main.py</code>. The main useable component is a function called validate_fsa029. This function inputs a schema folder and sample data, and outputs either a success or error message if the data is valid or not.

The script is independent of the schema folder location, so this means that it can be placed anywhere within this repo and the script will work. What is important is that the correct path of the schema folder and sample data is passed to the function.

To use this script/function, run the following:

```bash
python src/main.py
```


There are two cases in this script, The valid and invalid cases. The valid case is the first case on line 57. To see the invalid case, uncomment line 58 and run the script. This should raise an exception like the following:

```bash
lxml.etree.DocumentInvalid: Element '{urn:fsa-gov-uk:MER:FSA029:4}PartnershipsSoleTraders': This element is not expected., line 102
```

This points to where the error is located in the xml file.



## The Extra Mile

What causes it to fail schema validation? Why do you think the regulator has
included a valid file in their examples?

- The failure of the FSA029-Sample-Full.xml file to conform to the schema is caused by the Capital segment.
- The Capital segment takes a choice of three entries. IncorporatedEntities, PartnershipsSoleTraders or LLPs. This means that only one of these entries can be chosen to be under the capitals section.
- The full sample data has all three of the options under the Capital segment, and this is the cause of the error.

- The regulator has included a valid file in their examples so that a user can verify the behavior of the schema. When developing tests regarding this schema, a developer can easily develop a test which ensures that the schema works for valid data samples. It also shows that the schema behaves as is expected and is not faulty.


How would you fix the file to pass the schema validation?

- One way to fix the full sample data to pass validation would be to only choose one of the three sections under Capital (IncorporatedEntities, PartnershipsSoleTraders or LLPs) and delete the rest. This would respect the choice argument given to the Capital section and cause this error to be fixed.

- However, if you may wish to keep all of the data and redesign the schema, this could be a better option to keep all of the data instead of deleting it. It can be simply done by replacing the `<choice>` block with a `<sequence>` block and giving each of the three options the arguments of `< ... minOccurs="0" maxOccurs="1">` but giving IncorporatedEntities `< ... minOccurs="1" maxOccurs="1">`.  This makes sure that you can have maximum three unique inputs, with IncorporatedEntities being a must. 

- Both methods make the full data valid. However it depends on if one may wish to edit the sample data and delete inputs, or edit the schema and keep the inputs. 

Why do you think the regulator has included an invalid file in their examples?

- By providing a passing and failing data set, it helps developers with testing and understanding schemas. A failing data set helped this situation by giving a specific error and showing where the data set failed. This helps developers to understand the different types of errors and check the validity of the schema.



