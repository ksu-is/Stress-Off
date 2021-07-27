# Start of the Stress-Off program
# Created by Angel Lazo-Gonzalez 

# User Greeting
print("Welcome to Stress-Off! This program will ask you a series of questions regarding your current feelings and symptoms.")
print("In answering these questions, this program will inform you of remedies and solutions in regards to reducing and helping out your stress.")
print("The goal in going through this program is to hopefully release some tension and get some assistance to help you in your current situation, I hope you enjoy the program and get what you were hoping out of it!")
     
# Stress symptoms explained
webmd_symptoms = ["Becoming easily agitated, feeling overwhelmed, avoiding others, headaches, aches and pains, chest pain, nervousness, dry mouth and difficulty swallowing, constant worrying"]
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
          user_symptoms.append("feeling overwhelmed")
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
          user_symptoms.append("avoiding others")
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
          user_symptoms.append("headaches")
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
          user_symptoms.append("aches or pains")
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
          user_symptoms.append("chest pain")
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
          user_symptoms.append("nervousness")
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
          user_symptoms.append("dry mouth and difficulty swallowing")
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
          user_symptoms.append("constant worrying")
          break
      elif symptom9 == "0":
          break
      else:
          if symptom9 != "1" or "0":
               print("Input is incorrect, please remember to enter '1' for 'Yes' or '0' for 'No'.")
               symptom9 = input("Within the last few days or hours, have you experienced constant worrying? ")
#End symptom 9

#End symptom questions

#Analyze and format user responses#
for answer in range(0, len(user_input)):
     user_input[answer] = int(user_input[answer])
user_symptoms_list =", ".join(user_symptoms)
#End analysis

#Statement summarizing what the program has gathered from the responses
print("Based on the answers you gave the program, you have experienced",sum(user_input),"symptom(s) of Stress: \n", user_symptoms_list)
#Statemend ends

#Recommendations and use of Stress-Off-Link to assist individual

#Recommendations for individuals that have 3 or more symptoms of Stress
if sum(user_input) > 3:
    print("You have indicated from your inputs that you have experienced at least 3 of the symptoms of Stress.")
    
    if "headaches" in user_symptoms:
        if "chest pain" in user_symptoms:
             print("By informing the program that you have experienced chest pain and headaches, two of the more severe symptoms of stress, you should stop what you are doing and take a deep breath.")
        else:
            print("By indicating that you have are experiencing headaches, one of the more serious symptoms of Stress, you should stop what you are doing and take a deep breath. ")
    
    print("Because of information, we are transmitting you to a website in hopes of relieving your symptoms. ")
    import stress_off_link_2 as stress_off_link
    stress_off_link

#Recommendations for individuals that are experiencing less than 3 symptoms of Stress
if sum(user_input) <= 3:
    print("You have indicated from your inputs that you have experienced less than 3 of the symptoms of Stress.")
    
    if "headaches" in user_symptoms:
        if "chest pain" in user_symptoms:
             print("By informing the program that you have experienced chest pain and headaches, two of the more severe symptoms of stress, you should stop what you are doing and take a deep breath.")
        else:
            print("By indicating that you have are experiencing headaches, one of the more serious symptoms of Stress, you should stop what you are doing and take a deep breath. ")
    
    print("I will also inform you since you are experiencing less than 3 symptoms of stress, that perhaps your symptoms are not stress after all. I would highly advise a visit to your local urgent care facility! ")
    print("No matter how many symptoms of stress you are experiencing, I highly recommend the link that you are being transmitted too. Remember to breath! ")
    import stress_off_link_2 as stress_off_link
    stress_off_link

# End recommendations regarding two most severe symptoms of Stress


#Exit statement
print("Thank for you using my Stress-Off program!")
print("This project was created and sampled from a former group of KSU students that also took Dr. Thomas' IS3020 course at KSU.")
print("For every student that is experiencing stress, find an outlet, find someone, find something that can take your mind off of what is running through your head.")
print("By completing this program, regardless of stress or not, you should have achieved one minute of distraction from what was going on around you!")

#Code ends
