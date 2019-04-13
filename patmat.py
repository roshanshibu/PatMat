import csv
from nltk.tag.stanford import StanfordPOSTagger
from fysom import Fysom


#########################################################
#windows specific code
import os
java_path = "C:/Program Files/Java/jdk1.8.0_91/bin/java.exe"
os.environ['JAVAHOME'] = java_path
#############################################################

def SenToPhrase (tagged_sentence):
	fsm = Fysom({'initial': '0',                'events': [{'name': 'IN', 'src': '0', 'dst': '1'},{'name': 'NN', 'src': '1', 'dst': '3'},{'name': 'NNS', 'src': '1', 'dst': '3'},{'name': 'NNP', 'src': '1', 'dst': '3'},{'name': 'NNPS', 'src': '1', 'dst': '3'},{'name': 'DT', 'src': '1', 'dst': '2'},                {'name': 'NN', 'src': '2', 'dst': '3'},{'name': 'NNS', 'src': '2', 'dst': '3'},{'name': 'NNP', 'src': '2', 'dst': '3'},                {'name': 'NNPS', 'src': '2', 'dst': '3'},{'name': 'PRP$', 'src': '1', 'dst': '4'},{'name': 'PRP$', 'src': '2', 'dst': '4'},                {'name': 'JJ', 'src': '1', 'dst': '5'},{'name': 'JJ', 'src': '2', 'dst': '5'},{'name': 'JJR', 'src': '1', 'dst': '6'},                {'name': 'JJR', 'src': '2', 'dst': '6'},{'name': 'JJS', 'src': '1', 'dst': '7'},{'name': 'JJS', 'src': '2', 'dst': '7'},                {'name': 'NN', 'src': '5', 'dst': '3'},{'name': 'NN', 'src': '6', 'dst': '3'},{'name': 'NN', 'src': '7', 'dst': '3'},                {'name': 'NNS', 'src': '5', 'dst': '3'},{'name': 'NNS', 'src': '6', 'dst': '3'},{'name': 'NNS', 'src': '7', 'dst': '3'},                {'name': 'NNP', 'src': '5', 'dst': '3'},{'name': 'NNP', 'src': '6', 'dst': '3'},{'name': 'NNP', 'src': '7', 'dst': '3'},                {'name': 'NNPS', 'src': '5', 'dst': '3'},{'name': 'NNPS', 'src': '6', 'dst': '3'},{'name': 'NNPS', 'src': '7', 'dst': '3'},                {'name': 'PRP', 'src': '1', 'dst': '4'},{'name': 'PRP', 'src': '2', 'dst': '4'},{'name': 'NN', 'src': '4', 'dst': '3'},                {'name': 'NNS', 'src': '4', 'dst': '3'},{'name': 'NNP', 'src': '4', 'dst': '3'},{'name': 'NNPS', 'src': '4', 'dst': '3'},                {'name': 'TO', 'src': '0', 'dst': '1'},                {'name': 'MD', 'src': '0', 'dst': '8'},{'name': 'VB', 'src': '8', 'dst': '9'},{'name': 'VBD', 'src': '8', 'dst': '10'},                {'name': 'VBG', 'src': '8', 'dst': '11'},{'name': 'VBN', 'src': '8', 'dst': '12'},{'name': 'VBP', 'src': '8', 'dst': '13'},                {'name': 'VBZ', 'src': '8', 'dst': '14'},{'name': 'VB', 'src': '0', 'dst': '9'},{'name': 'VBD', 'src': '0', 'dst': '10'},                {'name': 'VBG', 'src': '0', 'dst': '11'},{'name': 'VBN', 'src': '0', 'dst': '12'},{'name': 'VBP', 'src': '0', 'dst': '13'},                {'name': 'VBZ', 'src': '0', 'dst': '14'},{'name': 'RB', 'src': '9', 'dst': '15'},{'name': 'RB', 'src': '10', 'dst': '15'},                {'name': 'RB', 'src': '11', 'dst': '15'},{'name': 'RB', 'src': '12', 'dst': '15'},{'name': 'RB', 'src': '13', 'dst': '15'},                {'name': 'RB', 'src': '14', 'dst': '15'},{'name': 'JJ', 'src': '9', 'dst': '16'},{'name': 'JJ', 'src': '10', 'dst': '16'},                {'name': 'JJ', 'src': '11', 'dst': '16'},{'name': 'JJ', 'src': '12', 'dst': '16'},{'name': 'JJ', 'src': '13', 'dst': '16'},                {'name': 'JJ', 'src': '14', 'dst': '16'},{'name': 'VB', 'src': '15', 'dst': '17'},{'name': 'VBD', 'src': '15', 'dst': '18'},                {'name': 'VBG', 'src': '15', 'dst': '19'},{'name': 'VBN', 'src': '15', 'dst': '20'},{'name': 'VBP', 'src': '15', 'dst': '21'},                {'name': 'VBZ', 'src': '15', 'dst': '22'},{'name': 'VB', 'src': '9', 'dst': '17'},{'name': 'VBD', 'src': '9', 'dst': '18'},                {'name': 'VBG', 'src': '9', 'dst': '19'},{'name': 'VBN', 'src': '9', 'dst': '20'},{'name': 'VBP', 'src': '9', 'dst': '21'},                {'name': 'VBZ', 'src': '9', 'dst': '22'},{'name': 'VB', 'src': '10', 'dst': '17'},{'name': 'VBD', 'src': '10', 'dst': '18'},                {'name': 'VBG', 'src': '10', 'dst': '19'},{'name': 'VBN', 'src': '10', 'dst': '20'},{'name': 'VBP', 'src': '10', 'dst': '21'},                {'name': 'VBZ', 'src': '10', 'dst': '22'},{'name': 'VB', 'src': '11', 'dst': '17'},{'name': 'VBD', 'src': '11', 'dst': '18'},                {'name': 'VBG', 'src': '11', 'dst': '19'},{'name': 'VBN', 'src': '11', 'dst': '20'},{'name': 'VBP', 'src': '11', 'dst': '21'},                {'name': 'VBZ', 'src': '11', 'dst': '22'},{'name': 'VB', 'src': '12', 'dst': '17'},{'name': 'VBD', 'src': '12', 'dst': '18'},                {'name': 'VBG', 'src': '12', 'dst': '19'},{'name': 'VBN', 'src': '12', 'dst': '20'},{'name': 'VBP', 'src': '12', 'dst': '21'},                {'name': 'VBZ', 'src': '12', 'dst': '22'},{'name': 'VB', 'src': '13', 'dst': '17'},{'name': 'VBD', 'src': '13', 'dst': '18'},                {'name': 'VBG', 'src': '13', 'dst': '19'},{'name': 'VBN', 'src': '13', 'dst': '20'},{'name': 'VBP', 'src': '13', 'dst': '21'},                {'name': 'VBZ', 'src': '13', 'dst': '22'},{'name': 'VB', 'src': '14', 'dst': '17'},{'name': 'VBD', 'src': '14', 'dst': '18'},                {'name': 'VBG', 'src': '14', 'dst': '19'},{'name': 'VBN', 'src': '14', 'dst': '20'},{'name': 'VBP', 'src': '14', 'dst': '21'},{'name': 'VBZ', 'src': '14', 'dst': '22'}]})
	high_final_states = ['3','15','16','17','18','19','20','21','22']
	low_final_states = ['4']
	final = []
	fsm.current = '0'
	new_temp = ""
	for j in tagged_sentence:
		try:
			fsm.trigger(j[1])
			new_temp += j[0] + " " 
		except:
			fsm.current='0'
			new_temp = ""
		finally:
			if(fsm.current in high_final_states):
				fsm.current="0"
				new_temp = new_temp[:-1]
				#final.append(new_temp)
				final.append(english_postagger.tag(new_temp.split()))
				new_temp = ""
			elif(fsm.current in low_final_states):
				fsm.current="0"
				new_temp = new_temp[:-1]
				#final.append(new_temp)
				final.append(english_postagger.tag(new_temp.split()))
				new_temp = ""
	s = " "
	return final


