# PMIDtoAbstract
Program to grab abstracts from NCBI using a file of PMIDs.
It will also grab DOIs, or PMIDs in a separate file for articles without DOIs, for each article.

DEPENDENCIES
The Requests package is needed to run this.  Requests can be found at http://docs.python-requests.org/en/master/

COMMANDS
To get only the abstracts, use the following:
python requestNCBI.py <file with PMIDs> 0
To get the abstracts with DOIs parsed out, use the following command:
python requestNCBI.py <file with PMIDs> 1
