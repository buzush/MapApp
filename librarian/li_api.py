#!/user/bin/python3

"""
input: library interface permalink to entity,
output: relevant metadata fields, including link to actual media file

json_url example:
http://primo.nli.org.il/PrimoWebServices/xservice/search/full?institution=NNL&docId=NNL03_Bitmuna700136506&json=true

actual media file example:
http://rosetta.nli.org.il/delivery/DeliveryManagerServlet?dps_pid=FL12173162&dps_func=stream

relevant forum discussion:
http://forum.hasadna.org.il/t/apis/986/3

relevant code:
https://github.com/hackita-froy/nli_pic_getter/

name convention:
module_name, package_name, ClassName, method_name, ExceptionName, function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name
"""
"""
TODO:
- Test on different library collections: music, video, travel
- Get better content metadata (subject, date...)
- Get off_campus_flag (online_access)
- For Music collections such as http://primo.nli.org.il/PrimoWebServices/xservice/search/full?institution=NNL&docId=NNL_MUSIC_AL003823118&json=true
there's no ie_id
- Handle collections that don't have permalink and doc_id or have more than one fl_id per ie_id, such as the portrait collection
- Code blocks, aesthetics
"""

#from django.contrib.gis.db import models
#from django.contrib.gis.geos import Point
#import MapApp.mapapp.librarian.models as entityModel

import sys
import os
import urllib.request
import json
import codecs
import re

#rosetta
import xml.etree.ElementTree as ET
import suds
import suds.client as suds_client

""" rosetta stuff, used by get_fl_id_list(doc_id), get_fl_url_list(doc_id)"""

#rosetta end point
ROSETTA_WSDL_URL="http://rosetta.nli.org.il/dpsws/delivery/DeliveryAccessWS?wsdl"
ROSETTA_IMAGE_URL="http://rosetta.nli.org.il/delivery/DeliveryManagerServlet?dps_pid={0}&dps_func=stream"
ROSETTA_FILE_RETRIEVE="http://rosetta.nli.org.il/delivery/DeliveryManagerServlet?dps_pid={0}&dps_func=stream"

#ROSETTA_WSDL_URL = os.environ['ROSETTA_WSDL_URL']
FILE_ID_ATTR = 'FILEID'

""" Return suds client """
def get_rosetta_client():
    return suds_client.Client(ROSETTA_WSDL_URL)

""" Return suds client.service """
def get_rosetta_delivery_service():
    return get_rosetta_client().service

""" end of rosetta stuff, used by get_fl_id_list(doc_id), get_fl_url_list(doc_id)"""


def get_doc_id(lib_ui_url):
    doc_id = re.search('docId=.+',lib_ui_url).group()[6:]
    return doc_id

# entity_dict = entityModel.Content(models.Model)
# print(entity_dict)

def get_json_url(doc_id):
    # not all collections have doc_id, see portrait collection as an example
    json_url = "http://primo.nli.org.il/PrimoWebServices/xservice/search/full?institution=NNL&docId={}&json=true".format(doc_id)
    return json_url

def get_json_obj(doc_id):
    # not all collections have doc_id, see portrait collection as an example
    json_url = get_json_url(doc_id)
    j = urllib.request.urlopen(json_url)
    reader = codecs.getreader("utf-8")
    j_obj = json.load(reader(j))
    return j_obj

def get_ie_id(doc_id):
    # TODO: test for different types of collections, more generic search might be needed
    j_obj = get_json_obj(doc_id)
    try:
        link_to_rsrc = (j_obj['SEGMENTS']['JAGROOT']['RESULT']['DOCSET']['DOC']['PrimoNMBib']['record']['links']['thumbnail'])
        ie_id = re.search('IE[0-9]{1,20}', link_to_rsrc).group()
        #ie_id = re.search('IE.+', link_to_rsrc).group()
    except:
        ie_id = None

    return ie_id

def get_display_dict(doc_id):
    j_obj=get_json_obj(doc_id)
    try:
        display_dict = (j_obj['SEGMENTS']['JAGROOT']['RESULT']['DOCSET']['DOC']['PrimoNMBib']['record']['display'])
    except:
        display_dict = None
    return display_dict


def get_title(doc_id):
    j_obj=get_json_obj(doc_id)
    try:
        title = (j_obj['SEGMENTS']['JAGROOT']['RESULT']['DOCSET']['DOC']['PrimoNMBib']['record']['display']['title'])
    except:
        title = None

    return title

def get_subject(doc_id):
    j_obj=get_json_obj(doc_id)

    try:
        subject = (j_obj['SEGMENTS']['JAGROOT']['RESULT']['DOCSET']['DOC']['PrimoNMBib']['record']['display']['subject'])
    except:
        subject = None

    return subject

