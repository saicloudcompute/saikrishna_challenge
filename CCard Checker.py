import re


#x = "4378-1234-1234-1234"
#x = "8678-1234-1234-1234"
x = "4444-4444-4444-4444"

pattern = re.compile(r"((^[456][0-9]{3})-([0-9]{4})-([0-9]{4})-([0-9]{4}$))")
repeats = re.compile(r"(\d)\1{3}")


if (pattern.search(x) and (not repeats.search(x.replace("-", "")))): 
    print("valid") 
else: 
    print("invalid")
