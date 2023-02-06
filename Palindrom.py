def palindrom_test(ward):
    ward_revers = ''
    ward = str(ward)
    for i in range(1,len(ward)+1):
        ward_revers += ward[-i]
    print(ward_revers.lower() == ward.lower())
    print(ward_revers.lower())
palindrom_test('Witek')