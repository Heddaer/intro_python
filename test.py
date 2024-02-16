# TIPS
# comment shortcut: command + shift + /


# Apply the  input function
# user_input = input("What is your name?"
# print(user_input)


# Creating variables 
# 9
num_candidates = 3
# winning_percentage = 73.81
# candidate = "Diane"
# won_election = True

# tally_local_werewolves = 10
# werewolf_name = "Billy"
# is_werewolf = False

# Conditional logic

# user_howl = int(input("Please input an integer of 0 or greater. "))

# if user_howl > 0:
#     print("You may be a werewolf.")
# else:
#     print("Congrats, you are not a werewolf.")


# NESTED else if
# What is the score?
# score = int(input("What is your test score?"))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')

# ELIF 
# What is the score?
score = int(input("What is your test score?"))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')