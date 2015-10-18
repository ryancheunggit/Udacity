# load libraries
import os
import xml.etree.cElementTree as cET
from collections import defaultdict
import pprint
import re
import codecs
import json
import string
from pymongo import MongoClient

# set up map file path
filename = "boston_massachusetts.osm" # osm filename
path = "d:\GithubRepos\Udacity\P3" # directory contain the osm file
bostonOSM = os.path.join(path, filename)

# some regular expression 
lower = re.compile(r'^([a-z]|_)*$') 
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

# initial version of expected street names
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place",
            "Square", "Lane", "Road", "Trail", "Parkway", "Commons"]

# Look at the street names, print out all the street names that is with 
# a unexpected street type
def audit_street_type(street_types, street_name):
    # add unexpected street name to a list
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
            
def is_street_name(elem):
    # determine whether a element is a street name
    return (elem.attrib['k'] == "addr:street")

def audit_street(osmfile):
    # iter through all street name tag under node or way and audit 
    # the street name value
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in cET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    return street_types

st_types = audit_street(bostonOSM)
# print out unexpected street names
pprint.pprint(dict(st_types))

# Based on the auditing results, I came up with the following mapping 
# dictionary, which addressed the abbrivations and the incorrect names.

# creating a dictionary for correcting street names
mapping = { "Ct": "Court",
            "St": "Street",
            "st": "Street",
            "St.": "Street",
            "St,": "Street",
            "ST": "Street",
            "street": "Street",
            "Street.": "Street",
            "Ave": "Avenue",
            "Ave.": "Avenue",
            "ave": "Avenue",
            "Rd.": "Road",   
            "rd.": "Road",
            "Rd": "Road",    
            "Hwy": "Highway",
            "HIghway": "Highway",
            "Pkwy": "Parkway",
            "Pl": "Place",      
            "place": "Place",
            "Sedgwick": "Sedgwick Street",
            "Sq.": "Square",
            "Newbury": "Newbury Street",
            "Boylston": "Boylston Street",
            "Brook": "Brook Parkway",
            "Cambrdige": "Cambrdige Center",
            "Elm": "Elm Street",
            "Webster Street, Coolidge Corner": "Webster Street",
            "Faneuil Hall": "Faneuil Hall Market Street",
            "Furnace Brook": "Furnace Brook Parkway",
            "Federal": "Federal Street",
            "South Station, near Track 6": "South Station, Summer Street",
            "PO Box 846028": "846028 Surface Road",
            "First Street, Suite 303": "First Street",
            "Kendall Square - 3": "Kendall Square",
            "Franklin Street, Suite 1702": "Franklin Street",
            "First Street, Suite 1100": "First Street",
            "Windsor": "Windsor Stearns Hill Road",
            "Winsor": "Winsor Village Pilgrim Road",
            "First Street, 18th floor": "First Street",
            "Sidney Street, 2nd floor": "Sidney Street",
            "Boston Providence Turnpike": "Boston Providence Highway",
            "LOMASNEY WAY, ROOF LEVEL": "Lomasney Way",
            "Holland": "Holland Albany Street",
            "Hampshire": "Hampshire Street",
            "Boylston Street, 5th Floor": "Boylston Street",
            "Fenway": "Fenway Yawkey Way",
            "Charles Street South": "Charles Street"}

# function that corrects incorrect street names
def update_name(name, mapping):    
    for key in mapping:
        if key in name:
            name = string.replace(name,key,mapping[key])
    return name
    
def audit_zipcodes(osmfile):
    # iter through all zip codes, collect all the zip codes that does not 
    # start with 02
    osm_file = open(osmfile, "r")
    zip_codes = {}
    for event, elem in cET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if tag.attrib['k'] == "addr:postcode" and not tag.attrib['v'].startswith('02'):
                    if tag.attrib['v'] not in zip_codes:
                        zip_codes[tag.attrib['v']] = 1
                    else:
                        zip_codes[tag.attrib['v']] += 1
    return zip_codes

zipcodes = audit_zipcodes(bostonOSM)
for zipcode in zipcodes:
    print zipcode, zipcodes[zipcode]
    
CREATED = [ "version", "changeset", "timestamp", "user", "uid"]

