import requests, sys

pmid='id='
db='db=pubmed&'	#We want to query the pubmed database
	
with open (sys.argv[1], 'r') as file:	#concatenate all of the pmids
	for x in file:
		pmid=pmid+str(x.strip())+','

pmid=pmid[:-1]+'&'	#remove comma from the end of our pmid list

retmode='retmode=text&'	#ask for plain text
rettype='rettype=abstract'	#ask for the abstracts

#make the html request to ncbi
r = requests.get('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?'+db+pmid+retmode+rettype)

print r.status_code

#write the results from ncbi to a file.  encoding helps prevent characters from being changed
with open('abstracts', 'w+') as file:
	file.write(r.text.encode('utf-8'))

if sys.argv[2] == '1':

	DOI='N/A'
	count=1

	with open ('abstracts', 'r') as file:	#read from abstracts
		with open ('absDOI', 'w+') as file2:	#create a file specifically for abstracts where we don't find DOIs
			file2.write('Abstract\tDOI\tPMID'+'\n')
			for line in file:
				if 'DOI:' in line:	#DOIs are stored on separate lines, so we can check for a pattern to find them
					DOI=line.split(' ')[1].strip()
				elif 'PMID' in line:	#if we reach the PMID without finding a DOI
					file2.write(str(count)+'\t'+DOI+'\t'+line.split(' ')[1]+'\n')	#write the article info and the PMID to our no doi list
					count=count+1
					DOI='N/A'

