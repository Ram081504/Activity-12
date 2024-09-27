Land_Animal_Speed_list = [
    ("Lion", "80 km/h"),
    ("Tiger", "65 km/h"),
    ("Elephant", "40 km/h"),
    ("Giraffe", "56 km/h"),
    ("Horse", "70 km/h"),
    ("Zebra", "65 km/h"),
    ("Kangaroo", "70 km/h"),
    ("Rabbit", "55 km/h"),
    ("Fox", "50 km/h"),
    ("Gazelle", "80 km/h"),
    ("Wildebeest", "65 km/h"),
    ("Coyote", "65 km/h")
]
print("A. Entire list:", Land_Animal_Speed_list)
print("B. 7th index is:", Land_Animal_Speed_list[6])
Land_Animal_Speed_list[8] = "Cheetah - 120 km/h"
print("C. Updated List:", Land_Animal_Speed_list)
del Land_Animal_Speed_list[9]
print("D. Updated List:", Land_Animal_Speed_list)
print("E. Sliced Portion:", Land_Animal_Speed_list[2:7])
print("F. Last Index Is:", Land_Animal_Speed_list[-1])