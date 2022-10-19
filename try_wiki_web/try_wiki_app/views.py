from bs4 import BeautifulSoup
from django.shortcuts import render
import requests
import re
from .models import *




def scrape_results_type(request ):

    res = requests.get( url='https://en.wikipedia.org/wiki/World_Health_Organization')
    res.encoding = "utf-8"
    soup = BeautifulSoup(res.text  , 'html.parser')

    search_type={}
    search_type['label']= soup.select(".infobox-label")
    search_type['data']= soup.select(".infobox-data")
    type_count = 0
    result_type = {}
    for type_label in search_type['label']:
        result_type[type_label.get_text()] = search_type['data'][type_count].get_text()
        type_count += 1
    
    if result_type :
        # if result_type['Born']:
        #     type_data = 'Person'
        if result_type['Type'] :
            type_data = 'Organization'
        else:
            print('error')
    #     store_type = Type.objects.create(type_name = type_data)
    #     store_type.save()
    # type_id = store_type.id
    print("Type Store done")

#################INDUSTRY PARTY #################

    search_typeIndustry = {}
    search_typeIndustry['label']= soup.select(".infobox-label")
    search_typeIndustry['data']= soup.select(".infobox-data")
    type_count = 0
    result_typeIndustry = {}
    for type_label in search_typeIndustry['label']:
        result_typeIndustry[type_label.get_text()] = search_typeIndustry['data'][type_count].get_text()
        type_count += 1
    # if result_typeIndustry :
        # if result_typeIndustry['Title']:
        #     type_ind = result_typeIndustry['Title']
        #     print(result_typeIndustry['Title'])

        # if result_typeIndustry['Industry'] :
        #     type_ind = result_typeIndustry['Industry']
        # else:
        #     print('error')
        # indus = [s for s in re.split("([A-Z][^A-Z]*)", type_ind ) if s]
        # value = " , ".join(indus)
        # store_industry = Industry.objects.create(industry_name = value)
        # store_industry.save()
        # industry_id = store_industry.id
        # print(type_id)
    scrape_results_information(request , soup)# , type_id , industry_id)
    print("Industry Store done")
    return render(request , 'results.html')# , context)




def scrape_results_information(request , soup ):#,type_id , industry_id):
####################  NAME AND IMAGE ############################
    name = {}
    name['Name'] = soup.select("#firstHeading > span ")
    for name_of in name['Name']:
        name['Name'] = name_of.get_text()

    image = {}
    image['Image'] = soup.select("table.infobox a.image img[src]")
    for cov_img in image['Image']:
        src_img = cov_img["src"]
####################  OTHER INFORMATION DATA #####################

    # type_id2 = Type.objects.get(id=type_id)
    # industry_id2 = Industry.objects.get(id=industry_id)
    # store_information = Information.objects.create(name = name_of.get_text() , image = src_img  ,type_key = type_id2 , industry_key = industry_id2)
    # store_information.save()
    # information_id = store_information.id
    search_type_informatoinMeta(request  , soup)# , information_id)
    print('Information Store Done')

    # context = {'result3' : dictt}
    # return render(request , 'results.html' , context)

def search_type_informatoinMeta(request  , soup):#, information_id):
################### INFORMATION DATA ####################

    dictuse = {}
    dictuse['Diff'] = soup.select(".infobox-label")
    dictuse['Diss'] = soup.select(".infobox-data")
    abc = 0
    founded_type = ['Founded' , 'Formed' , 'Formation']
    dictt={}
    for i in dictuse['Diff']:   
        dictt[i.get_text()]= dictuse['Diss'][abc].get_text()
        abc += 1
    for found_id in founded_type:
        if found_id in dictt.keys():
            # print(dictt[found_id])
            dictt[found_id] = dictt['Founded']
    print(dictt.keys())
            






#################### Other data #################################################
    dict3 = {}
    about = {}
    dict3['Try'] = soup.select(".mw-parser-output >  h3 , h2 , p ")
    asdf = dict3['Try']
    for para in asdf:
        if para.name == 'p':
            about['About'] = para.get_text()
        if para.name=='h2' or para.name=='h3':
            break
    foundH2 = False
    foundH3 = False
    headingValue = ''
    headingValue3 = ''
    for para in asdf:
        if para.name=='h2':
            headingValue = para.get_text()
            about[headingValue] = ''
            foundH2 = True
        if para.name == 'h3':
            headingValue3 = para.get_text()
            about[headingValue3]  = ''
            foundH3 = True            
        if para.name == 'p':
            if foundH2:
               about[headingValue] += para.get_text()
            if foundH3:
                about[headingValue3] += para.get_text()
        # information_id2 = Information.objects.get(id=information_id)
        # store_infoMeta = Info_Meta.objects.create(meta_key = about.keys() , meta_value = about.values() , info_key = information_id2)   
        # store_infoMeta.save()
    print('NInformation_META Store Done')

    # context = {'result4' : about}
    # return render(request , 'results.html' , context)