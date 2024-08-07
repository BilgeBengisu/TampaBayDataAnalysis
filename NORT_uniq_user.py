import pandas as pd
import re
import operator
#https://docs.python.org/3/library/collections.html#collections.defaultdict
from collections import defaultdict
from wordcloud import WordCloud

import matplotlib.pyplot as plt

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
        "formyers", "bocagrande","siesta", "florda", "srq", "sarastoabay", "stpetersburg", "tampabay", "pinellascounty", "pineypoint", "clearwaterbeach", "capecoral", "gulfofmexico","portcharlotte","bay", "gulf","st","pete", "St.Petersburg", "petersburg", "mexico"
]
locations = [location.lower() for location in locations] 
locations = [re.sub(r'[()]', '', location) for location in locations] # to remove "(" and ")"
locations = [word for location in locations for word in location.split()]

# getting & preparing the files
c_oil = pd.read_csv("spill_data/Cleaned_NORT_Files/C_NORT_Oil.csv")
c_sewage = pd.read_csv("spill_data/Cleaned_NORT_Files/C_NORT_Sewage.csv")
c_industrial = pd.read_csv("spill_data/Cleaned_NORT_Files/C_NORT_Industrial.csv")
oil_stop_words = ["oil", "crude", "petroleum", "tar ball", "tar balls","leak","leaks","leaked", "leaking", "leakage", "spill", "spills", "spilled", "spilling", "spillage", "ocean", "beach", "beaches", "bay", "gulf", "sea", "lake", "river", "creek", "waterway"]
industrial_stop_words = ["wastewater","contaminants", "contamination", "contaminating", "chemical", "chemicals", "discharge", "discharges", "discharging", "discharged", "pump", "pumps", "pumping", "pumped", "leak", "leaks", "leaked", "leaking", "leakage", "spill", "spills", "spilled", "spilling", "spillage","dump", "dumps", "dumped","dumping", "ocean", "beach", "beaches", "bay", "gulf", "sea", "lake", "river", "creek", "waterway"]
sewage_stop_words=["wastewater", "sewer", "sewers", "sewage", "septic", "stormwater", "storm water", "reclaimed water", "reclaim water", "untreated", "raw", "overflow", "discharge", "discharges", "discharging", "discharged", "pump", "pumps", "pumping", "pumped", "leak", "leaks", "leaked", "leaking", "leakage", "spill", "spills", "spilled", "spilling", "spillage", "dump", "dumps", "dumped", "dumping","ocean", "beach", "beaches", "bay", "gulf", "sea", "lake", "river", "creek", "waterway"]


def get_freq_unique_user(df, stop_words):
    word_freq_unique_users = defaultdict(int)
    word_users = defaultdict(set)

    for _, row in df.iterrows():  # Using "_" to ignore the index
        username = row['username']  # unique usernames
        text = row['text_with_display_links'] #the tweets
        if not pd.isna(text): #accounting for float values
            words = text.split()
            for word in words:
                word = word.lower().strip("'.,!?#$&();")
            # Check if this user has already used this word
                if word not in locations and word not in stop_words:
                    if username not in word_users[word]:
                        # If not, increase the count of this word and mark this user as having used it
                        word_freq_unique_users[word] += 1
                        word_users[word].add(username)
    dict = sorted(word_freq_unique_users.items(), key=lambda x: x[1], reverse = True)
    for word, freq in dict[0:29]:
        print(f"'{word}' appeared {freq} times")
    return word_freq_unique_users


# Oil

oil_freq = get_freq_unique_user(c_oil, oil_stop_words)
wc = WordCloud(background_color="white",collocations=False, max_words=1000).generate_from_frequencies(oil_freq)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Oil Spill Unique User No RT Tweet Analysis")
plt.show()

# Sewage
sewage_freq = get_freq_unique_user(c_sewage, sewage_stop_words)
wc = WordCloud(background_color="white",collocations=False, max_words=1000).generate_from_frequencies(sewage_freq)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Sewage Spill Unique User No RT Tweet Analysis")
plt.show()

# Industrial
sewage_freq = get_freq_unique_user(c_sewage, sewage_stop_words)
wc = WordCloud(background_color="white",collocations=False, max_words=1000).generate_from_frequencies(sewage_freq)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("Industrial Spill Unique User No RT Tweet Analysis")
plt.show()