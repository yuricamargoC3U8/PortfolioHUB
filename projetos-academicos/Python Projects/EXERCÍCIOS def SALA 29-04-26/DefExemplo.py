# def mostra_mensagem()
#     print("Exemplo de mensagem fixa em def.")
#
# if __name__ == "__main__":
#     print("Mensagem antes de chamar a função")
#     mostra_mensagem()
#     print("Mensagem dps da função")

def calcula_dobro(p_valor):
    dobro = p_valor * 2
    return dobro
if __name__ == '__main__':
    valor = int(input('Digite um valor: '))
    v_retornado = calcula_dobro(valor)
    print("valor retornado pela função: ", v_retornado)
