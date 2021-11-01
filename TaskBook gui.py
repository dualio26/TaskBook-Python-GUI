#Taskbook GUI interface 31/10/2021 by Eamon Green

from tkinter.constants import S
import PySimpleGUI as sg #Importing PySimpleGUI
import os #Importing OS for terminal interations
sg.theme('dark grey 9') #Set Terminal theme

# Define the window's contents
terminal = os.popen("tb").readlines()
tOutput = ""

layout = [  [sg.Text(tOutput.join(terminal), key='-OUTPUT-')],     #Widget component layout
            [sg.Input( enable_events=True,key='-INPUT-')],
            [sg.Button('Enter'), sg.Button('Quit')],
            [sg.Button('Submit', visible=False, bind_return_key=True)]]
# Create the window
window = sg.Window('Taskbook GUI', layout, icon='/favicon.ico')      #Window Defintion


#This will style the text similar to the terminal styling
#def Styling():
#    terminal = os.popen("tb").readlines()
#    i = 0
#    matched_indexes = []
#    length = len(terminal)
#    while i < length:
#        if any(f"  {i}." in s for s in terminal):
#            titles = [s for s in terminal if f"{i}." in s]
#            titles = [s + "\033[0;37;40m" for s in titles]
#            matched_indexes.append(i)
#            
#        i += 1
#    print(f'is present in terminal list at indexes {titles}')


# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit': #Quit program
        break
    # Output a message to the window
    elif event == 'Enter' or event == 'Submit': #Enter command to termianl and update window
        UsrInput = values['-INPUT-']
        if UsrInput == "": #If user enters nothing into prompt then the system returns tb
            terminal = os.popen("tb").readlines() #Stores terminal response to tb
            #terminal = Styling(terminal)
            #Styling()
            window['-OUTPUT-'].update(tOutput.join(terminal)) #Displays terminal output
        else: #Sends user input to terminal and returns terminal response
            terminal = os.popen(UsrInput).readlines()
            #terminal = Styling(terminal) #Styles response from terminal with color
            #Styling()
            window['-INPUT-']('')
            window['-OUTPUT-'].update(tOutput.join(terminal))

# Finish up by removing from the screen
window.close()