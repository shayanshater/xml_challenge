# XML Challenge

In this document, we will walk through setting up, testing and running the xml_challenge repo.


## Setup

To begin, open your terminal and change directory to your desired location. e.g: 

```bash
cd Desktop/Code
```

This will take you to the Code folder inside of Desktop. Once you are in the desired location, clone this repo using

```bash
git clone https://github.com/shayanshater/xml_challenge
```

Then change directory into this repo:

```bash
cd xml_challenge
```

And we are ready to setup the python requirements! Start by creating a virtual environment and installing the requirements into it


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

With a successful output that looks like:

```bash
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

The main script is located in <code>src/main.py</code>. The main useable component is a function called validate_fsa029. This function inputs a schema folder and sample data, and outputs either a success or error message.

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



