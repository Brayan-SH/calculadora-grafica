import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera calculadora")
ventana.geometry("400x600")

label1 = tk.Label(ventana, text="¡Primer numero!", font=("Arial", 12, "bold"))
label1.pack(pady=5)
entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)

label2 = tk.Label(ventana, text="¡Segundo numero!", font=("Arial", 12, "bold"))
label2.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

label_resultado = tk.Label(ventana, text="Resultado:", font=("sans-serif", 12))
label_resultado.pack(pady=5)

def Sumar() :
  num1 = entrada1.get()
  entrada1.config(text=f"primer numero, {num1}!")
  
  num2 = entrada2.get()
  entrada2.config(text=f"segundo numero, {num2}!")

  resultado = float(num1) + float(num2)
  label_resultado.config(text=f"Resultado: {resultado}")

def Restar() :
  num1 = entrada1.get()
  entrada1.config(text=f"primer numero, {num1}!")
  
  num2 = entrada2.get()
  entrada2.config(text=f"segundo numero, {num2}!")

  resultado = float(num1) - float(num2)

  label_resultado.config(text=f"Resultado: {resultado}")

def Multiplicar() :
  num1 = entrada1.get()
  entrada1.config(text=f"primer numero, {num1}!")
  
  num2 = entrada2.get()
  entrada2.config(text=f"segundo numero, {num2}!")

  resultado = float(num1) * float(num2)
  label_resultado.config(text=f"Resultado: {resultado}")

def Dividir() :
  num1 = entrada1.get()
  entrada1.config(text=f"primer numero, {num1}!")
  
  num2 = entrada2.get()
  entrada2.config(text=f"segundo numero, {num2}!")

  if float(num2) != 0:
    resultado = float(num1) / float(num2)
  else:
    resultado = "Error: División por cero no permitida."

  label_resultado.config(text=f"Resultado: {resultado}")
  
  
def limpiar() :
  entrada1.delete(0, tk.END)
  entrada2.delete(0, tk.END)
  label_resultado.config(text="Resultado:")

# Boton sumar
boton_sumar = tk.Button(ventana, text="Sumar", command=Sumar)
boton_sumar.pack(pady=5)

# Boton restar
boton_restar = tk.Button(ventana, text="Restar", command=Restar)
boton_restar.pack(pady=5)

# Boton multiplicar
boton_multiplicar = tk.Button(ventana, text="Multiplicar", command=Multiplicar)
boton_multiplicar.pack(pady=5)

# Boton dividir
boton_dividir = tk.Button(ventana, text="Dividir", command=Dividir)
boton_dividir.pack(pady=5)

# Boton limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

# Boton salir
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack(pady=5)

ventana.mainloop()