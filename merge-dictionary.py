fruits1 = {"Apple" : 100, "Banana" : 24}

fruits2 = {"Mango" : 80, "Orange" : 48}

merged = {}

for key in fruits1:

    merged[key] = fruits1[key]

for key in fruits2:

    merged[key] = fruits2[key]

print("Merged fruits dictionary is => ",  merged)