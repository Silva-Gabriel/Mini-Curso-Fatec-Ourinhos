# Crie um algoritmo que receba um número inteiro e retorne o seu antecessor e o seu sucessor
numero = int(input('Digite um número: '))
antecessor = numero-1
sucessor = numero+1
print(f'\033[032mNúmero escolhido:{numero}\n'
      f'\033[034mAntecessor: {antecessor}\n'
      f'\033[033mSucessor: {sucessor}\n')
