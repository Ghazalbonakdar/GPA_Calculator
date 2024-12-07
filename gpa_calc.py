def gpa_calc(number_subjects):
    total_gpa = 0
    total_units = 0
    for subjects in range(1,number_subjects+1):
        #taking the inputs
        gpa_units = input().split()
        gpa_units_int = list(map(int,gpa_units))
        gpa, units = gpa_units_int

        #implementing the formula
        total_gpa += gpa * units
        total_units += units
    return round(total_gpa/total_units, 2)








print(gpa_calc(3))




