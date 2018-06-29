import requests, sys, re


token=sys.argv[1]	#APIKey for NCBI
pmid='id='
db='db=pubmed&'	#We want to query the pubmed database
	
with open (sys.argv[2], 'r') as file:	#concatenate all of the pmids
	for x in file:
		pmid=pmid+str(x.strip())+','

pmid=pmid[:-1]+'&'	#remove comma from the end and add & for the next variable


retmode='retmode=text&'	#ask for plain text
rettype='rettype=abstract'	#ask for the abstracts

#make the html request to ncbi
r = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'+db+pmid+retmode+rettype)

#write the results from ncbi to a file.  encoding helps prevent characters from being changed
with open('abstracts', 'w+') as file:
	file.write(r.text.encode('utf-8'))


DOIList=[]	#create a list to store the DOIs we find in the response from ncbi
regex=r"[0-9]*[.]{1}[\w ]*[.]{1}[\w ]*[;]{1}[\d]*[(]{1}[\d]*[)]{1}[:]{1}[\d-]*[.]{1}"	#regex pattern to match first line of a new abstract
doiCheck=False
articleInfo=''

with open ('abstracts', 'r') as file:	#read from abstracts
	with open ('absNoDOI', 'w+') as file2:	#create a file specifically for abstracts where we don't find DOIs
		for line in file:
			if 'DOI:' in line:	#DOIs are stored on separate lines, so we can check for a pattern to find them
				DOIList.append(line)
				doiCheck=True
			elif re.match(regex, line) != None and 'doi' not in line.lower():	#if we find a regex match and it doesn't have a DOI associated
				doiCheck=False	#set our doiCheck to false
				articleInfo=line	#record the info about the line
			if 'PMID' in line and doiCheck==False:	#if we reach the PMID without finding a DOI
				file2.write(articleInfo.strip()+'\t'+line.split(' ')[1]+'\n')	#write the article info and the PMID to our no doi list
				doiCheck=True

with open ('absDOI', 'w+') as file:	#write our doi list to a separate file
	for x in DOIList:
		file.write(x)	
