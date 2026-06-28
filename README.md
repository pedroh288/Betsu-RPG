```text
>>======================================================<<
||                                                      ||
||  $$$$$$$\  $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\   $$\   ||
||  $$  __$$\ $$  _____|\__$$  __|$$  __$$\ $$ |  $$ |  ||
||  $$ |  $$ |$$ |         $$ |   $$ /  \__|$$ |  $$ |  ||
||  $$$$$$$\ |$$$$$\       $$ |   \$$$$$$\  $$ |  $$ |  ||
||  $$  __$$\ $$  __|      $$ |    \____$$\ $$ |  $$ |  ||
||  $$ |  $$ |$$ |         $$ |   $$\   $$ |$$ |  $$ |  ||
||  $$$$$$$  |$$$$$$$$\    $$ |   \$$$$$$  |\$$$$$$  |  ||
||  \_______/ \________|   \__|    \______/  \______/   ||
||                                                      ||
>>======================================================<<
```

Projeto desenvolvido em Python para auxiliar na administração e organização do **RPG Betsu**, automatizando diversas mecânicas importantes da mesa, como cálculos de atributos, progressão de status, gerenciamento de recursos e geração procedural de criaturas, etc.

O projeto foi estruturado para tornar as sessões mais rápidas e imersivas, reduzindo a necessidade de cálculos manuais durante o jogo, decisão de spawn de monstros, etc.

**A estrutura do README.md**:

- [Estrutura do projeto](#estrutura-do-projeto);
- [Sistemas](#sistemas).

## Estrutura do projeto
O arquivo [main.py](main.py) é o menu que acessa os outros sistemas de automações desenvolvidos. Você seleciona se é um jogador ou o mestre da mesa e, a partir daí, são mostrados sistemas diferentes que facilitam a vida dos participantes.

Os dados ficam dentro da pasta [dados](dados/), tais como os arquivos .json.
Os sistemas ficam dentro da pasta [sistemas](sistemas/), nessa pasta fica armazenada os sistemas para que o arquivo [main.py](main.py) acesse e execute o devido sistema que o usuário queira.

Essa separação de banco de dados e sistemas permite uma melhor organização, edição de dados, e gerenciamento do projeto.

## Sistemas
Dentre as automatizações estão:

- [Sistema de Spawn](#sistema-de-spawn-spawnpy);
- [Sistema de Status](#sistema-de-atributos-statuspy);
- [Sistema de Bestiário](#sistema-de-bestiário-betsuariopy);
- [Sistema de Lojas](#sistema-de-lojas-lojapy).

### Sistema de Spawn (**spawn.py**)
Baseados em **probabilidade**, **raridade**, **região** e **horário**, permitindo que diferentes criaturas apareçam de forma dinâmica e contextual dentro do universo do RPG.
Toda a lógica foi organizada de forma escalável, facilitando a expansão futura do sistema com novos monstros e dados.

Há a chance de 80% de apaprecer um monstro, e 20% de não aparecer. Se aparacer um monstro, o usuário escolhe o **reino**, a **região** e o **horário**, ao final é dito qual monstro apareceu baseado nos dados fornecidos.

O arquivo [spawn.json](dados/spawn.json) (situado na pasta "*dados*") é onde  fica os dados dos **reinos**, **regiões** e os **monstros** sendo que cada um tem sua váriavel para aparecer dependendo do **horário** e **raridade**. O arquivo [spawn.py](sistemas/spawn.py) roda esses dados e entregua ao usuário.

As modificações para **inclusão**/**retirada**/**edição** de dados são feitos exclusivamente no arquio [spawn.json](dados/spawn.json). Mas se for necessário, é preciso fazer as devidas adaptações no [spawn.py](sistemas/spawn.py).

### Sistema de Atributos (**status.py**)
Cálculos automáticos para atributos dos personagens, incluindo **vida**, **mana**, **stamina**, **resistências físicas** e **mágicas**, **movimentação**, **alcance** e progressão por **nível**.

São cálculos básicos e simples, mas o código agiliza o processo de fazer a contas e evita erros de cálculos e informações.

### Sistema de Bestiário (**betsuario.py**)
Esse sistema é um bestiário do mundo Betsu, ou **betsuario**. Esse sistema mostra as informações dos monstros que aparecem, incluíndo **características**, **localidade**, **raridade** e **drops**. **Dificuldade de pesca**, **uso na culinária** e **efeito** (se for um peixe para pescaria).

Esse sistema é semelhante ao [sistema de spawn](sistemas/spawn.py), ambos usam um banco de dados em .json. Agilizando o processo de busca por informações, o usuário digita o **reino**, a **região** e o **mob** que queira saber mais e assim é mostrado.

As modificações para **inclusão**/**retirada**/**edição** de dados são feitos exclusivamente no arquio [betsuario.json](dados/betsuario.json). Mas se for necessário, é preciso fazer as devidas adaptações no [betsuario.py](sistemas/betsuario.py).

### Sistema de Lojas (**loja.py**)
O sistema de Lojas tem a mesma estrutura e finalidade do [sistema betsuario](#sistema-de-bestiário-betsuariopy). Dentro do sistema, é possível ver os produtos vendidos de cada loja, o que pode vender ou comprar (dependendo da loja), em cada Reino.

As modificações para **inclusão**/**retirada**/**edição** de dados são feitos exclusivamente no arquio [lojas.json](dados/lojas.json). Mas se for necessário, é preciso fazer as devidas adaptações no [lojas.py](sistemas/lojas.py).