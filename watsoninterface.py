import requests
import simplejson as json

#medical dictionary...
d = { "chest was hurting":"angina,chest pain","sweating a lot":"diaphoresis", "about your stomach in the middle of your chest":"epigrastric,mediastinal","heartburn":"pyrosis"}
body_parts=["chest","stomach"]
verbs =["hurting","sweating"]
locations=["above","middle"]

#grabs symptoms from line
def symptom_reader(x):
    sym =[]
    for key in d.keys():
        if key in x:
            sym.append(d[key])
    return sym

#shows the results
def symptom_results(y):
    results =[]
    #print y['results']
    for i in range(len(y["results"])):
        results.append(filter(None,symptom_reader(y["results"][i]["alternatives"][0]["transcript"])))
    print results
    results2=filter(None,results)
    print results2
    return results2

def convertToJson():
	with open('Output.txt', 'r') as myfile:
		data = myfile.read().replace('\n','')
	dump = json.dumps(data)
	load = json.loads(dump)
	#print dump
	symptom_results(load)
	return

def rewriteTrue():
	text_file = open("Output.txt", "r")
	filedata = text_file.read()
	text_file.close()

	newdata = filedata.replace("true", "True")

	f = open("Output.txt", "w")
	f.write(newdata)
	f.close()
	#convertToJson()
	return

url = 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true'

username = "a9b10227-8be9-4e12-8437-64ac70c35227"
password = "dUD1Ke2xRle8"

headers={'Content-Type': 'audio/wav'}

audio = open('Htech2.wav', 'rb')

r = requests.post(url, data=audio, headers=headers, auth=(username, password))

data = r.json()
with open('ibmoutputjson.txt', 'w') as outfile:
    json.dump(data, outfile)

#print(r.text)
text_file = open("Output.txt", "w")
text_file.write(r.text)
text_file.close()

rewriteTrue()
symptom_results(r.json())






#curl -u a9b10227-8be9-4e12-8437-64ac70c35227:dUD1Ke2xRle8 -X POST --header "Content-Type: audio/wav" --header "Transfer-Encoding: chunked" --data-binary @Htech1.wav "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true"

#curl --user a9b10227-8be9-4e12-8437-64ac70c35227:dUD1Ke2xRle8 --request POST --header 'Content-Type: audio/wav' --header 'Transfer-Encoding: chunked' --data-binary @Htech1.wav 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true'

#curl --header 'Content-Type: audio/wav' --header 'Transfer-Encoding: chunked' --data @Htech1.wav 'https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?continuous=true'