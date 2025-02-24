import PySimpleGUI as sg
import time

layout = [
    [sg.Text("Cronômetro:", size=(12, 1)), sg.Text(
        "00:00:00", key='-TEXTO-', size=(10, 1))],
    [sg.Button("Iniciar"), sg.Button("Continuar"),
     sg.Button("Parar"), sg.Button("Sair")]
]

rodando = False
inicio = 0
window = sg.Window('JAnela 1', layout)

while True:
    event, value = window.read(timeout=100)

    if event == sg.WIN_CLOSED or event == 'Sair':
        break

    if event == 'Iniciar':
        inicio = time.time()
        rodando = True

    if event == 'Parar':
        rodando = False

    if rodando:
        elapsed = int(time.time() - inicio)
        horas = elapsed // 3600
        minutos = (elapsed % 60) // 60
        segundos = elapsed % 60
        tempo_formatado = f"{horas:02}:{minutos:02}:{segundos:02}"
      
        window['-TEXTO-'].update(tempo_formatado)

window.close()
