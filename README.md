# P2_CamadaFisicaComputacao_2021.2

<h2>Informações Gerais</h2>

<h3>Engenharia de Computação Insper - Camada Física da Computação 2021.2</h3>

<h3>Alunos:</h3>
<ul>
  <li><a href=https://www.linkedin.com/in/guilherme-rosada/>Guilherme Rosada</a></li>
  <li><a href=https://www.linkedin.com/in/marcosvinis//>Marcos Vinícius da Silva</a></li>
</ul>

<h3>Professor:</h3> 
<ul>
  <li><a href=https://www.insper.edu.br/pesquisa-e-conhecimento/docentes-pesquisadores/rodrigo-carareto/>Rodrigo Carareto</a></li>
</ul>

<h2>Informações da Atividade</h2>
<p>Neste projeto você deverá construir um código em Python para transmissão (client) e recepção (server) serial com uma resposta do server para o client.</p>

<h3>Objetivos:</h3>
<ul>
   <li>Você deverá ter duas aplicações distintas. Uma aplicação (client) deverá enviar via transmissão serial UART uma sequência de comandos que poderiam, por exemplo, controlar o estado da outra aplicação (server). A sequência deve ter entre 10 e 30 comandos, a ser determinada pelo client. O server não sabe a quantidade de comandos que irá receber. Após a recepção, o server deverá retornar ao client uma mensagem informando o número de estados que foram recebidos. Assim que o cliente receber a resposta com este número, poderá verificar se todos os estados foram recebidos, e o processo termina.</li>
   <li>O objetivo é fazer a transmissão no menor tempo possível, logo, o client deve iniciar um cronômetro no instante em que a aplicação se inicia. O cronômetro é parado após a verificação da resposta do server com o número de bytes correto. A transmissão deve ser feita com dois Arduinos. Cada aplicação irá se comunicar com um deles.</li>
</ul>
