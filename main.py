import tkinter as tk

def validation(conditions):

  true_values = 0
  false_values = 0
  
  # Verificação dos valores encontrados na tabela verdade

  for classification in conditions:
    
    if classification == True:
      true_values = true_values + 1

    if classification == False:
      false_values = false_values + 1

  output_text.insert(tk.END, f"\n  Classificação da proposição: \n")

  if (true_values > 0 and false_values == 0):
    output_text.insert(tk.END, f"             Tautologia\n")

  if (true_values == 0 and false_values > 0):
    output_text.insert(tk.END, f"             Contradição\n")

  if (true_values > 0 and false_values > 0):
    output_text.insert(tk.END, f"             Contigência\n")

def logicCalculator():

  output_text.config(state=tk.NORMAL, font=('Arial', 10, 'bold'), fg="#906090")
  output_text.delete(1.0, tk.END)

  # Faz um tratamento de exceção, caso esteja mal formulada, acusa erro
  
  try:
    
    expression = str(formula.get())
    
    variables = []; # Um vetor que irá armazenar quais variáveis foram digitadas na formúla
    variables_num = []; # Um segundo vetor que irá armazenar a quantidade de variáveis sem repetições

    expression_lower = expression.lower()

    for variable in expression_lower:
      if variable == "a" or variable == "b" or variable == "c" or variable == "d":
        variables.append(variable)

    variables_num = list(set(variables)) # Retorna uma lista com o número de varíaveis sem repetições

    # Substitui os símbolos da formula por comandos
    
    expression_lower = expression_lower.replace("∧", " and ")
    expression_lower = expression_lower.replace("∨", " or ")
    expression_lower = expression_lower.replace("¬", "not ")
    expression_lower = expression_lower.replace("→", ">>")
    expression_lower = expression_lower.replace("↔", "==")
    expression_lower = expression_lower.replace("⊻", "^")

    conditions = [] #Armazena o resultado de cada condição após a análise

    print(expression_lower)
      
    if (len(variables_num) > 4):
      output_text.insert(tk.END, "Quantidade de variáveis inválida.\n")

    else:

      # Após substituir os símbolos, gera-se uma expressão em string, mas que com o uso da função eval(), é possível converter essa string em uma instrução Python, permitindo sua execução

      if (len(variables_num) == 1):
        output_text.insert(tk.END, f"  | A | {expression} |\n")
        
        for a in range(0, 2):
          
          x = eval(expression_lower)
          #Adicionando o resultado da tabela verdade na lista
          
          if ">>" in expression_lower:

            # Por algum motivo, a implicação retorna os valores invertidos, mas na ordem correta. Com isso, no momento de exibição e de armazenamento dos resultados, o valor obtido é invertido
            output_text.insert(tk.END, f"  | {a} | {not x} |\n")
            conditions.append(not x)

          else:
            output_text.insert(tk.END, f"  | {a} | {x} |\n")
            conditions.append(x)


      if len(variables_num) == 2:
        
        output_text.insert(tk.END, f"  | A | B | {expression} |\n")

        for a in range(0, 2):
          for b in range(0, 2):
            
            x = eval(expression_lower)
            
            #Adicionando o resultado da tabela verdade na lista

            if ">>" in expression_lower:
              output_text.insert(tk.END, f"  | {a} | {b} | {not x} |\n")
              conditions.append(not x)

            else:
              output_text.insert(tk.END, f"  | {a} | {b} | {x} |\n")
              conditions.append(x)

      if len(variables_num) == 3:
        
        output_text.insert(tk.END, f"  | A | B | C | {expression} |\n")

        for a in range(0, 2):
          for b in range(0, 2):
            for c in range(0, 2):
              
              x = eval(expression_lower)

              if ">>" in expression_lower:
                output_text.insert(tk.END, f"  | {a} | {b} | {c} | {not x} |\n")
                conditions.append(not x)

              else:
                output_text.insert(tk.END, f"  | {a} | {b} | {c} | {x} |\n")
                conditions.append(x)

      elif len(variables_num) == 4:
        
        output_text.insert(tk.END, f"  | A | B | C | D | {expression} |\n")

        for a in range(0, 2):
          for b in range(0, 2):
            for c in range(0, 2):
              for d in range(0, 2):
                x = eval(expression_lower)

                if ">>" in expression_lower:
                  output_text.insert(tk.END, f"  | {a} | {b} | {c} | {d} | {not x} |\n")
                  conditions.append(not x)

                else:
                  output_text.insert(tk.END, f"  | {a} | {b} | {c} | {d} | {x} |\n")
                  conditions.append(x)

      # Chamada da função que retorna a classificação da proposição
      validation(conditions)

  except Exception as e:
    
    output_text.insert(tk.END, "\nA fórmula inserida está mal formulada")
    print(e)

    output_text.config(state=tk.DISABLED)


