import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

entrada = tk.Entry(ventana)
entrada.pack(pady=5)

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except Exception as e:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")
        
boton_calcular = tk.Button(ventana, text="=", command=calcular)
boton_calcular.pack(pady=5)


boton_salir = tk.Button(ventana, text="AC", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()
