Continent_Country_list = [
    ("Argentina", "South America"),
    ("Brazil", "South America"),
    ("Canada", "North America"),
    ("China", "Asia"),
    ("Egypt", "Africa"),
    ("France", "Europe"),
    ("Germany", "Europe"),
    ("India", "Asia"),
    ("Japan", "Asia"),
    ("Mexico", "North America"),
    ("Nigeria", "Africa"),
    ("Russia", "Europe"),
    ("South Africa", "Africa"),
    ("United Kingdom", "Europe"),
    ("United States", "North America")
]
print("A. Entire list:", Continent_Country_list)
print("B. 9th index is:", Continent_Country_list[8])
Continent_Country_list[9] = "Australia"
print("C. Updated List:", Continent_Country_list)
del Continent_Country_list[11]
print("D. Updated List:", Continent_Country_list)
print("E. Sliced Portion:", Continent_Country_list[3:8])
print("F. Last Index Is:", Continent_Country_list[-1])