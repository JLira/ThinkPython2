"""
  3.1 Escreva uma função chamada right_justify, que receba uma string chamada s como parametro
  e exiba a string com espaços suficientes à frente para que a ultima letra da string esteja na
  coluna 70 da tela
"""
def rigth_justify(s,n=70):
   return  (' ' * len(s) + s[:])*(n//(len(s)*2))

rigth_justify('monty')
