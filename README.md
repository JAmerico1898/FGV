# 📊 Mini-Case: Executivo S.A.
## Construção Sintética de BP, DRE e DFC

Sistema interativo desenvolvido em Streamlit para o **Mini-Case Executivo S.A.**, permitindo realizar as 8 transações do caso e visualizar automaticamente as demonstrações financeiras.

---

## 🎯 Sobre o Mini-Case

Este mini-case apresenta um conjunto específico de **8 transações** da empresa **Executivo S.A.** para construção prática das três principais demonstrações financeiras:

- 📋 **Balanço Patrimonial (BP)**
- 📊 **Demonstração do Resultado do Exercício (DRE)**
- 💰 **Demonstração dos Fluxos de Caixa (DFC)**

---

## 📝 As 8 Transações do Case

### Transações 1-4 (Constituição e Investimentos):

1. **Abertura**: Sócios investem **R$ 100.000** no caixa
2. **Empréstimo**: Empresa pega **R$ 50.000** no banco
3. **Compra de Estoque**: **R$ 30.000** pagos à vista
4. **Compra de Máquina**: **R$ 20.000** (R$ 5.000 à vista e R$ 15.000 a prazo)

### Transações 5-8 (Operações e Despesas):

5. **Venda**: Vende 80% do estoque por **R$ 60.000** (metade à vista, metade a prazo)
6. **Custo**: CMV = **R$ 24.000** (80% de R$ 30.000)
7. **Salários**: Paga **R$ 10.000** de salários
8. **Depreciação**: **R$ 2.000** de depreciação da máquina no período

---

## 🚀 Como Usar

### Instalação

1. **Instale as dependências:**
```bash
pip install streamlit pandas
```

2. **Execute o aplicativo:**
```bash
streamlit run mini_case_executivo_sa.py
```

3. **Acesse no navegador:**
```
http://localhost:8501
```

---

## 📖 Navegação pelo Sistema

### 🏠 Início
- Dashboard com métricas principais
- Progresso das transações (0/8 a 8/8)
- Visão geral do mini-case

### 📝 Transações do Case
- **Aba "Realizar Transações"**: Execute as 8 transações na ordem
- **Aba "Histórico"**: Visualize todas as transações realizadas
- Cada transação mostra:
  - Descrição completa
  - Valor envolvido
  - Lançamentos contábeis (Débito e Crédito)
  - Botão para registrar

### 📋 Balanço Patrimonial
- **Ativo Circulante**: Caixa, Contas a Receber, Estoque
- **Ativo Não Circulante**: Máquinas, (-) Depreciação Acumulada
- **Passivo**: Fornecedores, Empréstimos
- **Patrimônio Líquido**: Capital Social, Lucros Acumulados
- **Verificação automática**: Ativo = Passivo + PL

### 📊 DRE (Demonstração do Resultado)
- Receita de Vendas: R$ 60.000
- (-) CMV: R$ 24.000
- = Lucro Bruto: R$ 36.000
- (-) Despesas com Salários: R$ 10.000
- (-) Despesas com Depreciação: R$ 2.000
- = **Lucro Líquido: R$ 24.000**
- **Indicadores**: Margem Bruta, Operacional e Líquida

### 💰 DFC (Fluxo de Caixa)
- **Método Indireto**
- **Fluxo Operacional (FCO)**: + R$ 5.000
- **Fluxo de Investimento (FCI)**: - R$ 20.000
- **Fluxo de Financiamento (FCF)**: + R$ 150.000
- **Variação Total do Caixa**: + R$ 135.000

### 📈 Resumo Completo
- Comparação: Valores Esperados vs Realizados
- Métricas principais em destaque
- **Conclusão Econômica**: Análise crítica do case
- Conclusões e aprendizados do case

---

## 📊 Resultados Esperados

Ao completar todas as 8 transações, o sistema deve apresentar:

### Conclusão Econômica do Case