def shape_element(element):
    node = {}
    node["created"]={}
    node["address"]={}
    node["pos"]=[]
    refs=[]
    
    # we only process the node and way tags
    if element.tag == "node" or element.tag == "way" :
        if "id" in element.attrib:
            node["id"]=element.attrib["id"]
        node["type"]=element.tag

        if "visible" in element.attrib.keys():
            node["visible"]=element.attrib["visible"]
      
        # the key-value pairs with attributes in the CREATED list are 
        # added under key "created"
        for elem in CREATED:
            if elem in element.attrib:
                node["created"][elem]=element.attrib[elem]
                
        # attributes for latitude and longitude are added to a "pos" array
        # include latitude value        
        if "lat" in element.attrib:
            node["pos"].append(float(element.attrib["lat"]))
        # include longitude value    
        if "lon" in element.attrib:
            node["pos"].append(float(element.attrib["lon"]))

        
        for tag in element.iter("tag"):
            if not(problemchars.search(tag.attrib['k'])):
                if tag.attrib['k'] == "addr:housenumber":
                    node["address"]["housenumber"]=tag.attrib['v']
                    
                if tag.attrib['k'] == "addr:postcode":
                    node["address"]["postcode"]=tag.attrib['v']
                
                # handling the street attribute, update incorrect names using
                # the strategy developed before   
                if tag.attrib['k'] == "addr:street":
                    node["address"]["street"]=tag.attrib['v']
                    node["address"]["street"] = update_name(node["address"]["street"], mapping)

                if tag.attrib['k'].find("addr")==-1:
                    node[tag.attrib['k']]=tag.attrib['v']
                    
        for nd in element.iter("nd"):
             refs.append(nd.attrib["ref"])
                
        if node["address"] =={}:
            node.pop("address", None)

        if refs != []:
           node["node_refs"]=refs
            
        return node
    else:
        return None

# process the xml openstreetmap file, write a json out file and return a
# list of dictionaries
def process_map(file_in, pretty = False):
    file_out = "{0}.json".format(file_in)
    data = []
    with codecs.open(file_out, "w") as fo:
        for _, element in cET.iterparse(file_in):
            el = shape_element(element)
            if el:
                data.append(el)
                if pretty:
                    fo.write(json.dumps(el, indent=2)+"\n")
                else:
                    fo.write(json.dumps(el) + "\n")
    return data
    
# process the file
data = process_map(bostonOSM, True)

# Insert the data into local MongoDB Database
client = MongoClient()
db = client.BostonOSM
collection = db.bostonMAP
collection.insert(data)

collection

# Summary Statistics of Data
# size of the original xml file
os.path.getsize(bostonOSM)/1024/1024

# size of the processed json file
os.path.getsize(os.path.join(path, "boston_massachusetts.osm.json"))/1024/1024

# The Number of documents
collection.find().count()

# The Number of Unique users
len(collection.group(["created.uid"], {}, {"count":0}, "function(o, p){p.count++}"))

# The Number of Nodes
collection.find({"type":"node"}).count()

# The Number of Ways
collection.find({"type":"way"}).count()

# The Number of Methods Used to Create Data Entry
pipeline = [{"$group":{"_id": "$created_by",
                       "count": {"$sum": 1}}}]
result = collection.aggregate(pipeline)
print(len(result['result']))\

# Proportions of top users' contributions
pipeline = [{"$group":{"_id": "$created.user",
                       "count": {"$sum": 1}}},
            {"$project": {"proportion": {"$divide" :["$count",collection.find().count()]}}},
            {"$sort": {"proportion": -1}},
            {"$limit": 3}]
result = collection.aggregate(pipeline)
result['result']

# Most popular cuisines
pipeline = [{"$match":{"amenity":{"$exists":1}, "amenity":"restaurant", "cuisine":{"$exists":1}}}, 
            {"$group":{"_id":"$cuisine", "count":{"$sum":1}}},        
            {"$sort":{"count":-1}}, 
            {"$limit":10}]
result = collection.aggregate(pipeline)
result['result']

#  Universities
pipeline = [{"$match":{"amenity":{"$exists":1}, "amenity": "university", "name":{"$exists":1}}},
            {"$group":{"_id":"$name", "count":{"$sum":1}}},
            {"$sort":{"count":-1}}]
result = collection.aggregate(pipeline)
result['result']