# Janela Principal

mainApp = tk.Tk()

mainApp.title("Calculadora Lógica")
mainApp.geometry("500x500")
mainApp["bg"] = "#301860"

# Label Fórmula

label = tk.Label(mainApp, text="Fórmula", bg="#483078", fg="white", font=('Arial', 10, 'bold'), width=15)
label.grid(row=0, column=0, ipadx=45, ipady=5)

# Entry Fórmula
formula = tk.Entry(mainApp, width=25, font=('Arial', 10, 'bold'), fg="#906090")
formula.grid(row=0, column=1, ipadx=45, ipady=5)

# Buttons

def button_insertA():
  formula.insert(tk.END, "A")

buttonA = tk.Button(mainApp, text="A", command=button_insertA)
buttonA.place(x=12, y=125)


def button_insertB():
  formula.insert(tk.END, "B")

buttonB = tk.Button(mainApp, text="B", command=button_insertB)
buttonB.place(x=47, y=125)


def button_insertC():
  formula.insert(tk.END, "C")

buttonC = tk.Button(mainApp, text="C", command=button_insertC)
buttonC.place(x=82, y=125)

def button_insertD():
  formula.insert(tk.END, "D")

buttonD = tk.Button(mainApp, text="D", command=button_insertD)
buttonD.place(x=117, y=125)

def button_insert1():
  formula.insert(tk.END, "∧")

button1 = tk.Button(mainApp, text="∧", command=button_insert1)
button1.place(x=12, y=153)

def button_insert2():
  formula.insert(tk.END, "∨")

button2 = tk.Button(mainApp, text="∨", command=button_insert2)
button2.place(x=47, y=153)

def button_insert3():
  formula.insert(tk.END, "¬")

button3 = tk.Button(mainApp, text="¬", command=button_insert3)
button3.place(x=82, y=153)

def button_insert4():
  formula.insert(tk.END, "→")

button4 = tk.Button(mainApp, text="→", command=button_insert4)
button4.place(x=117, y=153)

def button_insert5():
  formula.insert(tk.END, "↔")

button5 = tk.Button(mainApp, text="↔", command=button_insert5)
button5.place(x=12, y=180)

def button_insert6():
  formula.insert(tk.END, "⊻")

button6 = tk.Button(mainApp, text="⊻", command=button_insert6)
button6.place(x=47, y=180)

def button_insert7():
  formula.insert(tk.END, "(")

button7 = tk.Button(mainApp, text=" ( ", command=button_insert7)
button7.place(x=82, y=180)

def button_insert8():
  formula.insert(tk.END, ")")

button8 = tk.Button(mainApp, text=" )", command=button_insert8)
button8.place(x=117, y=180)

expression = str(formula.get())

buttonConfirm = tk.Button(mainApp, text="Gerar Tabela", bg="green", command=logicCalculator)
buttonConfirm.place(x=25, y=220)

info_label = tk.Label(mainApp,
                      text="Operadores",
                      bg="#906090",
                      fg="white",
                      font=('Arial', 10, 'bold'))

info_label.place(x=15, y=85, width = 140, height=25)

table_label = tk.Label(mainApp,
                      text="Tabela Verdade",
                      bg="#906090",
                      fg="white",
                      font=('Arial', 10, 'bold'))

table_label.place(x=250, y=85, width = 140, height=25)

output_text = tk.Text(mainApp, height=20, width=45)
output_text.place(x=170, y=125)

output_text.config(state=tk.NORMAL, font=('Arial', 10, 'bold'), fg="#906090")

mainApp.mainloop()