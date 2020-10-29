"""
This program takes in a frequency
and calculates the length of a Double Bazooka Antenna, (coaxial dipole)
then creates a txt file and writes the results to the file 
it can be printed out
this can be helpful sometimes
happy antenna building.
"""
FREQUENCY = "Enter the Antenna Frequency: "
print("\n"*50)
print("--DOUBLE BAZOOKA ANTENNA--\n___________________________")
user = float(input(FREQUENCY))
FORMULA_TOTAL = 299.792458/user*0.9993*0.50
FORMULA_CENTRE = 299.792458/user*0.6595*0.50
END = (FORMULA_TOTAL-FORMULA_CENTRE)/2
FINAL_RESULT = f"""             your coaxial dipole length in metres
                    (frequency = {user} mHz)
                             total
          |------------------{FORMULA_TOTAL:.3f}------------------|
          -----------==========-==========-----------
          
                             centre
                    |--------{FORMULA_CENTRE:.3f}--------|         
          -----------==========-==========-----------
          |--{END:.3f}--|
          end length""".title()
print("\n"*50)
write_to_txt_file = open("bazooka.txt", "w") 
write_to_txt_file.write(FINAL_RESULT) 
print(FINAL_RESULT)      
print("\n"*3)
