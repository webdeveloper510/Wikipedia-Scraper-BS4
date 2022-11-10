from bs4 import BeautifulSoup
from django.conf import settings
from django.shortcuts import render
import requests
from .models import *
import re
import pprint 
pp = pprint.PrettyPrinter(indent=4)
from collections import defaultdict

from django.conf import settings

# function Called from main function for type and Industry

def gettypeIndustryAndSave(labels,data,keyword,model):
  
   

    count = 0
    name = ''
    for label in labels:
        if label.get_text()==keyword:
         name = data[count].get_text()
        count +=1
         
    id = None
    if keyword=='Type' and name!='':
        type = model()
        type.type_name = name
        type.save()
        id = type.id
    elif keyword=='Industry' and name!='':
        industry = model()
        industry.industry_name = name
        industry.save()
        id = industry.id
    return id
    
# Main Function


def scrape_results_type( request ):

    res = requests.get( url='https://en.wikipedia.org/wiki/Elon_Musk')
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text  , 'html.parser')

    search_type={}
    search_type['label']= soup.select(".infobox-label")
    search_type['data']= soup.select(".infobox-data")
    
    typeId = gettypeIndustryAndSave(search_type['label'],search_type['data'],'Type',Type)
    industryId = gettypeIndustryAndSave(search_type['label'],search_type['data'],'Industry',Industry)
    scrape_results_information(request,soup,typeId,industryId)

    print("typeId===================",typeId)
    print("industryId===================",industryId)
    return
    
    




def scrape_results_information(request , soup ,type_id=None , industry_id=None):
####################  NAME AND IMAGE ############################
    name = {}
    name['Name'] = soup.select("#firstHeading > span ")
    for name_of in name['Name']:
        name['Name'] = name_of.get_text()

    image = {}
    image['Image'] = soup.select("table.infobox a.image img[src]")
    for cov_img in image['Image']:
        name['Img'] = cov_img["src"]
        type_id2 = Type.objects.filter(id = type_id).values('id')
        industry_id2 = Type.objects.filter(id = industry_id).values('id')
    Information_sa = Information.objects.create(name = name["Name"] , image = name['Img'] ,industry_key = None, type_key = None)
    Information_sa.save()
    Information_Id = Information_sa.id
    print("Information_Id===================>" , industry_id2)
    print("Information_Id===================>" , type_id2)
    scrape_results_Content_sub(request , soup , Information_Id=None)






def scrape_results_Content_sub(request , soup , Information_Id=None):

    obj = {}
    object = dict()
    saveobject = {}
    info_key=''
    obj_list2 = []
    obj_list1 = []

    i = ''
    toc2 = soup.findAll('span' , {'class': 'tocnumber'})

    for filter_data in toc2:
        key = filter_data.text
        info_key = key.replace('.' , "_")
        obj_list1.append(info_key)


    toc = soup.findAll('span' , {'class': 'toctext'})
    for info in toc:
        obj_list2.append(info.text)
    count = 0
    for i in obj_list1:
        object[i] = obj_list2[count]

        count += 1
    for keys , value in object.items():
        if len(keys)==1:
            save_Content = Content_type.objects.create(keyID = keys , keyValue = value ,Info_Key = None)
            save_Content.save()
            save_content_ID = save_Content.id
    # '''---------------------------------------------------------<<<???>>>'''



    headingValue3 = ''
    headingValue4 = ''
    foundH3 = False
    foundH4 = False
    dict3 = {}

    about = {}
    dict3['Try'] = soup.select(".mw-parser-output >  h4 , h3 , h2 , p ")
    for para in dict3['Try']:

        #h3
        if para.name == 'h3':
            
            headingValue3 = para.get_text()
            about[headingValue3]  = ''
            foundH3 = True  

        # h4
        if para.name == 'h4':
            headingValue4 = para.get_text()
            about[headingValue4] = ''
            foundH4 = True  
           
        if para.name=='p' :
            if foundH3:
                about[headingValue3] += para.get_text()

            if foundH4:
                about[headingValue4] += para.get_text() 
    
    for keyss , values  in about.items():
        for it , k in object.items():
            if keyss == k:
                print('i-----------> ' , it ,  keyss == k)

                level_length = len(it.split("_"))
                print(level_length)
                SubContent_sa = SubContent_type.objects.create(Sub_keyID = it , Sub_keyValue = keyss , SubKey_Description = values  , level_Info =level_length ,Content_Key = None)
                SubContent_sa.save()
                print("done")
