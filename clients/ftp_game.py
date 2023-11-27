import terminal_api
import os
import time
import platform
settings_filename = 'client_settings.txt'

terminal = 'game'
console = terminal_api.console
console.print('Connecting to server...')

current_os = "Windows"
if platform.system() != "Windows":
    current_os = "Other"
    os.system('clear')
else:
    os.system('cls')
    os.system(f'mode con: cols={terminal_api.game_width} lines={terminal_api.game_height}')

if terminal_api.connect(terminal):
    console.print('Connected.')
    team_colour = terminal_api.team_colour

    terminal_api.prompt = f"[{team_colour}]FTP[/{team_colour}]@[{team_colour}]{terminal_api.game_ip_address}[/{team_colour}]>"

    message = ''

    while message != 'quit':
        message = console.input(terminal_api.prompt)
        if message == 'print':
            console.print(f'My IP: {terminal_api.game_ip_address}')
        else:
            terminal_api.send(message)
        time.sleep(0.2)
    terminal_api.disconnect()
else:
    console.print("Failed to connect.")