> 💡 **Insight Importante:**
> 
> A empresa gerou **R$ 24k de lucro** (competência), mas apenas **R$ 5k de caixa operacional**. 
> Ela **'queimou' R$ 20k em investimentos** e se financiou com **R$ 150k de sócios e bancos**. 
> O caixa subiu, mas **a operação ainda não se paga**.
> 
> **Ou seja:** O lucro contábil existe, mas o negócio ainda depende de capital externo para funcionar. 
> A geração de caixa operacional é insuficiente para cobrir os investimentos realizados.

### Balanço Patrimonial

| Item | Valor (R$) |
|------|------------|
| **ATIVO** | |
| Caixa | 135.000 |
| Contas a Receber | 30.000 |
| Estoque | 6.000 |
| Máquinas | 20.000 |
| (-) Depreciação Acum. | (2.000) |
| **TOTAL ATIVO** | **189.000** |
| | |
| **PASSIVO** | |
| Fornecedores | 15.000 |
| Empréstimos | 50.000 |
| **Total Passivo** | **65.000** |
| | |
| **PATRIMÔNIO LÍQUIDO** | |
| Capital Social | 100.000 |
| Lucros Acumulados | 24.000 |
| **Total PL** | **124.000** |
| | |
| **TOTAL PASSIVO + PL** | **189.000** |

### DRE

| Item | Valor (R$) |
|------|------------|
| Receita de Vendas | 60.000 |
| (-) CMV | (24.000) |
| **= Lucro Bruto** | **36.000** |
| (-) Despesas com Salários | (10.000) |
| (-) Despesas com Depreciação | (2.000) |
| **= Lucro Operacional (EBIT)** | **24.000** |
| **= Lucro Líquido** | **24.000** |

### DFC

| Item | Valor (R$) |
|------|------------|
| Lucro Líquido | 24.000 |
| (+) Depreciação | 2.000 |
| (-) Aumento Contas a Receber | (30.000) |
| (-) Aumento Estoque | (6.000) |
| (+) Aumento Fornecedores | 15.000 |
| **= FCO** | **5.000** |
| (-) Compra de Máquina | (20.000) |
| **= FCI** | **(20.000)** |
| (+) Capital Social | 100.000 |
| (+) Empréstimo | 50.000 |
| **= FCF** | **150.000** |
| | |
| **Variação Total do Caixa** | **135.000** |

---

## 🎓 Conceitos Abordados

### 1. Método das Partidas Dobradas
Cada transação gera lançamentos de débito e crédito de mesmo valor.

**Exemplo (Transação 1):**
- **Débito**: Caixa + R$ 100.000
- **Crédito**: Capital Social + R$ 100.000

### 2. Regime de Competência
A venda é reconhecida quando ocorre, mesmo que parte seja a prazo (Transação 5).

### 3. CMV (Custo da Mercadoria Vendida)
O custo do estoque vendido reduz o lucro (Transação 6).

### 4. Depreciação
Despesa que reduz o lucro mas não afeta o caixa (Transação 8).

### 5. Fluxo de Caixa vs Lucro
O lucro líquido é R$ 24.000, mas o caixa operacional gerado é apenas R$ 5.000.

### 6. Interligação das Demonstrações
- O Lucro Líquido da DRE vai para o PL no BP
- A variação do caixa na DFC bate com o saldo no BP

---

## 💡 Funcionalidades do Sistema

### ✅ O que o sistema faz:

1. **Guia passo a passo**: Execute as transações na ordem correta
2. **Validação de sequência**: Só permite transações após as anteriores
3. **Cálculos automáticos**: Todas as demonstrações são atualizadas em tempo real
4. **Lançamentos contábeis**: Mostra débito e crédito de cada operação
5. **Verificação de equilíbrio**: Confirma que Ativo = Passivo + PL
6. **Indicadores**: Calcula margens de rentabilidade automaticamente
7. **Progresso visual**: Acompanhe quantas transações foram realizadas
8. **Histórico completo**: Veja todas as operações registradas

### 🎯 Diferenciais:

- Interface intuitiva e profissional
- Cores e design inspirados no material original
- Explicações em cada etapa
- Comparação com valores esperados
- Sistema de navegação por abas
- Possibilidade de limpar e recomeçar

