year = int(input("Sisesta aasta: "))

if (year % 400) == 0 or ((year % 4) == 0 and (year % 100)):
    print(year, "on liigaasta")
    
else: 
    print(year, "ei ole liigaasta")