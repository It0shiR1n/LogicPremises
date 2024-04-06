"""
Tabelas Verdades necessárias:

E

V V = V 
V F = F 
F V = F 
F F = F 


OU 

V V = V
V F = V 
F V = V 
F F = F


SE ENTÃO (IF)

V V = V 
V F = F
F V = V 
F F = V 


"""

print("Considerando as afirmações.\n")

print("1.Francisco é advogado e Gerson é analista. (FALSE)")           # 2
print("2.Gerson é analista ou Hugo é engenheiro. (TRUE)")              # 3 
print("3.Se Francisco é advogado então Igor é jornalista. (FALSE)")    # 4  
print("4.Se Joel é assistente, então Hugo não é engenheiro. (TRUE)")   # 1  
print("5.Se Lucas é técnico, então Joel é assistente. (TRUE)\n")       # 5

FranciscoAdvogado = True
GersonAnalista = False 
IgorJornalista = False 
JoelAssistente = False 
HugoEngenheiro = True
HugoNaoEngenheiro = False 
LucasTecnico = False 


if FranciscoAdvogado == True and IgorJornalista == False:
    if FranciscoAdvogado == True and GersonAnalista == False:
        if GersonAnalista == False and HugoEngenheiro == True:
            if JoelAssistente == False and HugoNaoEngenheiro == False:
                if LucasTecnico == False and JoelAssistente == False:
                    print("Franciso é Advogado")
                    print("Igor não é Jornalista")
                    print("Gerson não é analista")
                    print("Hugo é engenheiro")
                    print("Joel não é assistente")
                    print("Lucas não é técnico")

                else:
                    print("Lucas é tecnico e Joel é assistente")

            else:
                print("Joel é Assistente e Hugo não é engenheiro")

        else:
            print("Gerson é Analista e Hugo Não é engenheiro")

    else:
        print("Francisco não é Advogado e Gerson é Analista")

else:
    print("Francisco não é Advogado e Igor é jornalista")