---

## 🔧 Requisitos Técnicos

### Mínimo
- Python 3.8+
- 50 MB de espaço em disco
- Navegador web moderno

### Dependências
```
streamlit==1.28.0
pandas==2.1.0
```

---

## 📚 Como Usar para Estudo

### Para Estudantes:

1. **Primeira vez**: Leia todas as transações antes de começar
2. **Execute em ordem**: Siga as transações de 1 a 8
3. **Observe os efeitos**: Veja como cada transação afeta as contas
4. **Confira os resultados**: Compare com os valores esperados
5. **Refaça o exercício**: Limpe tudo e pratique novamente

### Para Professores:

1. **Demonstração em sala**: Projete o sistema e execute as transações
2. **Discussão em grupo**: Pare após cada transação para discutir
3. **Exercício prático**: Peça aos alunos para executarem sozinhos
4. **Variações**: Modifique os valores e discuta os efeitos
5. **Avaliação**: Use para verificar compreensão dos conceitos

---

## 🎯 Objetivos de Aprendizagem

Ao completar este mini-case, você será capaz de:

- ✅ Registrar lançamentos contábeis usando débito e crédito
- ✅ Entender a diferença entre lucro e caixa
- ✅ Construir um Balanço Patrimonial
- ✅ Elaborar uma DRE
- ✅ Preparar uma DFC pelo método indireto
- ✅ Compreender como as demonstrações se conectam
- ✅ Calcular e interpretar indicadores de rentabilidade
- ✅ Aplicar o regime de competência

---

## 🔄 Fluxo de Uso Recomendado

```
1. INÍCIO
   ↓
2. Leia as 8 transações
   ↓
3. Execute Transação 1
   ↓
4. Veja o efeito no BP
   ↓
5. Execute Transação 2
   ↓
6. Continue até Transação 8
   ↓
7. Confira a DRE completa
   ↓
8. Analise a DFC
   ↓
9. Veja o Resumo Completo
   ↓
10. Compare com valores esperados
```

---

## 🎨 Capturas de Tela

### Tela Inicial
- Dashboard com progresso
- Métricas principais
- Descrição das transações

### Realizando Transações
- Transações expandíveis
- Lançamentos contábeis visíveis
- Validação de sequência
- Feedback visual

### Demonstrações Financeiras
- Tabelas profissionais
- Cálculos destacados
- Verificações automáticas
- Indicadores em tempo real

---

## ⚠️ Observações Importantes

1. **Ordem das transações**: Execute na sequência (1 a 8)
2. **Dados temporários**: Os dados são mantidos apenas durante a sessão
3. **Sem edição**: Não é possível editar transações, apenas limpar tudo
4. **Valores fixos**: Este é um caso específico, os valores não podem ser alterados
5. **Educacional**: Desenvolvido exclusivamente para fins didáticos

---

## 🆘 Resolução de Problemas

### "Não consigo executar uma transação"
**Solução**: Execute as transações anteriores primeiro. O sistema bloqueia transações fora de ordem.

### "Os valores não batem com o esperado"
**Solução**: Limpe todas as transações e comece novamente. Certifique-se de executar todas as 8 transações.

### "O balanço não está equilibrado"
**Solução**: Verifique se todas as 8 transações foram executadas corretamente.

---

## 📝 Licença

Este projeto é de uso livre para fins educacionais.

---

## 👨‍🏫 Autor

Desenvolvido como material didático para a disciplina de **Análise de Demonstrações Financeiras**.

Baseado no Mini-Case "Executivo S.A." - Construção Sintética de BP, DRE e DFC.

---

## 🎓 Para Saber Mais

### Conceitos Relacionados:
- Contabilidade Básica
- Análise de Balanços
- Gestão Financeira
- Controladoria

### Próximos Passos:
- Análise Vertical e Horizontal
- Índices de Liquidez
- Índices de Endividamento
- Análise DuPont

---

**Mini-Case: Executivo S.A.**

_Construção Sintética de BP, DRE e DFC_

_Versão 1.0 - Novembro 2025_

📚 Bons estudos! 🎓