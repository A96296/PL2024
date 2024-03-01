import sys

class SomadorOnOff:
    def __init__(self):
        self.somar = False
        self.numero_atual = 0

    def processar_texto(self, texto):
        resultado = ""
        for caractere in texto:
            if self.somar and caractere.isdigit():
                self.numero_atual += int(caractere)
            elif caractere.lower() == 'o':
                self.somar = True
            elif caractere.lower() == 'f':
                self.somar = False
            elif caractere == '=':
                resultado += str(self.numero_atual) + '\n'
                self.numero_atual = 0
            else:
                resultado += caractere
        return resultado

# Obter texto da linha de comando
entrada = ' '.join(sys.argv[1:])

# Criar uma instância do somador
somador = SomadorOnOff()

# Processar o texto e imprimir o resultado
resultado = somador.processar_texto(entrada)
print(resultado)
