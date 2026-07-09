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
- [Tecnologias utilizadas](#tecnologias-utilizadas);
- [Instalação](#instalação);
- [Sistemas](#sistemas);
    - [Sistema de betsuario](#sistema-de-bestiário-betsuariopy);
    - [Sistema de dado](#sistema-de-dado-dadopy);
    - [Sistema de lojas](#sistema-de-lojas-lojapy);
    - [Sistema de spawn](#sistema-de-spawn-spawnpy);
    - [Sistema de status](#sistema-de-atributos-statuspy).
- [Autores](#autores);
- [Como contribuir?](#como-contribuir).

---

# Estrutura do projeto
```
├── Betsu-RPG
│   ├── dados                 # Dados de Betsu
│   │   ├── betsuario.json
│   │   ├── lojas.json
│   │   └── spawn.json
│   ├── sistemas              # Sistemas usados
│   │   ├── betsuario.py
│   │   ├── dado.py
│   │   ├── __init__.py
│   │   ├── lojas.py
│   │   ├── spawn.py
│   │   ├── status.py
│   │   └── utils.py          # Central de funções
|   ├── main.py
│   ├── README.md
```

---

# Tecnologias utilizadas
- Linguagens:
    - Python 3
- Bibliotecas:
    - OS;
    - Time;
    - Random;
    - JSON;
    - RE.
- Empacotamento: **PyInstaller**

---

# Instalação
Clone o repositório:

```bash
git clone https://github.com/pedroh288/Betsu-RPG.git
cd Betsu-RPG
```
Instale as depedências:
```bash
pip install -r requirements.txt
```
Execute o programa:
```bash
python main.py
```

---

# Funcionamento
O arquivo [main.py](main.py) é o menu que acessa os outros sistemas de automações desenvolvidos. Você seleciona se é um jogador ou o mestre da mesa e, a partir daí, são mostrados sistemas diferentes que facilitam a vida dos participantes. A cada seleção é um módulo python diferente. 

O arquivo [utils.py](sistemas/utils.py) é a central das funções. É onde fica as funções que se repetem, ou que são colocadas nesse módulo para trazer mais clareza ao código.

---

# Sistemas
Dentre as automatizações estão:

- [Sistema de Bestiário](#sistema-de-bestiário-betsuariopy);
- [Sistema de Dados](#sistema-de-dado-dadopy);
- [Sistema de Lojas](#sistema-de-lojas-lojapy);
- [Sistema de Spawn](#sistema-de-spawn-spawnpy);
- [Sistema de Status](#sistema-de-atributos-statuspy).

## Sistema de Bestiário (**betsuario.py**)
Esse sistema é um bestiário do mundo Betsu, ou **betsuario**. Esse sistema mostra as informações dos monstros que aparecem, incluíndo **características**, **localidade**, **raridade** e **drops**. **Dificuldade de pesca**, **uso na culinária** e **efeito** (se for um peixe para pescaria).

Agilizando o processo de busca por informações, o usuário digita o **reino**, a **região** e o **mob** que queira saber mais e assim é mostrado.

O arquivo [betsuario.json](dados/betsuario.json) (situado na pasta "*dados*") é onde  fica os dados dos **reinos**, **regiões** e os **monstros**. O arquivo [betsuario.py](sistemas/betsuario.py) roda esses dados e entregua ao usuário.

As modificações para **inclusão**/**retirada**/**edição** de dados são feitos exclusivamente no arquio [betsuario.json](dados/betsuario.json). Mas se for necessário, é preciso fazer as devidas adaptações no [betsuario.py](sistemas/betsuario.py).

## Sistema de Dado (**dado.py**)
O sistema de Dado foi feito para poder simular a **rolagem de dados** de RPG.

O programa pede **quantidade de dados**, **lados do dado e o bônus** (se tiver) e usa a **biblioteca random** para gerar o resultado. E usando a biblioteca RE, ele mantém o padrão de input.

## Sistema de Lojas (**loja.py**)
O sistema de Lojas tem a mesma estrutura e finalidade do [sistema betsuario](#sistema-de-bestiário-betsuariopy). Dentro do sistema, é possível ver os produtos vendidos de cada loja, o que pode vender ou comprar (dependendo da loja), em cada Reino.

As modificações para **inclusão**/**retirada**/**edição** de dados são feitos exclusivamente no arquio [lojas.json](dados/lojas.json). Mas se for necessário, é preciso fazer as devidas adaptações no [lojas.py](sistemas/lojas.py).

## Sistema de Spawn (**spawn.py**)
Baseados em **probabilidade**, **raridade**, **região** e **horário**, permitindo que diferentes criaturas apareçam de forma dinâmica e contextual dentro do universo do RPG.
Toda a lógica foi organizada de forma escalável, facilitando a expansão futura do sistema com novos monstros e dados.

Há a chance de 80% de apaprecer um monstro, e 20% de não aparecer. Se aparacer um monstro, o usuário escolhe o **reino**, a **região** e o **horário**, ao final é dito qual monstro apareceu baseado nos dados fornecidos.

O arquivo [spawn.json](dados/spawn.json) (situado na pasta "*dados*") é onde  fica os dados dos **reinos**, **regiões** e os **monstros** sendo que cada um tem sua váriavel para aparecer dependendo do **horário** e **raridade**. O arquivo [spawn.py](sistemas/spawn.py) roda esses dados e entregua ao usuário.

As modificações para **inclusão**/**retirada**/**edição** de dados são feitos exclusivamente no arquio [spawn.json](dados/spawn.json). Mas se for necessário, é preciso fazer as devidas adaptações no [spawn.py](sistemas/spawn.py).

## Sistema de Atributos (**status.py**)
Cálculos automáticos para atributos dos personagens, incluindo **vida**, **mana**, **stamina**, **resistências físicas** e **mágicas**, **movimentação**, **alcance** e progressão por **nível**.

São cálculos básicos e simples, mas o código agiliza o processo de fazer a contas e evita erros de cálculos e informações.

---

# Autores
- [@pedroh288](https://www.github.com/pedroh288).

---

# Como contribuir?
1. Faça fork do repositório;
2. Crie uma branch da feature (`git checkou -b ...`);
3. Faça commit das suas mudanças (`git commit -m "..."`);
4. Faça push para a branch criada (`git push origin ...`);
5. Abra um Pull Request.