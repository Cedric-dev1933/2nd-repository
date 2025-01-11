import tkinter as tk


def converter_temperatura():
    #Pegando o VALOR digitado em Entry e convertendo para float, par que a operação seja possivel
    celsius = float(entrada_celsius.get())
    #Conversão
    temperatura_fahrenheit = (celsius*1.8)+32
    #Configurando para a Label mostrar o resultado da conversão
    label.config(text=f"A temperatura é: {temperatura_fahrenheit:.2f}")


# Criação da janela principal
root = tk.Tk()
root.geometry("700x500")
root.title("Conversor de temperatura")

# Um Entry é como uma textbox
entrada_celsius = tk.Entry(root)
entrada_celsius.grid(row=0, column=0, padx=10, pady=5)


#Botão para converter a temperatura
botao_converter = tk.Button(root, text='Converter para Fahrenheit', command=converter_temperatura)
botao_converter.grid(row=1, column=0, columnspan=4, pady=10)

#Label para mostrar o resultado convertido
label = tk.Label(root, text="Temperatura em Fahrenheit: ")
label.grid(row=2, column=0, columnspan=4, pady=10)


root.mainloop()