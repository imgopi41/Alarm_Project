# Importing necessary libraries
import playsound #library to play tunes/sounds
import datetime #using datetime library because we are dealing with hours and minutes

alarmHour = int(input("Enter the Hour: "))#asking user to enter the hour
alarmMin = int(input("Enter the Minute: "))#asking user to enter the minute
Am_or_Pm = input("Am or Pm: ")#asking user to enter am_or_pm
# os.system('clear')
print("Waiting for time to ring", alarmHour, alarmMin, Am_or_Pm)
#checking  for 12 hours or 24 hours format
if(Am_or_Pm == "Pm"):
    alarmHour = alarmHour + 12
while(1):
    # setting current time
    if(alarmHour == datetime.datetime.now().hour and       
        alarmMin == datetime.datetime.now().minute):
        print("Time for Workout")
        playsound.playsound(r"beep.mp3") #alarm sound to play
        break