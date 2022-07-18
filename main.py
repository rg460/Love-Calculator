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

## 🚨 Don't change the code below 👇
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
#  check how many times  joined_str_lower_case has a t,r,u,e in it .
t = int(joined_str_lower_case.count("t"));
r = int(joined_str_lower_case.count("r"));
u = int(joined_str_lower_case.count("u"));
e = int(joined_str_lower_case.count("e"));
# add together to get a total
total_true = t + r + u + e;
#  check how many times  joined_str_lower_case has a l,o,v,e in it .
l = int(joined_str_lower_case.count("l"));
o = int(joined_str_lower_case.count("0"));
v = int(joined_str_lower_case.count("v"));
e = int(joined_str_lower_case.count("e"));
total_love = l + o + v + e;

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
#  check how many times  joined_str_lower_case has a t,r,u,e in it .
t = (joined_str_lower_case.count("t"));
r = (joined_str_lower_case.count("r"));
u = (joined_str_lower_case.count("u"));
e = (joined_str_lower_case.count("e"));
# add together to get a total
total_true = t + r + u + e;
#  check how many times  joined_str_lower_case has a l,o,v,e in it .
l = (joined_str_lower_case.count("l"));
o = (joined_str_lower_case.count("0"));
v = (joined_str_lower_case.count("v"));
e = (joined_str_lower_case.count("e"));
total_love = l + o + v + e;
# calculate love score by concantenate the totals of true and love , convert both to strings
love_score = str(total_true) + str(total_love);
# print the users love score 
print(f"Your Love Score is {love_score}")




