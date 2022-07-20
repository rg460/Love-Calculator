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
int_love_score = int(love_score)
# if statement to dertemine the users love score and phrase to go with love score
if (int_love_score < 10) or (int_love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (int_love_score >= 40) and (int_love_score <= 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
    


