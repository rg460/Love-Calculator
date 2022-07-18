# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# #Write your code below this line 👇
# # Plan
#  combine names
joined_str = name1 + name2;
# guard against the user inputing names in a certain way 
# turn joined_str into lower case
joined_str_lower_case = joined_str.lower();
#  create a count variable for TRUE
count_TRUE = 0;
#  check how many times  joined_str_lower_case has a T in it .
t = int(joined_str_lower_case.count("t"));
r = int(joined_str_lower_case.count("r"));
u = int(joined_str_lower_case.count("u"));
e = int(joined_str_lower_case.count("e"));
total_true = t + r + u + e;
print(total_true);

