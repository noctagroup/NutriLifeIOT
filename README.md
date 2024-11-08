# Contador de Passos com Microbit Integrado a um App de Nutrição

Este projeto permite monitorar os passos de um usuário utilizando um dispositivo **micro:bit** e integrar os dados em um aplicativo de nutrição. O contador de passos é gerenciado pelo micro:bit, e os dados gerados são coletados por um servidor Python e armazenados em um arquivo `.txt`, que serve como base para o aplicativo.

## 🚀 Estrutura do Projeto

- **`microbit.txt`**: Código que deve ser carregado no micro:bit para contar os passos.
- **`Blu.py`**: Código Python que deve ser executado no PC para receber os dados do micro:bit via Bluetooth.
- **`server.py`**: Código Python que deve ser executado no PC para salvar os dados em um arquivo `dadoos_pedometro.txt`.

## 🛠️ Requisitos

Antes de começar, verifique se você tem o seguinte instalado:

- **micro:bit** (com firmware adequado para Bluetooth)
- **Python 3.x** no seu PC
- **Bibliotecas Python**: `pyserial`, `flask`, ou outras dependências necessárias para comunicação e servidor.

### Instalar Dependências Python

Instale as bibliotecas necessárias com o seguinte comando:

bash
pip install pyserial flask

## 📦 Passos para Configuração
1. Carregar o Código no micro
Conecte o micro
ao seu PC via cabo USB.
Abra o arquivo microbit.txt e carregue o código no micro
. Esse código vai contar os passos utilizando o acelerômetro e enviar os dados para o PC através da porta serial.
2. Configuração do Servidor no PC
Baixe e extraia os arquivos do repositório para uma pasta no seu PC.

Abra o terminal ou prompt de comando na pasta onde os arquivos estão localizados.

Execute o código do servidor com o comando:

bash
Copiar código
python server.py
O servidor irá gerar um arquivo chamado dadoos_pedometro.txt, que conterá os dados dos passos.

3. Executar o Código de Comunicação via Cabo USB
Execute o código Blu.py no seu PC para iniciar a comunicação com o micro
via cabo USB. Esse código irá ler os dados da porta serial do micro
e passá-los para o servidor.

bash
Copiar código
python Blu.py
4. Integração com o App de Nutrição
O arquivo dadoos_pedometro.txt gerado pelo servidor pode ser acessado pelo aplicativo de nutrição, que usará esses dados para calcular o número de passos e exibi-los na interface do usuário.

⚠️ Observações
Conexão via Cabo USB: Certifique-se de que o micro
esteja corretamente conectado via cabo USB e que o computador reconheça a porta serial do dispositivo.
Servidor: O servidor Python (server.py) deve estar rodando continuamente enquanto o micro
estiver em uso para garantir a captura e armazenamento dos dados em tempo real.
Problemas com a Porta Serial: Caso haja algum problema na leitura da porta serial, verifique as configurações do micro
e as permissões do seu sistema operacional para acesso à porta serial.



