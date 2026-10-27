# PDV - Sistema de Ponto de Venda

## O que o código faz

Este programa simula um sistema simples de Ponto de Venda (PDV). Ele recebe o valor de cada compra e a idade do cliente, aplica os descontos previstos, exibe o valor final e registra as compras. Quando o usuário digita `0` no valor da compra, o programa encerra o atendimento e apresenta um resumo do dia com a quantidade de compras, o total bruto, os descontos concedidos e o total final.

## Como ele faz

1. O programa solicita o valor da compra. Se o usuário digitar `0`, o loop termina.
2. Se o valor da compra for negativo, o programa exibe um aviso e solicita uma nova compra.
3. Para valores válidos, o programa solicita a idade do cliente. Se a idade for negativa, exibe um aviso e volta ao início do loop.
4. Se a idade for maior ou igual a 65 anos, aplica um desconto de 20% sobre o valor da compra.
5. Depois do desconto por idade, verifica se o valor restante é maior que R$ 100,00. Se for, aplica um desconto adicional de 10% sobre esse valor.
6. O programa calcula o desconto total, exibe o valor original, o desconto e o valor final.
7. Cada compra é armazenada em uma lista usando `.append()`.
8. Ao encerrar, o programa calcula e exibe a quantidade de compras, o total bruto, o total de descontos e o total final.

## Como rodar

No terminal execute:

'python pdv.py'

## Tabela de exemplos

Exemplo de compra de R$ 200,00 para um cliente de 65 anos:

| Etapa | Valor |
|---|---:|
| Valor original | R$ 200,00 |
| Após 20% de desconto por idade | R$ 160,00 |
| Após 10% de desconto extra | R$ 144,00 |
| **Valor final** | **R$ 144,00** |
