def palindrom_test(ward):
    """
       Fukcja do sprawdzania czy dany wyraz jest palindromem
       argument funkcji naley podawać w "" lub ''
       wyrazy mogą być pisane z duej lub małej litery
       funkcja zwraca wartość boolean: True/False
    """
    ward_revers = ward[len(ward)::-1]
    return ward_revers.lower() == ward.lower()

print("Słowo %s jest palindromem: %s" %('Witek',palindrom_test('Witek')))
print("Słowo %s jest palindromem: %s" %('Potop',palindrom_test('Potop')))
