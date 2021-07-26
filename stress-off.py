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
