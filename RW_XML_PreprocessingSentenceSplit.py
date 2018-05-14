import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
#print(base_path)  print current directory address

xml_file = os.path.join(base_path, "training_set.xml")
#print(xml_file) 

tree = et.parse(xml_file)

root = tree.getroot()

#[1,2,3,4] list

for reviewElement in root:

    #print(reviewElement.tag,reviewElement.attrib)
    newSentencesEl = et.Element('sentences')
    reviewElement.insert(1,newSentencesEl)
    for subChild in reviewElement:
        #print(subChild.tag,subChild.attrib)
        if subChild.tag == 'text':
           reviewTextContent = subChild.text.split('.')
           attrNum = 1
           for sentenceNumber in range(0,len(reviewTextContent)):
               if len(reviewTextContent[sentenceNumber]) != 0:
                   newSentenceEl = et.SubElement(newSentencesEl,'sentence',attrib={"id":str(attrNum)})
                   newSentenceEl.text = reviewTextContent[sentenceNumber].strip()
                   attrNum = attrNum + 1
               #print (reviewTextContent[sentenceNumber].strip())
               #print(newSentenceEl.tag,newSentenceEl.attrib,newSentenceEl.text)
		

tree.write("training_set_SentenceSplitted.xml")