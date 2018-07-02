# PMIDtoAbstract
Program to grab plain text abstracts from NCBI using a file of PMIDs.  This should be used with less than 200 PMIDs as it uses HTTP GET and that what NCBI asks.  This program was written for Python 2.7, so it likely will not work for Python 3+.  
It will also put DOIs and PMIDs for each article into a seperate file if you want.

## DEPENDENCIES

The Requests package is needed to run this.  Requests can be found at http://docs.python-requests.org/en/master/

## USAGE

To get only the abstracts, use the following:

python requestNCBI.py fileWithPMIDs 0

To get the abstracts with IDs parsed out, use the following command:

python requestNCBI.py fileWithPMIDs 1
