import main_cadastro
from moto import moto
from caminhao import caminhao
from carro import carro
from motorista import Motorista

main_cadastro.carregar_veiculos()

m = moto("ABC1D23", "Honda", "CG 160", 2020, 15000, 40,"Gasolina", 14, "Disponivel", 160)
main_cadastro.adicionar_veiculo(m)

main_cadastro.salvar_veiculos()
print(main_cadastro.buscar_veiculo("ABC1D23"))

c = caminhao("AAAXXXX","MERCEDES","QUEM SABE", 1992, 50000,50,"diesel",16,"Disponivel", "simples")
main_cadastro.adicionar_veiculo(c)

main_cadastro.salvar_veiculos()
print(main_cadastro.buscar_veiculo("AAAXXXX"))

car = carro("AAABBBB", "toyota","hilux",2014,30000,25,"diesel",12,"Disponivel",4)
main_cadastro.adicionar_veiculo(car)

main_cadastro.salvar_veiculos()
print(main_cadastro.buscar_veiculo("AAABBBB"))


main_cadastro.carregar_motoristas()

moto1 = Motorista("João","632.434.654-74", 56, "11111111111", "ab")
main_cadastro.adicionar_motorista(moto1)

main_cadastro.salvar_motoristas()
print(main_cadastro.buscar_motorista("632.434.654-74"))