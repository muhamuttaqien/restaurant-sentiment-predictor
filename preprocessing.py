import os
import xml.etree.ElementTree as et
import nltk
import Sastrawi

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
en_stop_words = set(stopwords.words('english'))

from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

pstemmer = PorterStemmer()

from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
factory = StopWordRemoverFactory()
#ind_stop_words = factory.get_stop_words()
ind_stop_word_remover = factory.create_stop_word_remover()

# import StemmerFactory class
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

# create stemmer
stemToolFactory = StemmerFactory()
ind_word_stemmer = stemToolFactory.create_stemmer()

base_path = os.path.dirname(os.path.realpath(__file__))
#print(base_path)  print current directory address

xml_file = os.path.join(base_path, "training_set.xml")
#xml_file = os.path.join(base_path, "_______") XML training set to be read


tree = et.parse(xml_file)

root = tree.getroot()

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
                   #newSentenceEl = et.SubElement(newSentencesEl,'sentence',attrib={"id":str(attrNum)})
                   #newSentenceEl.text = reviewTextContent[sentenceNumber].strip()
                   newProcSentenceEl = et.SubElement(newSentencesEl,'sentence',attrib={"id":str(attrNum)})
                   word_tokens = word_tokenize(reviewTextContent[sentenceNumber].strip())
                   filtered_sentence = [w for w in word_tokens if not w in en_stop_words]
                   attrNum = attrNum + 1
                   #print(reviewTextContent[sentenceNumber].strip())
                   #print(newSentenceEl.tag,newSentenceEl.attrib,newSentenceEl.text)
                   filtered_sentence_result = ""
                   for w in filtered_sentence:
                      filtered_sentence_result = filtered_sentence_result + (pstemmer.stem(w)) + " "
                   filtered_sentence_result2 = filtered_sentence_result[:(len(filtered_sentence_result)-1)]
                   newProcSentenceEl.text = ind_word_stemmer.stem(ind_stop_word_remover.remove(filtered_sentence_result2))
                   #print(newProcSentenceEl.tag,newProcSentenceEl.attrib,newProcSentenceEl.text)
				   
tree.write("training_set_preprocessed.xml")#tree.write("____________") XML preprocessed training set file to be written on 

xml_file = os.path.join(base_path, "validation_set.xml") 

tree = et.parse(xml_file)

root = tree.getroot()

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
                   #newSentenceEl = et.SubElement(newSentencesEl,'sentence',attrib={"id":str(attrNum)})
                   #newSentenceEl.text = reviewTextContent[sentenceNumber].strip()
                   newProcSentenceEl = et.SubElement(newSentencesEl,'cleansentence',attrib={"id":str(attrNum)})
                   word_tokens = word_tokenize(reviewTextContent[sentenceNumber].strip())
                   filtered_sentence = [w for w in word_tokens if not w in en_stop_words]
                   attrNum = attrNum + 1
                   #print(reviewTextContent[sentenceNumber].strip())
                   print(newSentenceEl.tag,newSentenceEl.attrib,newSentenceEl.text)
                   filtered_sentence_result = ""
                   for w in filtered_sentence:
                      filtered_sentence_result = filtered_sentence_result + (pstemmer.stem(w)) + " "
                   filtered_sentence_result2 = filtered_sentence_result[:(len(filtered_sentence_result)-1)]
                   newProcSentenceEl.text = ind_word_stemmer.stem(ind_stop_word_remover.remove(filtered_sentence_result2))
                   print(newProcSentenceEl.tag,newProcSentenceEl.attrib,newProcSentenceEl.text)
				   
tree.write("training_set_preprocessed.xml")