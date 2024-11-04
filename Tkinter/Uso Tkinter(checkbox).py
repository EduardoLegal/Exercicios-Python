import tkinter as tk

janela = tk.Tk()
janela.title('Checkbox')

def enviar():
    if var_promocoes.get():
        print('O usuário deseja receber promoções')
    else:
        print('O usuário NÃO deseja receber promoções')

    if var_termos.get():
        print('O usuário concordou com os termos de Uso e Políticas de Privacidade')
    else:
        print('O usuário NÃO concordou')

        


var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text = 'Deseja Receber e-mail promocionais?', variable = var_promocoes)
checkbox_promocoes.grid(row = 0, column = 0)

var_termos = tk.IntVar()
checkbox_termos = tk.Checkbutton(text = "Aceitar os termos de Uso e Políticas de Privacidade", variable = var_termos)
checkbox_termos.grid(row = 1, column = 0)



botao_enviar = tk.Button(text = 'Enviar',command=enviar)
botao_enviar.grid(row = 2,column = 0)


janela.mainloop()