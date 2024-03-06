
def rename(name):
        if "StatTrak™" in name:
            rename = name.split("StatTrak™")[1].split("(")[0]
        elif "Souvenir" in name:
             rename = name.split("Souvenir")[1].split("(")[0]
        else:
            rename = name.split("(")[0]

        if len(rename) >= 22:
            rename = rename[:26]
            return rename
        else:
             return rename
        
print(rename("StatTrak™ Desert Eagle | Kumicho"))
