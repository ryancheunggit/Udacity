from bs4 import BeautifulSoup
import requests


r = requests.get("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2")
soup = BeautifulSoup(r.text)

vs = soup.find(id = "__VIEWSTATE")["value"]
ev = soup.find(id = "__EVENTVALIDATION")["value"]

r = requests.post("http://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
             data = {"AirportList":"BOS",
                     "CarrierList":"VX",
                     "Submit": "Submit",
                     "__EVENTTARGET": "",
                     "__EVENTARGUMENT":"",
                     "__EVENTVALIDATION": ev,
                     "__VIEWSTATE":vs})
                     
f = open("virgin_and_logan_test.html", "w")
f.write(r.text)