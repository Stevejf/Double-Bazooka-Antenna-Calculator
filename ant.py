"""
This program takes in a frequency
and calculates the length of a Double Bazooka Antenna, (coaxial dipole)
then creates a txt file and writes the results to the file 
it can be printed out
this can be helpful sometimes
opening the txt file in wordpad worked better than notepad for me
happy antenna building.
"""
frequency = "Enter the Antenna Frequency: "
print("\n"*50)
print("--DOUBLE BAZOOKA ANTENNA--\n___________________________")
user = float(input(frequency))
formula_total = 299.792458/user*0.9993*0.50
formula_centre = 299.792458/user*0.6595*0.50
end = (formula_total-formula_centre)/2
final_result = f"""             
               your coaxial dipole length in metres
                    (frequency = {user} mHz)
                         total length
          |------------------{formula_total:.3f}------------------|
          -----------==========-==========-----------    
                         braid length
                    |--------{formula_cantre:.3f}-------|         
          -----------==========-==========-----------
          |--{end:.3f}--|          |--------{formula_total/2:.3f}--------|
          end length                  half length""".title()
print("\n"*50)
write_to_txt_file = open("bazooka.txt", "w") 
write_to_txt_file.write(final_result) 
write_to_txt_file.close()
print(final_result)      
print("\n"*3)
