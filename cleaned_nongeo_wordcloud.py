import pandas as pd

from wordcloud import WordCloud

import matplotlib.pyplot as plt

# Location words resource: https://github.com/FNeffati/TBRTD/blob/main/frontEnd/src/components/analysis.js
# + split versions. ex: "bay", "gulf"

locations = ['Gottfried Creek', 'Halifax River', 'Hamilton Branch', 'Harney River', 'Hickory Creek','Hillsborough River', 'Homosassa River', 'Hontoon Dead River', 'Ichetucknee River', 'Imperial River',
        'Itchepackesassa Creek', 'Julington Creek', 'Kissimmee River', 'Lafayette Creek',"Little Econlockhatchee River", "Little Manatee River", "Little River (Biscayne Bay)",
        "Little River (Ochlockonee River tributary)", "Little Wekiva River", "Little Withlacoochee River","Lochloosa Creek", "Loxahatchee River", "Manatee River", "Matanzas River", "McCullough Creek",
        "Miami River", "Myakka River", "Myakkahatchee Creek", "New River (Broward County)","New River (Carrabelle River tributary)", "New River (Santa Fe River tributary)", "Ochlockonee River",
        "Ocklawaha River", "Oleta River", "Orange Creek", "Orange River", "Palatlakaha River", "Payne Creek","Pea River", "Peace River", "Pellicer Creek", "Perdido River", "Pimple Creek",
        "Pithlachascotee River", "Poplar Creek", "Pottsburg Creek", "Rainbow River", "Ribault River","Rice Creek (St. Johns River)", "Rocky Comfort Creek", "St. Johns River", "St. Marys River",
        "Santa Fe River", "Shingle Creek", "Silver River", "Snapper Creek", "Sopchoppy River","Spanish River", "Spanishtown Creek", "St. Lucie River", "St. Marks River", "St. Sebastian River",
        "Steinhatchee River", "Suwannee River", "Swamp Creek (Attapulgus Creek tributary)","Tampa Bypass Canal", "Telogia Creek", "Three Rivers State Park", "Tiger Creek", "Tomoka River",
        "Trout River", "Turkey Creek (Econlockhatchee River tributary)","Turkey Creek (Indian River tributary)", "Waccasassa River", "Wacissa River", "Wagner Creek",
        "Wakulla River", "Weeki Wachee River", "Wekiva River", "Wekiva River (Gulf Hammock, Levy County)","Whidden Creek", "Withlacoochee River", "Withlacoochee River (Suwannee River tributary)",
        "Yellow River (Pensacola Bay)", 'Apalachee Bay', 'Apalachicola Bay', 'Boca Ciega Bay', 'Charlotte Harbor','Choctawhatchee Bay', 'East Bay', 'Escambia Bay', 'Estero Bay', 'Florida Bay', 'Pensacola Bay', 'Ponce de Leon Bay',
        'Sarasota Bay', 'St. Andrews Bay', 'St. Joseph Bay', 'Tampa Bay', 'Whitewater Bay', "Anna Maria", "Bradenton","Bradenton Beach", "Cortez", "Ellenton", "Holmes Beach", "Longboat Key",
        "Myakka City", "Oneco", "Palmetto", "Parrish", "Sarasota", "Tallevast", "Terra Ceia", "Apollo Beach","Balm", "Brandon", "Dover", "Durant", "Gibsonton", "Lithia", "Lutz", "Mango", "Odessa", "Plant City",
        "Riverview", "Ruskin", "Seffner", "Sun City", "Sun City Center", "Sydney", "Tampa", "Thonotosassa","Valrico", "Wimauma", "Bay Pines", "Belleair Beach", "Clearwater", "Clearwater Beach", "Crystal Beach",
        "Dunedin", "Indian Rocks Beach", "Largo", "Oldsmar", "Ozona", "Palm Harbor", "Pinellas Park","Safety Harbor", "Saint Petersburg", "Seminole", "Tarpon Springs", "Aripeka", "Crystal Springs",
        "Dade City", "Holiday", "Hudson", "Lacoochee", "Land O Lakes", "New Port Richey", "Port Richey","Saint Leo", "San Antonio", "Spring Hill", "Trilby", "Wesley Chapel", "Zephyrhills", "fl",
        "florida", "swfl", "floridas", "manateecounty", "annamariaisland", "siestakey", "stpete", "sanibel", "everglades", "fortmyersbeach","manasotakey", "sarasotabay", "fortmyers", "lakeokeechobee", "bradentonbeach",
        "formyers", "bocagrande","siesta", "florda", "srq", "sarastoabay", "stpetersburg", "tampabay", "pinellascounty", "pineypoint", "clearwaterbeach", "capecoral", "gulfofmexico","portcharlotte","bay", "gulf","st pete", "St.Petersburg"
]
locations = [x.lower() for x in locations]

'''
Oil
'''
# the words used to search for oil tweets
oil_stop_words = ["oil", "crude", "petroleum", "tar ball", "tar balls","leak","leaks","leaked", "leaking", "leakage", "spill", "spills", "spilled", "spilling", "spillage", "ocean", "beach", "beaches", "bay", "gulf", "sea", "lake", "river", "creek", "waterway"]
c_oil = pd.read_csv("spill_data/Cleaned_Files/C_All_Oil.csv")
c_oil['text_with_display_links'] = c_oil['text_with_display_links'].astype(str)
c_oil_tw = ' '.join(c_oil['text_with_display_links'])

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocations=False, stopwords= locations + oil_stop_words).generate(c_oil_tw)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Oil Spill Non-Geo Word Cloud")
plt.show()

'''
Sewage
'''
sewage_stop_words=["sewer", "sewers", "sewage", "septic", "stormwater", "storm water", "reclaimed water", "reclaim water", "untreated", "raw", "overflow", "discharge", "discharges", "discharging", "discharged", "pump", "pumps", "pumping", "pumped", "leak", "leaks", "leaked", "leaking", "leakage", "spill", "spills", "spilled", "spilling", "spillage", "dump", "dumps", "dumped", "dumping","ocean", "beach", "beaches", "bay", "gulf", "sea", "lake", "river", "creek", "waterway"]
c_sewage = pd.read_csv("spill_data/Cleaned_Files/C_All_Sewage.csv")
c_sewage['text_with_display_links'] = c_sewage['text_with_display_links'].astype(str)
c_sewage_tw = ' '.join(c_sewage['text_with_display_links'])

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocations=False, stopwords=locations + sewage_stop_words).generate(c_sewage_tw)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Sewage Spill Non-Geo Word Cloud")
plt.show()

'''
Industrial
'''
industrial_stop_words = ["wastewater","contaminants", "contamination", "contaminating", "chemical", "chemicals", "discharge", "discharges", "discharging", "discharged", "pump", "pumps", "pumping", "pumped", "leak", "leaks", "leaked", "leaking", "leakage", "spill", "spills", "spilled", "spilling", "spillage","dump", "dumps", "dumped","dumping", "ocean", "beach", "beaches", "bay", "gulf", "sea", "lake", "river", "creek", "waterway"]
c_industrial = pd.read_csv("spill_data/Cleaned_Files/C_All_Industrial.csv")
c_industrial['text_with_display_links'] = c_industrial['text_with_display_links'].astype(str)
c_industrial_tw = ' '.join(c_industrial['text_with_display_links'])

# Generate WordCloud object
wordcloud = WordCloud(background_color='white', collocations=False, stopwords= locations + industrial_stop_words).generate(c_industrial_tw)

# Display the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Industrial Spill Non-Geo Word Cloud")
plt.show()