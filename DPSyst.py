import tkinter as tk
from tkinter import scrolledtext
import subprocess

#Função para executar um script e exibir a saida na interface
def executar_script(caminho_script):
    #Limpar a área de texto antes de rodar o próximo script
    prompt_area.delete(1.0, tk.END)

    #Executar o script e capturar a saída.
    try:
        resultado = subprocess.run(['python', caminho_script], capture_output=True, text=True)
        #Verifique se a variável 'resultado' foi criada corretamente
        if resultado:
        #Exibir a saída no prompt
            prompt_area.insert(tk.END, resultado.stdout)
            prompt_area.insert(tk.END, resultado.stderr)
        else:
            prompt_area.insert(tk.END, "Erro: Nenhuma saída foi capturada.")
    except Exception as e:
        prompt_area.insert(tk.END, f"Erro ao executar o script: {e}")

#Criar a janela principal
janela = tk.Tk()
janela.title("DPSystem")
janela.geometry("500x400")

#Botões para o script
botao1 = tk.Button(janela, text="RenoPDF", command=lambda: executar_script('renopdf.py'))
botao1.pack(pady=10)

botao2 = tk.Button(janela, text="Busca de Protocolos", command=lambda: executar_script('Users/Zito/Desktop/renopdf.py'))
botao2.pack(pady=10)

botao3 = tk.Button(janela, text="Controle de Chamado", command=lambda: executar_script('Users/Zito/Desktop/renopdf.py'))
botao3.pack(pady=10)

#Área de texto para exibir a saída (como um prompt)
prompt_area = scrolledtext.ScrolledText(janela, width=60, height=10)
prompt_area.pack(pady=20)

#Iniciar o loop da interface
janela.mainloop()
