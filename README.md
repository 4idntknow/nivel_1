Este programa simula um PDV (Ponto de Venda) que calcula descontos progressivos em compras. A cada compra, o usuário informa o valor e a idade do cliente. O programa aplica 20% de desconto para clientes com 65 anos ou mais e, em seguida, 10% de desconto extra se o valor já descontado for maior que R$ 100,00. O valor final de cada compra é exibido no console, e o programa permite registrar várias compras seguidas até o usuário digitar 0 no valor da compra. Ao encerrar, ele mostra um resumo do dia com a quantidade de compras registradas, o total bruto, o total de descontos concedidos e o total final.


Como ele faz

1. Cria duas listas vazias, uma para os valores originais e outra para os valores finais, e um contador de descontos.
2. Entra em um loop que pede o valor da compra. Se o valor for 0, o loop termina.
3. Se o valor ou a idade forem negativos, exibe um aviso e pede novamente.
4. Guarda o valor original na lista com .append().
5. Verifica se a idade é maior ou igual a 65 e, se for, aplica 20% de desconto.
6. Verifica se o valor já descontado passa de R$ 100,00 e, se passar, aplica mais 10%.
7. Exibe o valor final formatado em reais e guarda esse valor na segunda lista com .append().
8. Ao encerrar o loop, soma as listas e mostra o resumo: quantidade de compras, total bruto, total de descontos (total bruto menos total final) e total final.

Como rodar: python pdv.py.

Tabela de casos:

| # | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---|------------|-------|----------------|----------------|----------------------|
| 1 | 50.00 | 30 | 0% | 0% | R$ 50.00 |
| 2 | 100.00 | 30 | 0% | 0% | R$ 100.00 |
| 3 | 80.00 | 65 | 20% | 0% | R$ 64.00 |
| 4 | 100.00 | 70 | 20% | 0% | R$ 80.00 |
| 5 | 125.00 | 70 | 20% | 0% | R$ 100.00 |
| 6 | 200.00 | 30 | 0% | 10% | R$ 180.00 |
| 7 | 101.00 | 30 | 0% | 10% | R$ 90.90 |
| 8 | 200.00 | 65 | 20% | 10% | R$ 144.00 |
| 9 | 1000.00 | 80 | 20% | 10% | R$ 720.00 |
| 10 | 200.00 | 64 | 0% | 10% | R$ 180.00 |