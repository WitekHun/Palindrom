def palindrom_test(ward):
    """
       Fukcja do sprawdzania czy dany wyraz jest palindromem
       argument funkcji naley podawać w "" lub ''
       wyrazy mogą być pisane z duej lub małej litery
       funkcja zwraca wartość boolean: True/False
    """
    ward_revers = ''
    ward = str(ward)
    for i in range(1,len(ward)+1):
        ward_revers += ward[-i]
    print(ward_revers.lower() == ward.lower())
    return(ward_revers.lower() == ward.lower())
palindrom_test('Witek')