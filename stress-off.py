# Start of the Stress-Off program
# Created by Angel Lazo-Gonzalez 

# User Greeting
print("Welcome to Stress-Off! This program will ask you a series of questions regarding your current feelings and symptoms.")
print("In answering these questions, this program will inform you of remedies and solutions in regards to reducing and helping out your stress.")
print("The goal in going through this program is to hopefully release some tension and get some assistance to help you in your current situation, I hope you enjoy the program and get what you were hoping out of it!")
     
# Stress symptoms explained
webmd_symptoms = ["Becoming easily agitated, feeling overwhelmed, avoiding others, headaches, aches and pains, chest pain, nervousness, dry mouth and difficulty swallowing, constant worrying, inability to focus, changes in appetite"]
stress_symptoms =  ", ".join (webmd_symptoms)
#Inform user of the most common symptoms found on Webmd
print("Based on the research from Webmb, the current most common symptons of stress are:", stress_symptoms)

#Establish repository for user responses
user_input = []
user_symptoms = []

#Program is about to inform user on how to insert their information
print("Hope everything is going swell so far, we are about to begin the questions included in our program today. Please type '1' for 'Yes' or '0' for 'No' for your responses.")
#Begin asking questions starting with symptom 1
symptom1 = input("Within the last few days or hours, have you noticed yourself getting easily agitated with others? ")
while True:
      if symptom1 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom1 == "0":
          break
      else:
          if symptom1 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom1 = input("Within the last few days or hours, have you noticed yourself getting easily agitated with others? ")
#End symptom 1

#Begin question for symptom 2
symptom2 = input("Within the last few days or hours, have you noticed yourself gaining an uneasy feeling of overwhelmingness? ")
while True:
      if symptom2 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom2 == "0":
          break
      else:
          if symptom2 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom2 = input("Within the last few days or hours, have you noticed yourself gaining an uneasy feeling of overwhelmingness? ")
#End symptom 2

#Begin question for symptom 3
symptom3 = input("Within the last few days or hours, have you noticed yourself start to avoid others? ")
while True:
      if symptom3 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom3 == "0":
          break
      else:
          if symptom3 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom3 = input("Within the last few days or hours, have you noticed yourself start to avoid others? ")
#End symptom 3

#Begin question for symptom 4
symptom4 = input("Within the last few days or hours, have you had any temple or frontal lobe headaches? ")
while True:
      if symptom4 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom4 == "0":
          break
      else:
          if symptom4 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom4 = input("Within the last few days or hours, have you had any temple or frontal lobe headaches? ")
#End symptom 4

#Begin question for symptom 5
symptom5 = input("Within the last few days or hours, have you had any aches or pains that are unusual for you? ")
while True:
      if symptom5 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom5 == "0":
          break
      else:
          if symptom5 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom5 = input("Within the last few days or hours, have you had any aches or pains that are unusual for you? ")
#End symptom 5

#Begin question for symptom 6
symptom6 = input("Within the last few days or hours, have you had any unusual chest pains? ")
while True:
      if symptom6 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom6 == "0":
          break
      else:
          if symptom6 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom6 = input("Within the last few days or hours, have you had any unusual chest pains? ")
#End symptom 6

#Begin question for symptom 7
symptom7 = input("Within the last few days or hours, have you felt more nervous than usual or consistent nervousness? ")
while True:
      if symptom7 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom7 == "0":
          break
      else:
          if symptom7 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom7 = input("Within the last few days or hours, have you felt more nervous than usual or consistent nervousness? ")
#End symptom 7

#Begin question for symptom 8
symptom8 = input("Within the last few days or hours, have you had a dry mouth or difficulty swallowing? ")
while True:
      if symptom8 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom8 == "0":
          break
      else:
          if symptom8 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom8 = input("Within the last few days or hours, have you had a dry mouth or difficulty swallowing? ")
#End symptom 8

#Begin question for symptom 9
symptom9 = input("Within the last few days or hours, have you experienced constant worrying? ")
while True:
      if symptom9 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom9 == "0":
          break
      else:
          if symptom9 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom9 = input("Within the last few days or hours, have you experienced constant worrying? ")
#End symptom 9

#Begin question for symptom 10
symptom10 = input("Within the last few days or hours, have you been experiencing the inability to focus on daily tasks? ")
while True:
      if symptom10 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom10 == "0":
          break
      else:
          if symptom10 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom10 = input("Within the last few days or hours, have you been experiencing the inability to focus on daily tasks? "
#End symptom 10
   
#Begin question for symptom 11
symptom11 = input("Within the last few days or hours, have you been experiencing a lack of appetite? ")
while True:
      if symptom11 == "1":
          user_input += ("1")
          user_symptoms.append("Becoming easily agitated")
          break
      elif symptom11 == "0":
          break
      else:
          if symptom11 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom11 = input("Within the last few days or hours, have you been experiencing a lack of appetite? "                                
#End symptom 11

#End symptom questions

#Analyze and format user responses#
for answer in range(0, len(user_responses)):
     user_input[answer] = int(user_input[answer])
user_symptoms_list =, ".join(user_symptoms)
#End analysis

#Statement summarizing what the program has gathered from the responses
print("Based on the answers you gave the program, you have experienced",sum(user_input),"symptom(s) of Stress: \n", user_symptom_list)
#Statemend ends
