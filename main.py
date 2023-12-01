import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', password='ant35accessdev?1', port='3306', db='menagerie')

c = conn.cursor()

c.execute('SELECT name, birth, MONTH(birth) AS birth_month FROM pet')

pet = c.fetchall()

name_width = 10
birth_width = 15
month_width = 10  # Adjust this width according to your preference

# Print the header with specified spacing
print(f"{'Name'.ljust(name_width)}{'Birth'.ljust(birth_width)}{'Month(birth)'.ljust(month_width)}")

# Display the data with specified spacing
for pets in pet:
    name = str(pets[0])
    birth = str(pets[1])
    birth_month = str(pets[2])

    print(f"{name.ljust(name_width)}{birth.ljust(birth_width)}{birth_month.ljust(month_width):>20}")


# for pets in pet:
#     print
#     print(pets)

# for pets in pet:
#     print(pets)

# name_width = 10
# owner_width = 10
# species_width = 12
# sex_width = 8
# birth_width = 15
# death_width = 10
#
# # Print the header with specified spacing
# print(f"{'Name'.ljust(name_width)}{'Owner'.ljust(owner_width)}{'Species'.ljust(species_width)}"
#       f"{'Sex'.ljust(sex_width)}{'Birth'.ljust(birth_width)}{'Death'.ljust(death_width)}")
#
# # Display the data with specified spacing
# for pets in pet:
#     print(f"{str(pets[0]).ljust(name_width)}{str(pets[1]).ljust(owner_width)}{str(pets[2]).ljust(species_width)}"
#           f"{str(pets[3]).ljust(sex_width)}{str(pets[4]).ljust(birth_width)}{str(pets[5]).ljust(death_width)}")
