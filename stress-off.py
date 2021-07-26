# Start of the Stress-Off program
# Created by Angel Lazo-Gonzalez 

# User Greeting
print("Welcome to Stress-Off! This program will ask you a series of questions regarding your current feelings and symptoms.)
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

#Begin questions for symptom 2
 
     
