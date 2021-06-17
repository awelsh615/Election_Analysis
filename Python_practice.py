counties_tuple=("Arapahoe","Denver","Jefferson")

#for county in counties_tuple:
#    print(county)

counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}

for key,value in counties_dict.items():
#    print(key,"county has", value, "registered voters.")
    print(f"{key} county has {value} registered voters.")
