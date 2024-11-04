import tkinter as tk

def abrir_janela():
    janela2 = tk.Toplevel()
    janela2.title('Nova Janela')
    botao_fechar = tk.Button(janela2,text = 'Fechar Janela', command = janela2.destroy)
    botao_fechar.grid(row=0,column=0)


janela = tk.Tk()
janela.title('Uso Tkinter(Nova Janela)')

botao = tk.Button(janela,text = 'ir para outra janela', command = abrir_janela)
botao.grid(row = 0, column = 0)

janela.mainloop()
