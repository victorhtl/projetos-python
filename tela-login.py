from PySimpleGUI import PySimpleGUI as sg

# Layout (Consulte os vários tipos de temas existentes)
sg.theme('Reddit')

# Janela, recebe o título e o resto do layout
janela = sg.Window('Tela de Login', 
    layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Entrar')] # o botão retorna a própria string
])

while True:
    eventos,  valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        # Aqui entraria a base de dados de usuários cadastrados:
        if valores['usuario'] == 'Victor' and valores['senha'] == '123456':
            print('Abre as outras partes da aplicação')