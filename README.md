# Teste Técnico – Desenvolvedor de Sistemas Júnior

Este repositório contém três programas desenvolvidos como parte de um desafio técnico solicitado pela empresa.
Cada programa utiliza entrada do usuário ou arquivos JSON e apresenta saídas claras e objetivas.

---

## Programas incluídos

### 1 Cálculo de Comissão (`comissao.py`)
Este programa:
- Lê os dados de vendas a partir de um arquivo JSON.
- Aplica as regras de comissão:
  - Vendas abaixo de R$ 100 → 0%
  - Vendas entre R$ 100 e R$ 500 → 1%
  - Vendas acima de R$ 500 → 5%
- Gera o total de comissão por vendedor.
- Exibe um relatório no terminal.

Objetivo: processar grandes listas de vendas e calcular comissões automaticamente.

---

### 2 Movimentação de Estoque (`estoque.py`)
Este programa permite:
- Buscar um produto pelo código ou nome.
- Escolher entre:
  - Adicionar ao estoque  
  - Remover do estoque  
- Atualizar a quantidade final.
- Descrever a movimentação realizada (ex.: “Foram removidas 15 unidades”).
- Funcionar em loop, permitindo várias operações até o usuário decidir sair.

Objetivo: simular um sistema de estoque básico, com entradas e saídas de produtos.

---

### 3 Cálculo de Juros por Atraso (`juros.py`)
Este programa:
- Solicita o valor original da dívida (aqui deve-se 
  utilizar pontos [.] e não vírgulas [,]).
- Lê a data de vencimento informada pelo usuário.
- Compara com a data atual automaticamente.
- Calcula juros de 2.5% ao dia em caso de atraso.
- Funciona em loop, permitindo vários cálculos.

**Objetivo:** calcular juros simples com base em atraso de pagamento.

---

OBS.: Certifique-se de ter Python 3.9+ instalado.

