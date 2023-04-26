# Python Challenge - Backend

Este desafio tem como objetivo testar os seus conhecimentos de desenvolvedor python e avaliar a sua forma de 
codificação e habilidades com as tecnologias propostas.

# Parking lot

![Parking lot](https://driving-tests.org/wp-content/uploads/2012/02/back-parking.jpg)

Jacks e seu pai compraram um terreno e vão inaugurar um estacionamento.

Para ajudar, o irmão de Jacks está desenvolvendo uma aplicação para controle de
estacionamento.

Quando o veículo entra no estacionamento, o atendente observa a sua placa e a mesma é registrada, juntamente com o 
modelo do veículo e a sua cor. A hora de entrada é gerada automaticamente, correspondendo ao momento de registro.

O cliente ao retornar para estacionamento informa a placa do veículo ao atendente para registro da saída. O tempo de 
permanência é calculado pelo sistema. Considerando esse tempo de permanência é aplicada a seguinte tabela de preços.

#### Tabela de Preços

Dias | Período | Valor/h
:--------- | :------: | :------:
Segunda - Sexta | 08:00 as 12:00 | R$ 2,00
Segunda - Sexta | 12:01 as 18:00 |  R$ 3,00
Sábado e domingo | 08:00 as 18:00 | R$ 2,50

Os donos precisam de relatórios de faturamento por período. Não aceitar entrada de veiculos fora do horario da tabela 
de preços.

# O que deve ser entregue
* Readme.md com instruções para iniciar ou buildar(caso esteja usando docker) o serviço.
* Readme.md com instruções de cada endpoint.
* Requirements.txt, caso não esteja em um ambiente docker.
* Python Notebook com o código.
* O Backend deve possuir um endpoint para entrada de veículos, onde ele receba a placa e registre o horario de entrada.
* O Backend deve possuir um endpoint para saída de veículos, onde ele receba a placa e devolva o valor a pagar. 
* O Backend deve possuir um endpoint para mostrar um relatório (pode ser apenas em json) que devolva um resumo de 
Faturamento X Dia.

Exemplo do json ( Você está livre parar alterar os campos e formatos ) 

```json
  [
    { "day":1572957282288, "revenues":125.5 5},
    ...
  ]
```

# Tecnologias Back-End (Obrigatório)
* Flask, Django;
* Banco de dados relacionais, 'SQL-based', preferencialmente postgresql;


# Diferenciais
* Realização de testes unitários;
* Utilização de Docker;
* Organização e clareza nas ideias;
* Um destaque maior para quem quiser desenvolver uma interface. Preferencialmente, procuramos alguém esteja apto a usar
 Pyqt, mas sinta-se a vontade de utilizar qualquer framework;
* Menos é mais, seja prático e não perca tempo com aspectos desnecessários;
* Este é apenas um roteiro, sinta-se a vontade de tomar as decisões que achar necessárias para desenvolver. Documente 
qualquer decisão ou mudança que achou necessário para a realização do projeto.

## Contatos

Use o contato abaixo para sanar quaisquer dúvidas.
* Tiago Custódio: [**tiago.custodio@itriad.org.br**](tiago.custodio@itriad.org.br)