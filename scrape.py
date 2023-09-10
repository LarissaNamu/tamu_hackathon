import xml.etree.ElementTree as ET
import json
import requests

stops=[8502689138, 8502689139, 8502689140, 9460150719, 9461821084, 9461821085, 9461821086, 9461821087, 9461821088, 9461821089, 9461821090, 9461821091, 9461821092, 9461821093, 9461821094, 9461821095, 9461821097, 9461821098, 9461821099, 9461821100, 9461821101, 9461821102, 9461821103, 9630568957, 10062018693, 10062379785, 10081955879, 10553778079, 10553778080, 10553778081, 10553778082, 10553778087, 10553778088, 10688559663, 10688627220, 10716013943, 10716013944, 10716013945, 10716013946, 10716013947, 10716013948, 10716075596, 10716075597, 10716075598, 10716075599, 10716075600, 10716075601, 10716075602, 10716075603, 10716075604, 10716077105, 10728463229, 10972116191, 10972118464, 11033604431, 11033604432, 11033604433, 11033604434, 11033604435, 11033604436, 11033604437, 11033604438, 11033604439, 11033604451, 11033604452, 11033604453, 11052607135, 11052607136, 11052607137, 11052607138, 11052607139, 11052706187, 11052706188, 11052706189, 11052706190, 11052706191, 11052706192, 11052706193, 11053998554, 11054013702, 11054021345, 11054028644, 11054028916, 11054032207, 11054066176, 11054066177, 11054066178, 11054066179, 11054066180, 11054066181, 11054066182, 11054066183, 11054066184, 11054228268, 11054228269, 11054431403, 11062930445, 11062930446, 11062930447, 11062930448, 11062930449, 11062930450, 11062930451, 11062930452, 11062930453, 11062930454, 11062930455, 11062930456, 11062930457, 11062930458, 11062930459, 11062930460, 11062930461, 11062930462, 11062930463, 11065893552, 11065893554, 11065893555, 11065943254, 11076658007, 11076658008, 11076658009, 11076658010, 11076658011, 11076658012, 11076658013, 11076658014, 11076658015, 11076658016, 11076658017, 11076658018, 11076658019, 11076658020, 11076658021, 11076658022, 11076658023, 11076658024, 11076658025]
def extract_data(data):
  #'id, latitude, longitude, stop name, bus route number, bus route name'
  out=''
  data=data['elements']
  first_line=data[0]
  for i, node in enumerate(data):
    line=''
    if i==0:
      continue
    else:
      line+=str(first_line['id'])+','
      line+=str(first_line['lat'])+','
      line+=str(first_line['lon'])+','
      line+=first_line['tags']['name']+','
      try:
        line+=node['tags']['ref']+','
      except:
        continue  
      try:
        line+=node['tags']['description']+','
      except:
        line+=node['tags']['name']+','

      out+=line+'\n'

  return out
      
      
# # Construct the query
# query = """
# /*
# This has been generated by the overpass-turbo wizard.
# The original search was:
# “"bus stop"”
# */
# [out:json][timeout:100];
# // gather results
# (
#   // query part for: “"bus stop"”
#   node[highway=bus_stop][network=AggieSpirit];
#   node[highway=bus_stop][network=AggieSprit];
# );
# // print results
# out body;
# >;
# out skel qt;
# """

# url = "https://overpass-api.de/api/interpreter"
# response = requests.get(url, params={'data': query})

# # Parse the JSON response
# data = response.json()

# stops = []
# for element in data['elements']:
#     stop_type = element['tags'].get('highway') or element['tags'].get('railway')
#     stops.append(
#         element['id'],   # Include the OSM node ID
#     )

# print(stops)
# print(len(stops))



url = "https://overpass-api.de/api/interpreter"
f=open('stops.csv','w')
for id in stops:

    # Construct the query for the specific node
    query = f"""
    [out:json][timeout:25];
    (node({id});
    <;
    );
    out geom;
"""
    response = requests.get(url, params={'data': query})


    # Parse the JSON response
    data = response.json()

    f.write(extract_data(data))

f.close()