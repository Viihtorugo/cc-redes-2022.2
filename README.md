# Projeto final

Universidade Federal de Alagoas

Matéria: Redes

Para executar esse projeto é preciso que as máquinas tenham python instalado, além de estar conectados em uma mesma rede local.
Importante se alientar que o sistema operacional e a rede deve ter liberdade para utilizar a porta 12000, pois a mesma será utilizada para conexão!

## PASSO A PASSO DA CONEXÃO

### SERVIDOR

1. Em um computador descubra o IP do computador - por exemplo: 192.168.0.11
3. Abra o terminal
4. Vá para pasta do projeto e digite ```cd servidor```
5. Execute o arquivo python ```./servidor.py```
6. Só aguardar os clientes se conectarem!

### CLIENTE

1. Em outro computador, abra o terminal
2. Vá para pasto do projeto e digite ```cd cliente```
3. Dentro dessa pasta tem um arquivo cliente.py
4. Edite esse arquivo
5. Na linha 8 (ou procure por ```SERVER = ""```) e digite o IP da máquina do servidor (no exemplo seria ```SERVER = "192.168.0.11"```)
6. Execute o aquivo python ```./cliente.py```

## FUNCIONALIDADE

- No cliente você pode informar a função que você quer executar: Fatorial, Par ou Primo. Em seguida, quando solicitado, informe o número para a operação.
- No cliente, digite !EXIT para encerrar o processo.
- No servidor, pressione Ctrl+C para encerrar o processo.