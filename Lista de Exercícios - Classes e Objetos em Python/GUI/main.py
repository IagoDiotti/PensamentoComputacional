import tkinter as tk



def clique():
    if rotulo.cget("text") != "Olá, mundo!":
        rotulo.config(text="Olá, mundo!")
    else:
        rotulo.config(text="Olá, turma!")
    


janela = tk.Tk()
janela.title("Exemplo botão")
janela.geometry("600x400")
rotulo = tk.Label(janela, text="Olá", font=("Arial", 16))
rotulo.pack(pady=20)
botao = tk.Button(janela, text="Clique aqui", command=clique)
botao.pack(pady=20)
janela.mainloop()


