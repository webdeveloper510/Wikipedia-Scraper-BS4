from bs4 import BeautifulSoup
import requests
from .models import *
import pprint 
pp = pprint.PrettyPrinter(indent=4)



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
        src_img = cov_img["src"]
####################  OTHER INFORMATION DATA #####################

    type = None if type_id is None else Type.objects.get(id=type_id)
    industry = None if industry_id is None else Industry.objects.get(id=industry_id)
    store_information = Information.objects.create(name = name_of.get_text() , image = src_img  ,type_key = type , industry_key = industry)
    store_information.save()
    information_id = store_information.id
    print()
    search_type_informatoinMeta(request  , soup , information_id)
    print('Information Store Done')

    # context = {'result3' : dictt}
    # return render(request , 'results.html' , context)





def search_type_informatoinMeta(request  , soup, information_id):
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
            dictt['Founded'] = dictt.pop(found_id)
#################### Other data #################################################
    dict3 = {}
    about = {}
    dict3['Try'] = soup.select(".mw-parser-output >  h4 ,h3 , h2 , p ")
    asdf = dict3['Try']
    for para in asdf:
        if para.name == 'p':
            about['About'] = para.get_text()

        if para.name=='h2' or para.name=='h3' or para.name=='h4':
            break
    foundH2 = False
    foundH3 = False
    foundH4 = False
    headingValue = ''
    headingValue3 = ''
    headingValue4 = ''
    for para in asdf:
        # h2
        if para.name=='h2':
            headingValue = para.get_text()
            about[headingValue] = ''
            foundH2 = True
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
        if para.name=='p':
            if foundH2:
                about[headingValue] += para.get_text()
            if foundH3:
                about[headingValue3] += para.get_text()
            if foundH4:
                about[headingValue4] += para.get_text() 
    dict_dictt_about = {}
    for dictt_k ,dictt_v in dictt.items():
        dict_dictt_about[dictt_k] = dictt_v
    for about_k ,about_v in about.items():
        dict_dictt_about[about_k] = about_v
    print(dict_dictt_about)
    for ddk , ddv in dict_dictt_about.items():


    # dict_dictt_about_keys = {'dictt_keys' :dictt.keys()  , 'about_keys' : about.keys()}
    # # print(dict_dictt_about_keys.values())
    # dict_dictt_about_values = {'dictt_values' :dictt.values()  , 'about_values' : about.values()}
        information_id2 = Information.objects.get(id=information_id)
        store_infoMeta = Info_Meta.objects.create(meta_key = ddk, meta_value = ddv , info_key = information_id2)   
        store_infoMeta.save()
    print('NInformation_META Store Done')

    # context = {'result4' : about}
    # return render(request , 'results.html' , context)