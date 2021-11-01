import PySimpleGUI as sg

sg.change_look_and_feel('GreenTan')
color_list = sg.list_of_look_and_feel_values()
color_list.sort()
layout = [[sg.Text('Theme Browser')],
          [sg.Text('Click on a theme.')],
          [sg.Listbox(values=color_list,
                      size=(20, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]]

window = sg.Window('Look and Feel Browser', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break

    themeNow = values['-LIST-'][0]
    sg.theme(themeNow)
    sg.change_look_and_feel(themeNow)
    window.refresh()
    sg.popup("Changed theme to " + themeNow)

window.close()