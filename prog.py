def comprar_pao (preco = 1, dinheiro = 10); #O def será utilizado para definir a funçao. 
"""utilizamos underline na variável, pois o python não aceita variável aceita espaço dentro da variável podemos definir algumas fuções"""

     pao = int(input("Quantos pães você deseja comprar?" ))#definimos a variável pao,permitimos que ele responda utilizando o input. O int é utilizado para quando o usuário informar o número o python entenda que se trata de um número e não de texto assim permitindo realizar a conta"""
     
     total_da_compra = pao * preco"""variável total_da_compra criada para armazenar a multiplicação da quantidade de pães comprado e o valor do pão"""
      troco = total_da_compra - dinheiro
      
     print("O valor da compra é R$ " + total_da_compra)"""irá mostrar o valor total da compra para usuário"""
    
     
     if total_da_compra <= dinheiro :"""fara a validação do valor que o usuário possui com o valor total da compra então se a compra deu pr exemplo 12 reais e o usuário só possui 10, automaticamente o python entende que ele não possui dinheiro suficiente e passa para a proxima etapa o else"""
     
        print("O seu troco é de R$ " + troco +". Obrigado volte sempre!")
     else:
         print("Infelizmente não foi possivel realizar a compra. Sentimos muito")
