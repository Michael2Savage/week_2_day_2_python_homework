# Excersize 1
print("Excersize 1" + "\n")

the_list = [1,11,14,5,8,9]

for num in the_list:
    if num < 10:
        print(num)

print("")


# Excersize 2
print("Excersize 2" + "\n")

l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]

def l_merger(first_list, second_list):
    merged = first_list + second_list
    return sorted(merged)

print(f'{l_merger(l_1, l_2)} \n')


#Function Excersize
print("Function excersize")

#Write a function that combines 2 lists and generates first and last names.
# Input will be from first_name, then last_name, combining intop new list
# Output will be one new list with each item being a full name.

first_name = ['John', 'Evan', 'Jordan', 'Max']
last_name = ['Smith', 'Smith', 'Williams', 'Bell']

def full_name_list(firstnamelist, lastnamelist):
    fullname = []
    for name in fullname:
        fullname.append(first_name() + last_name())

    return fullname

print(full_name_list(first_name, last_name))

# I tried doing this extra part but 


