import os
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))
#print(base_path)  print current directory address

xml_file = os.path.join(base_path, "training_set.xml")
#print(xml_file) 

tree = et.parse(xml_file)

root = tree.getroot()

#[1,2,3,4] list

#for child in root:
     #print(child)
	 #print(child.tag)
#     print(child.tag,child.attrib)
	
#for child in root :
#    for element in child:
#       print(element.tag,":", element.text)

#new_review = et.SubElement(root,"review", attrib={"id":"1404"})
#new_review_text = et.SubElement(new_review, "text")
#new_review_aspects = et.SubElement(new_review,"aspects", attrib={"id":"0"})
#new_food_aspect = et.SubElement(new_review_aspects,"aspect", attrib={ "category":"FOOD" , "polarity":"POSITIVE"}) 
#new_price_aspect = et.SubElement(new_review_aspects,"aspect", attrib={   
#new_service_aspect = et.SubElement(new_review_aspects,"aspect", attrib={   
#new_ambience_aspect = et.SubElement(new_review_aspects,"aspect", attrib={   

#new_review_text.text = "bla bla bla bla"

tree.write("randomfile2.xml")