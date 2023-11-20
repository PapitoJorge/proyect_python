# EJERCICIO 1
# student_heights = input().split()

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])

# total_heights = 0
# for height in student_heights:
#     total_heights += height
    
# print(f"total height = {total_heights}")

# number_of_students = 0
# for student in student_heights:
#     number_of_students += 1
# print(f"number of students = {number_of_students}")

# average_students = round(total_heights / number_of_students)
# print(f"average of students = {average_students}")


#EJERCICIO 2
# student_score = input().split()
# for n in range(0, len(student_score)):
#     student_score[n] = int(student_score[n])

# highest_score = 0
# for score in student_score:
#     if score > highest_score:
#         highest_score = score

# print(f"the highest score {n} is {highest_score}")

#JERECICIO 4

# increment = 0
# for number in range(1, 101):
#     increment += number
# print(increment)

#JERECICIO 5

# target = int(input())

# suma_par = 0
# for number in range(2, target + 1, 2):
#     suma_par += number
# print(suma_par)

#JERECICIO 6

# print("Vamos a jugar al FizzBuzz")
# hasta = int(input("Hasta que número quieres jugar: "))

# for num in range(1, hasta + 1 ):
#     print(num)
#     intento = input("¿Qué sería?: ")
#     if num % 3 == 0 and intento != "Fizz":
#         print("ERROOOOOOR")
#     elif num % 5 == 0 and intento != "Buzz":
#         print("ERROOOOOOOR")

#PROYECTO

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

number = ['1', '2', '3', '4', '5', '6', '7' ,'8', '9', '0']

symbol = ['!', '?', '%', '$', '(', ')', '*', '+']

print("¡Bienvenido al creador de contraseñas seguras!")

n_letras = int(input("¿Cuántas letras quieres que tenga la contraseña?\n"))
n_numeros = int(input("¿Cuántos núumeros quieres que tenga la contraseña?\n"))
n_simbolo = int(input("¿Cuántos símbolos quieres que tenga la contraseña\n"))