#===================== M A I N == P R O G R A M =========================#

#get the mapped data from the file
data = list(csv.reader(open('mappings.csv', 'r', encoding="utf8"), delimiter='\t'))

#get all english-malayalam translations from meta.txt
dictionary = [line.rstrip('\n') for line in open('meta.txt', encoding="utf8")]

#get all preposition translations and rules from meta.txt
prep_rules = [line.rstrip('\n') for line in open('prepositions.txt', encoding="utf8")]

#english word
#print(dictionary[0][:dictionary[0].find(":")])
#malayalam word
#print(dictionary[0][dictionary[0].find(":")+1:])

#for each sentence...
for i in range (len(data)):

	#running for only one case while developing
	#comment the following two lines in production
	if(i>5):
		break

	#if there no malayalam mapping, then ignore that sentence and move on to the next one
	if(len(data[i]) == 1):
		continue;

	#get english sentence
	eng_sen = data[i][0][:-1]
	print ("\n\nSentence is ---> ",eng_sen)

	#printing malayalm mappings
	for j in range (len(data[i])-1):
		print ("\nMalayalam mapping ",j,"->",data[i][j+1])

	
	#POS tag the english sentence
	#create postagger entity
	distsim = 'english-bidirectional-distsim.tagger'
	post = 'stanford-postagger.jar'
	english_postagger = StanfordPOSTagger(distsim, post)
	postag = english_postagger.tag(eng_sen.split())
	print("tagged sentence> ",postag)

	#get the phrases from the sentence
	phrases = SenToPhrase(postag)
	#print (phrases)
	
	#if no phrases were returned by the function, move on to the next sentence
	if(len(phrases) == 0):
		print ("No phrases were returned :( ")
		continue

	for j in range (len(phrases)):
		print ("phrase ",j,"-----> ",phrases[j])
		focus = phrases[j]
		#check if any of the following POS tags are persent in the phrase
		noun=""
		mal_noun=""
		preposition=""
		prep_rule=""
		for k in range (len(focus)):
			if(focus[k][1] in ["NN","NNP","NNPS","NNS"]):
				noun = focus[k][0]
			if(focus[k][1] in ["IN"]):
				preposition = focus[k][0]
				
		if (noun != ""):
			print("This phrase contains a noun --> ",focus)				
			print("The noun is --> ",focus[k][0])
			#find the malayalam translation of the noun
			for l in range (len(dictionary)):
				if(dictionary[l][:dictionary[l].find(":")] == noun):
					mal_noun = dictionary[l][dictionary[l].find(":")+1:]
			print("The translation is -->",mal_noun)

			print ("The proposition is ", preposition)
			for l in range (len(prep_rules)):
				if(prep_rules[l][:prep_rules[l].find(":")] == preposition):
					prep_rule = prep_rules[l][prep_rules[l].find(":")+1:]
			print ("The proposition rule is ", prep_rule[0],"*", prep_rule[1],"*", prep_rule[2],"*")
					
		else:
			print("This phrase contains no nouns :(")

			


	
