def leap_year():
    year = int(input("Ingrese el año: "))
    print(year)
    if year%4 == 0:
        if year%100 == 0  and year%400 == 0:
         print(f"El año {year} es bisiesto")
       
        elif year%100 != 0:
            print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")