def get_content_type(doc_id):
    j_obj=get_json_obj(doc_id)
    try:
        content_type = (j_obj['SEGMENTS']['JAGROOT']['RESULT']['DOCSET']['DOC']['PrimoNMBib']['record']['display']['type'])
    except:
        content_type = None

    return content_type

def get_date(doc_id):
    j_obj=get_json_obj(doc_id)
    try:
        date = (j_obj['SEGMENTS']['JAGROOT']['RESULT']['DOCSET']['DOC']['PrimoNMBib']['record']['display']['creationdate'])
    except:
        date = None

    return date

""" Return list of all FL asosciated with doc_id """
def get_fl_id_list(doc_id):
    ie_id = get_ie_id(doc_id)
    ns = {'mets': 'http://www.loc.gov/METS/'}
    fl_list = []
    try:
        result = get_rosetta_delivery_service().getIE(ie_id)
        tree = ET.fromstring(result)
        fptr_elements = tree.findall('.//mets:structMap[1]//mets:fptr', ns)
        for element in fptr_elements:
            fl_list.append(element.get(FILE_ID_ATTR))

        return fl_list
    except suds.WebFault as e :
        print('an web error happened, entity not retrieved')
        print(e)
        return

""" Return list of all urls to FL asosciated with doc_id """
def get_fl_url_list(doc_id):
    fl_url_list=[]
    for fl_id in get_fl_id_list(doc_id):
        fl_url_list.append("http://rosetta.nli.org.il/delivery/DeliveryManagerServlet?dps_pid={0}&dps_func=stream".format(fl_id))
    return fl_url_list


"""
  # get actual media file from FL_url
def get_media_file_from_fl_id(fl_id):
    f = urllib.request.urlopen("http://rosetta.nli.org.il/delivery/DeliveryManagerServlet?dps_pid={0}&dps_func=stream".format(fl_id))
"""

def get_metadata_dict(lib_ui_url):

    entity_dict = {"content_type":"", "title":"", "subject":"", "date":"", "online_access":"", "display_dict":"", "ids":{"doc_id":"", "ie_id":"", "fl_id_list":""}, "urls":{"lib_ui_url":"", "json_url":"", "fl_url_list":""}}

    doc_id = get_doc_id(lib_ui_url)

    entity_dict["content_type"] = get_content_type(doc_id)
    entity_dict["title"] = get_title(doc_id)
    entity_dict["subject"] = get_subject(doc_id)
    entity_dict["date"] = get_date(doc_id)

    # TODO: online_access

    entity_dict["display_dict"] = get_display_dict(doc_id)

    entity_dict["ids"]["doc_id"] = doc_id
    entity_dict["ids"]["ie_id"] = get_ie_id(doc_id)
    entity_dict["ids"]["fl_id_list"] = get_fl_id_list(doc_id)

    entity_dict["urls"]["lib_ui_url"] = lib_ui_url
    entity_dict["urls"]["json_url"] = get_json_url(doc_id)
    entity_dict["urls"]["fl_url_list"] = get_fl_url_list(doc_id)

    return(entity_dict)


""" TESTS """

""" list of test entities from different collections"""

# Ephemera
ephemera_url_1 = 'http://primo.nli.org.il/primo_library/libweb/action/dlDisplay.do?vid=NNL_Ephemera&docId=NNL_Ephemera700157393'

# Jewish Art
jewish_art_url_1 = 'http://primo.nli.org.il/primo_library/libweb/action/dlDisplay.do?vid=NLI_CJA&docId=NNL03_CJA700384633'

# Maps
map_url_1 = 'http://primo.nli.org.il/primo_library/libweb/action/dlDisplay.do?vid=NLI&docId=NNL_MAPS002368920'
map_url_2 = 'http://primo.nli.org.il/primo_library/libweb/action/dlDisplay.do?vid=NLI&docId=NNL_MAPS002370015'

# Photos

# Bitmuna
bitmuna_url_1 = 'http://primo.nli.org.il/primo_library/libweb/action/dlDisplay.do?vid=NLI_Photo&docId=NNL03_Bitmuna700137006'

# Zalmania
zalmania_url_1 = 'http://primo.nli.org.il/primo_library/libweb/action/dlDisplay.do?vid=NLI_Zalmania&docId=NNL_Zalmania_ROS700012818'

# Video
# TODO

# Song
# TODO

# Travel
# TODO

test_url_list = [ephemera_url_1, jewish_art_url_1, map_url_1, map_url_2, bitmuna_url_1, zalmania_url_1]

for url in test_url_list:
    #print(get_json_url(get_doc_id(url)))
    print(get_metadata_dict(url))