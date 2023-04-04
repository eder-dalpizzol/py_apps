# # -*- coding: utf-8 -*-
# import sqlite3
# import threading
# from nicegui import ui

# conn = sqlite3.connect('exemplo.db')
# cursor = conn.cursor()
# cursor.execute('CREATE TABLE IF NOT EXISTS clientes (id INTEGER PRIMARY KEY, nome TEXT, email TEXT)')

# def adicionar_cliente():
#     def capturar_entrada():
#         nome = input('Digite o nome do cliente:')
#         email = input('Digite o email do cliente:')
#         cursor.execute('INSERT INTO clientes (nome, email) VALUES (?, ?)', (nome, email))
#         conn.commit()
#         ui.alert('Cliente adicionado com sucesso!')
        
#     threading.Thread(target=capturar_entrada).start()

# def listar_clientes():
#     cursor.execute('SELECT * FROM clientes')
#     clientes = cursor.fetchall()
#     ui.alert('Lista de clientes:', '\n'.join(str(cliente) for cliente in clientes))

# with ui.card():
#     ui.button('Adicionar cliente', on_click=adicionar_cliente)
#     ui.button('Listar clientes', on_click=listar_clientes)

# ui.run()
import os

path = os.path.join(os.path.expanduser("~"), "Downlads")
print(path)
