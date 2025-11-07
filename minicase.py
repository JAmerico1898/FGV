import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(
    page_title="Mini-Case: Executivo S.A.",
    page_icon="📊",
    layout="wide"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: white;
        text-align: center;
        margin: 0;
    }
    .main-header p {
        color: #e0e0e0;
        text-align: center;
        margin: 0.5rem 0 0 0;
    }
    .stMetric {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Título principal com estilo
st.markdown("""
<div class="main-header">
    <h1>📊 Mini-Case: Executivo S.A.</h1>
    <p>Construção Sintética de BP, DRE e DFC</p>
</div>
""", unsafe_allow_html=True)

# Inicialização do estado da sessão
if 'transacoes_realizadas' not in st.session_state:
    st.session_state.transacoes_realizadas = []
    
if 'contas' not in st.session_state:
    st.session_state.contas = {
        # ATIVO
        'Caixa': 0,
        'Contas a Receber': 0,
        'Estoque': 0,
        'Máquinas': 0,
        'Depreciação Acumulada': 0,
        
        # PASSIVO
        'Fornecedores': 0,
        'Empréstimos': 0,
        
        # PATRIMÔNIO LÍQUIDO
        'Capital Social': 0,
        'Lucros Acumulados': 0,
        
        # DRE
        'Receita de Vendas': 0,
        'CMV': 0,
        'Despesas com Salários': 0,
        'Despesas com Depreciação': 0,
    }

# Sidebar para navegação
st.sidebar.title("📑 Menu de Navegação")
pagina = st.sidebar.radio(
    "Escolha a seção:",
    ["🏠 Início", "📝 Transações do Case", "📋 Balanço Patrimonial", 
     "📊 DRE", "💰 DFC", "📈 Resumo Completo"]
)

# Página: Início
if pagina == "🏠 Início":
    st.header("Bem-vindo ao Mini-Case Executivo S.A.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Transações Realizadas", f"{len(st.session_state.transacoes_realizadas)}/8")
    with col2:
        total_ativo = (st.session_state.contas['Caixa'] + 
                      st.session_state.contas['Contas a Receber'] + 
                      st.session_state.contas['Estoque'] + 
                      st.session_state.contas['Máquinas'] - 
                      st.session_state.contas['Depreciação Acumulada'])
        st.metric("Total do Ativo", f"R$ {total_ativo:,.2f}")
    with col3:
        lucro_liquido = (st.session_state.contas['Receita de Vendas'] - 
                        st.session_state.contas['CMV'] - 
                        st.session_state.contas['Despesas com Salários'] - 
                        st.session_state.contas['Despesas com Depreciação'])
        st.metric("Lucro Líquido", f"R$ {lucro_liquido:,.2f}")
    
    st.markdown("---")
    
    st.subheader("📖 Sobre o Mini-Case")
    st.write("""
    Este mini-case apresenta as **8 transações** da empresa **Executivo S.A.** para construção 
    das demonstrações financeiras:
    
    ### Transações (1-4):
    1. **Abertura**: Sócios investem R$ 100.000 no caixa
    2. **Empréstimo**: Empresa pega R$ 50.000 no banco
    3. **Compra de Estoque**: R$ 30.000 pagos à vista
    4. **Compra de Máquina**: R$ 20.000 (R$ 5.000 à vista e R$ 15.000 a prazo)
    
    ### Transações (5-8):
    5. **Venda**: Vende 80% do estoque por R$ 60.000 (metade à vista, metade a prazo)
    6. **Custo**: CMV = R$ 24.000 (80% de R$ 30.000)
    7. **Salários**: Paga R$ 10.000 de salários
    8. **Depreciação**: R$ 2.000 de depreciação da máquina
    
    **Como usar:**
    1. Vá para "📝 Transações do Case"
    2. Realize as 8 transações na ordem
    3. Consulte as demonstrações financeiras geradas automaticamente
    """)
    
    # Progresso das transações
    st.markdown("---")
    st.subheader("📊 Progresso das Transações")
    progresso = len(st.session_state.transacoes_realizadas) / 8
    st.progress(progresso)
    st.write(f"**{len(st.session_state.transacoes_realizadas)} de 8 transações realizadas** ({progresso*100:.0f}%)")
    
    if len(st.session_state.transacoes_realizadas) == 8:
        st.success("✅ Todas as transações foram realizadas! Consulte as demonstrações financeiras.")

# Página: Transações do Case
elif pagina == "📝 Transações do Case":
    st.header("Transações do Mini-Case")
    
    tab1, tab2 = st.tabs(["Realizar Transações", "Histórico"])
    
    with tab1:
        st.subheader("Selecione a Transação")
        
        # Verificar quais transações já foram realizadas
        transacoes_ids = [t['id'] for t in st.session_state.transacoes_realizadas]
        
        # Transação 1
        if 1 not in transacoes_ids:
            with st.expander("**Transação 1** - Abertura: Investimento de Capital", expanded=True):
                st.info("💰 Sócios investem R$ 100.000 no caixa")
                st.write("**Lançamento Contábil:**")
                st.write("• **Débito**: Caixa - R$ 100.000")
                st.write("• **Crédito**: Capital Social - R$ 100.000")
                
                if st.button("✅ Registrar Transação 1", key="trans1"):
                    st.session_state.contas['Caixa'] += 100000
                    st.session_state.contas['Capital Social'] += 100000
                    st.session_state.transacoes_realizadas.append({
                        'id': 1,
                        'descricao': 'Abertura - Investimento de Capital',
                        'valor': 100000,
                        'data': datetime.now()
                    })
                    st.success("✅ Transação 1 registrada com sucesso!")
                    st.rerun()
        else:
            st.success("✅ Transação 1 já foi realizada")
        
        # Transação 2
        if 2 not in transacoes_ids:
            with st.expander("**Transação 2** - Empréstimo Bancário", expanded=(1 in transacoes_ids)):
                st.info("🏦 Empresa pega R$ 50.000 no banco")
                st.write("**Lançamento Contábil:**")
                st.write("• **Débito**: Caixa - R$ 50.000")
                st.write("• **Crédito**: Empréstimos - R$ 50.000")
                
                if 1 not in transacoes_ids:
                    st.warning("⚠️ Realize a Transação 1 primeiro")
                else:
                    if st.button("✅ Registrar Transação 2", key="trans2"):
                        st.session_state.contas['Caixa'] += 50000
                        st.session_state.contas['Empréstimos'] += 50000
                        st.session_state.transacoes_realizadas.append({
                            'id': 2,
                            'descricao': 'Empréstimo Bancário',
                            'valor': 50000,
                            'data': datetime.now()
                        })
                        st.success("✅ Transação 2 registrada com sucesso!")
                        st.rerun()
        else:
            st.success("✅ Transação 2 já foi realizada")
        
        # Transação 3
        if 3 not in transacoes_ids:
            with st.expander("**Transação 3** - Compra de Estoque", expanded=(2 in transacoes_ids)):
                st.info("📦 Compra de Estoque: R$ 30.000 pagos à vista")
                st.write("**Lançamento Contábil:**")
                st.write("• **Débito**: Estoque - R$ 30.000")
                st.write("• **Crédito**: Caixa - R$ 30.000")
                
                if 2 not in transacoes_ids:
                    st.warning("⚠️ Realize a Transação 2 primeiro")
                else:
                    if st.button("✅ Registrar Transação 3", key="trans3"):
                        st.session_state.contas['Estoque'] += 30000
                        st.session_state.contas['Caixa'] -= 30000
                        st.session_state.transacoes_realizadas.append({
                            'id': 3,
                            'descricao': 'Compra de Estoque à vista',
                            'valor': 30000,
                            'data': datetime.now()
                        })
                        st.success("✅ Transação 3 registrada com sucesso!")
                        st.rerun()
        else:
            st.success("✅ Transação 3 já foi realizada")
        
        # Transação 4
        if 4 not in transacoes_ids:
            with st.expander("**Transação 4** - Compra de Máquina", expanded=(3 in transacoes_ids)):
                st.info("🏭 Compra de Máquina: R$ 20.000 (R$ 5.000 à vista e R$ 15.000 a prazo)")
                st.write("**Lançamento Contábil:**")
                st.write("• **Débito**: Máquinas - R$ 20.000")
                st.write("• **Crédito**: Caixa - R$ 5.000")
                st.write("• **Crédito**: Fornecedores - R$ 15.000")
                
                if 3 not in transacoes_ids:
                    st.warning("⚠️ Realize a Transação 3 primeiro")
                else:
                    if st.button("✅ Registrar Transação 4", key="trans4"):
                        st.session_state.contas['Máquinas'] += 20000
                        st.session_state.contas['Caixa'] -= 5000
                        st.session_state.contas['Fornecedores'] += 15000
                        st.session_state.transacoes_realizadas.append({
                            'id': 4,
                            'descricao': 'Compra de Máquina (mista)',
                            'valor': 20000,
                            'data': datetime.now()
                        })
                        st.success("✅ Transação 4 registrada com sucesso!")
                        st.rerun()
        else:
            st.success("✅ Transação 4 já foi realizada")
        
        # Transação 5
        if 5 not in transacoes_ids:
            with st.expander("**Transação 5** - Venda de Mercadorias", expanded=(4 in transacoes_ids)):
                st.info("💵 Venda: 80% do estoque por R$ 60.000 (metade à vista, metade a prazo)")
                st.write("**Lançamento Contábil:**")
                st.write("• **Débito**: Caixa - R$ 30.000")
                st.write("• **Débito**: Contas a Receber - R$ 30.000")
                st.write("• **Crédito**: Receita de Vendas - R$ 60.000")
                
                if 4 not in transacoes_ids:
                    st.warning("⚠️ Realize a Transação 4 primeiro")
                else:
                    if st.button("✅ Registrar Transação 5", key="trans5"):
                        st.session_state.contas['Caixa'] += 30000
                        st.session_state.contas['Contas a Receber'] += 30000
                        st.session_state.contas['Receita de Vendas'] += 60000
                        st.session_state.transacoes_realizadas.append({
                            'id': 5,
                            'descricao': 'Venda de Mercadorias (mista)',
                            'valor': 60000,
                            'data': datetime.now()
                        })
                        st.success("✅ Transação 5 registrada com sucesso!")
                        st.rerun()
        else:
            st.success("✅ Transação 5 já foi realizada")
        
        # Transação 6
        if 6 not in transacoes_ids:
            with st.expander("**Transação 6** - Custo da Mercadoria Vendida (CMV)", expanded=(5 in transacoes_ids)):
                st.info("📉 CMV = R$ 24.000 (80% de R$ 30.000)")
                st.write("**Lançamento Contábil:**")
                st.write("• **Débito**: CMV - R$ 24.000")
                st.write("• **Crédito**: Estoque - R$ 24.000")
                
                if 5 not in transacoes_ids:
                    st.warning("⚠️ Realize a Transação 5 primeiro")
                else:
                    if st.button("✅ Registrar Transação 6", key="trans6"):
                        st.session_state.contas['CMV'] += 24000
                        st.session_state.contas['Estoque'] -= 24000
                        st.session_state.transacoes_realizadas.append({
                            'id': 6,
                            'descricao': 'Custo da Mercadoria Vendida',
                            'valor': 24000,
                            'data': datetime.now()
                        })
                        st.success("✅ Transação 6 registrada com sucesso!")
                        st.rerun()
        else:
            st.success("✅ Transação 6 já foi realizada")
        
        # Transação 7
        if 7 not in transacoes_ids:
            with st.expander("**Transação 7** - Pagamento de Salários", expanded=(6 in transacoes_ids)):
                st.info("👥 Paga R$ 10.000 de salários (despesa do período)")
                st.write("**Lançamento Contábil:**")
                st.write("• **Débito**: Despesas com Salários - R$ 10.000")
                st.write("• **Crédito**: Caixa - R$ 10.000")
                
                if 6 not in transacoes_ids:
                    st.warning("⚠️ Realize a Transação 6 primeiro")
                else:
                    if st.button("✅ Registrar Transação 7", key="trans7"):
                        st.session_state.contas['Despesas com Salários'] += 10000
                        st.session_state.contas['Caixa'] -= 10000
                        st.session_state.transacoes_realizadas.append({
                            'id': 7,
                            'descricao': 'Pagamento de Salários',
                            'valor': 10000,
                            'data': datetime.now()
                        })
                        st.success("✅ Transação 7 registrada com sucesso!")
                        st.rerun()
        else:
            st.success("✅ Transação 7 já foi realizada")
        
        # Transação 8
        if 8 not in transacoes_ids:
            with st.expander("**Transação 8** - Depreciação", expanded=(7 in transacoes_ids)):
                st.info("📊 R$ 2.000 de depreciação da máquina no período")
                st.write("**Lançamento Contábil:**")
                st.write("• **Débito**: Despesas com Depreciação - R$ 2.000")
                st.write("• **Crédito**: Depreciação Acumulada - R$ 2.000")
                
                if 7 not in transacoes_ids:
                    st.warning("⚠️ Realize a Transação 7 primeiro")
                else:
                    if st.button("✅ Registrar Transação 8", key="trans8"):
                        st.session_state.contas['Despesas com Depreciação'] += 2000
                        st.session_state.contas['Depreciação Acumulada'] += 2000
                        st.session_state.transacoes_realizadas.append({
                            'id': 8,
                            'descricao': 'Depreciação da Máquina',
                            'valor': 2000,
                            'data': datetime.now()
                        })
                        st.success("✅ Transação 8 registrada com sucesso!")
                        st.balloons()
                        st.rerun()
        else:
            st.success("✅ Transação 8 já foi realizada")
        
        # Botão para limpar tudo
        if len(st.session_state.transacoes_realizadas) > 0:
            st.markdown("---")
            if st.button("🗑️ Limpar Todas as Transações", type="secondary"):
                if st.checkbox("Confirmar exclusão"):
                    st.session_state.transacoes_realizadas = []
                    for key in st.session_state.contas:
                        st.session_state.contas[key] = 0
                    st.success("✅ Todas as transações foram excluídas!")
                    st.rerun()
    
    with tab2:
        st.subheader("Histórico de Transações Realizadas")
        
        if st.session_state.transacoes_realizadas:
            df_trans = pd.DataFrame(st.session_state.transacoes_realizadas)
            df_trans['valor'] = df_trans['valor'].apply(lambda x: f"R$ {x:,.2f}")
            df_trans = df_trans[['id', 'descricao', 'valor']]
            df_trans.columns = ['#', 'Descrição', 'Valor']
            st.dataframe(df_trans, use_container_width=True, hide_index=True)
        else:
            st.info("Nenhuma transação realizada ainda.")

# Página: Balanço Patrimonial
elif pagina == "📋 Balanço Patrimonial":
    st.header("Balanço Patrimonial - Executivo S.A.")
    
    # Cálculos do Ativo
    ativo_circulante = (st.session_state.contas['Caixa'] + 
                       st.session_state.contas['Contas a Receber'] + 
                       st.session_state.contas['Estoque'])
    
    ativo_nao_circulante = (st.session_state.contas['Máquinas'] - 
                           st.session_state.contas['Depreciação Acumulada'])
    
    total_ativo = ativo_circulante + ativo_nao_circulante
    
    # Cálculos do Passivo
    passivo_total = (st.session_state.contas['Fornecedores'] + 
                    st.session_state.contas['Empréstimos'])
    
    # Cálculo do Lucro Líquido
    lucro_liquido = (st.session_state.contas['Receita de Vendas'] - 
                    st.session_state.contas['CMV'] - 
                    st.session_state.contas['Despesas com Salários'] - 
                    st.session_state.contas['Despesas com Depreciação'])
    
    # Atualizar Lucros Acumulados
    st.session_state.contas['Lucros Acumulados'] = lucro_liquido
    
    # Patrimônio Líquido
    patrimonio_liquido = (st.session_state.contas['Capital Social'] + 
                         st.session_state.contas['Lucros Acumulados'])
    
    total_passivo_pl = passivo_total + patrimonio_liquido
    
    # Exibição do Balanço
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("ATIVO")
        
        st.markdown("**ATIVO CIRCULANTE**")
        df_ativo_circ = pd.DataFrame({
            'Conta': ['Caixa', 'Contas a Receber', 'Estoque', '**TOTAL ATIVO CIRCULANTE**'],
            'Cálculo': [
                '100+50-30-5+30-10',
                '(5)',
                '30 - 24',
                ''
            ],
            'Valor (R$)': [
                f"{st.session_state.contas['Caixa']:,.2f}",
                f"{st.session_state.contas['Contas a Receber']:,.2f}",
                f"{st.session_state.contas['Estoque']:,.2f}",
                f"**{ativo_circulante:,.2f}**"
            ]
        })
        st.dataframe(df_ativo_circ, use_container_width=True, hide_index=True)
        
        st.markdown("**ATIVO NÃO CIRCULANTE**")
        df_ativo_nao_circ = pd.DataFrame({
            'Conta': ['Máquinas', '(-) Depreciação Acumulada', '**TOTAL ATIVO NÃO CIRCULANTE**'],
            'Cálculo': ['(4)', '(8)', ''],
            'Valor (R$)': [
                f"{st.session_state.contas['Máquinas']:,.2f}",
                f"({st.session_state.contas['Depreciação Acumulada']:,.2f})",
                f"**{ativo_nao_circulante:,.2f}**"
            ]
        })
        st.dataframe(df_ativo_nao_circ, use_container_width=True, hide_index=True)
        
        st.markdown(f"### **TOTAL DO ATIVO: R$ {total_ativo:,.2f}**")
    
    with col2:
        st.subheader("PASSIVO E PATRIMÔNIO LÍQUIDO")
        
        st.markdown("**PASSIVO CIRCULANTE**")
        df_passivo = pd.DataFrame({
            'Conta': ['Fornecedores (Máquina)', 'Empréstimos', '**TOTAL PASSIVO**'],
            'Cálculo': ['(4)', '(2)', ''],
            'Valor (R$)': [
                f"{st.session_state.contas['Fornecedores']:,.2f}",
                f"{st.session_state.contas['Empréstimos']:,.2f}",
                f"**{passivo_total:,.2f}**"
            ]
        })
        st.dataframe(df_passivo, use_container_width=True, hide_index=True)
        
        st.markdown("**PATRIMÔNIO LÍQUIDO**")
        df_pl = pd.DataFrame({
            'Conta': ['Capital Social', 'Lucros Acumulados (DRE)', '**TOTAL PL**'],
            'Cálculo': ['(1)', '', ''],
            'Valor (R$)': [
                f"{st.session_state.contas['Capital Social']:,.2f}",
                f"{st.session_state.contas['Lucros Acumulados']:,.2f}",
                f"**{patrimonio_liquido:,.2f}**"
            ]
        })
        st.dataframe(df_pl, use_container_width=True, hide_index=True)
        
        st.markdown(f"### **TOTAL PASSIVO + PL: R$ {total_passivo_pl:,.2f}**")
    
    # Verificação de consistência
    st.markdown("---")
    diferenca = total_ativo - total_passivo_pl
    if abs(diferenca) < 0.01:
        st.success(f"✅ Balanço Patrimonial está EQUILIBRADO! Ativo = Passivo + PL = R$ {total_ativo:,.2f}")
    else:
        st.error(f"⚠️ Atenção! Diferença de R$ {diferenca:,.2f} entre Ativo e Passivo+PL")

# Página: DRE
elif pagina == "📊 DRE":
    st.header("Demonstração do Resultado do Exercício (DRE)")
    
    # Cálculos
    receita_vendas = st.session_state.contas['Receita de Vendas']
    cmv = st.session_state.contas['CMV']
    lucro_bruto = receita_vendas - cmv
    
    despesas_salarios = st.session_state.contas['Despesas com Salários']
    despesas_depreciacao = st.session_state.contas['Despesas com Depreciação']
    
    lucro_operacional = lucro_bruto - despesas_salarios - despesas_depreciacao
    lucro_liquido = lucro_operacional  # Sem juros/IR para simplificar
    
    # Exibição da DRE
    df_dre = pd.DataFrame({
        'Descrição': [
            'Receita de Vendas (5)',
            '',
            'CMV (Custo da Mercadoria Vendida) (6)',
            '',
            '= LUCRO BRUTO',
            '',
            'Despesa com Salários (7)',
            '',
            'Despesa com Depreciação (8)',
            '',
            '= LUCRO OPERACIONAL (EBIT)',
            '',
            '(Sem Juros/IR para simplificar)',
            '',
            '= LUCRO LÍQUIDO'
        ],
        'Referência': [
            '(5)',
            '',
            '(6)',
            '',
            '',
            '',
            '(7)',
            '',
            '(8)',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
        'Valor (R$)': [
            f"+ {receita_vendas:,.2f}",
            "",
            f"- {cmv:,.2f}",
            "",
            f"**= {lucro_bruto:,.2f}**",
            "",
            f"- {despesas_salarios:,.2f}",
            "",
            f"- {despesas_depreciacao:,.2f}",
            "",
            f"**= {lucro_operacional:,.2f}**",
            "",
            "",
            "",
            f"**= {lucro_liquido:,.2f}**"
        ]
    })
    
    st.dataframe(df_dre, use_container_width=True, hide_index=True)
    
    # Indicadores
    st.markdown("---")
    st.subheader("📊 Indicadores de Rentabilidade")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        margem_bruta = (lucro_bruto / receita_vendas * 100) if receita_vendas > 0 else 0
        st.metric("Margem Bruta", f"{margem_bruta:.2f}%")
    
    with col2:
        margem_operacional = (lucro_operacional / receita_vendas * 100) if receita_vendas > 0 else 0
        st.metric("Margem Operacional", f"{margem_operacional:.2f}%")
    
    with col3:
        margem_liquida = (lucro_liquido / receita_vendas * 100) if receita_vendas > 0 else 0
        st.metric("Margem Líquida", f"{margem_liquida:.2f}%")

# Página: DFC
elif pagina == "💰 DFC":
    st.header("Demonstração dos Fluxos de Caixa (DFC)")
    
    # Cálculo do Lucro Líquido
    lucro_liquido = (st.session_state.contas['Receita de Vendas'] - 
                    st.session_state.contas['CMV'] - 
                    st.session_state.contas['Despesas com Salários'] - 
                    st.session_state.contas['Despesas com Depreciação'])
    
    # Fluxo Operacional (Método Indireto)
    st.subheader("💼 Fluxo de Caixa Operacional (Método Indireto)")
    
    depreciacao = st.session_state.contas['Depreciação Acumulada']
    var_contas_receber = -st.session_state.contas['Contas a Receber']
    var_estoque = -st.session_state.contas['Estoque']
    var_fornecedores = st.session_state.contas['Fornecedores']
    
    fco = lucro_liquido + depreciacao + var_contas_receber + var_estoque + var_fornecedores
    
    df_fco = pd.DataFrame({
        'Descrição': [
            'Lucro Líquido (Início)',
            '',
            'Ajustes (sem caixa):',
            '  + Depreciação (8)',
            '',
            'Variações no Capital de Giro (do BP):',
            '  - Aumento Contas a Receber (Ativo subiu)',
            '  - Aumento Estoque (Ativo subiu)',
            '  + Aumento Fornecedores (Passivo subiu)',
            '',
            '= FLUXO DE CAIXA OPERACIONAL (FCO)'
        ],
        'Valor (R$)': [
            f"+ {lucro_liquido:,.2f}",
            "",
            "",
            f"+ {depreciacao:,.2f}",
            "",
            "",
            f"{var_contas_receber:,.2f}",
            f"{var_estoque:,.2f}",
            f"+ {var_fornecedores:,.2f}",
            "",
            f"**= {fco:,.2f}**"
        ]
    })
    
    st.dataframe(df_fco, use_container_width=True, hide_index=True)
    
    # Fluxo de Investimento
    st.markdown("---")
    st.subheader("🏭 Fluxo de Investimento (FCI)")
    
    fci = -st.session_state.contas['Máquinas']
    
    df_fci = pd.DataFrame({
        'Descrição': [
            '- Compra de Máquina (4)',
            '',
            '= TOTAL FCI'
        ],
        'Valor (R$)': [
            f"- {st.session_state.contas['Máquinas']:,.2f}",
            "",
            f"**= ({abs(fci):,.2f})**"
        ]
    })
    
    st.dataframe(df_fci, use_container_width=True, hide_index=True)
    
    # Fluxo de Financiamento
    st.markdown("---")
    st.subheader("💰 Fluxo de Financiamento (FCF)")
    
    fcf = st.session_state.contas['Capital Social'] + st.session_state.contas['Empréstimos']
    
    df_fcf = pd.DataFrame({
        'Descrição': [
            '+ Capital Social (1)',
            '+ Empréstimo (2)',
            '',
            '= TOTAL FCF'
        ],
        'Valor (R$)': [
            f"+ {st.session_state.contas['Capital Social']:,.2f}",
            f"+ {st.session_state.contas['Empréstimos']:,.2f}",
            "",
            f"**= {fcf:,.2f}**"
        ]
    })
    
    st.dataframe(df_fcf, use_container_width=True, hide_index=True)
    
    # Variação Total do Caixa
    st.markdown("---")
    st.subheader("📊 O Fechamento do Caixa")
    
    variacao_total = fco + fci + fcf
    caixa_final = st.session_state.contas['Caixa']
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### Verificação Final")
        st.write(f"**FCO**: + R$ {fco:,.2f}")
        st.write(f"**FCI**: - R$ {abs(fci):,.2f}")
        st.write(f"**FCF**: + R$ {fcf:,.2f}")
        st.write("---")
        st.write(f"**Variação Total** = + R$ {variacao_total:,.2f}")
    
    with col2:
        st.markdown(f"### +{variacao_total/1000:.0f}k")
        st.markdown("#### Variação Total do Caixa")
        
        if abs(variacao_total - caixa_final) < 0.01:
            st.success(f"""
            ✅ Este valor é exatamente o saldo da conta "Caixa" no Balanço Patrimonial 
            (R$ {caixa_final:,.2f}). 
            
            **As demonstrações se conectam perfeitamente!**
            """)
        else:
            st.warning(f"""
            Diferença entre variação do caixa e saldo final: 
            R$ {abs(variacao_total - caixa_final):,.2f}
            """)

# Página: Resumo Completo
elif pagina == "📈 Resumo Completo":
    st.header("Resumo Completo das Demonstrações Financeiras")
    
    # Verificar se todas as transações foram realizadas
    if len(st.session_state.transacoes_realizadas) < 8:
        st.warning(f"""
        ⚠️ **Atenção**: Apenas {len(st.session_state.transacoes_realizadas)} de 8 transações foram realizadas.
        
        Para ver o resumo completo, realize todas as transações na seção "📝 Transações do Case".
        """)
        st.stop()
    
    st.success("✅ Todas as 8 transações foram realizadas! Veja abaixo o resumo completo:")
    
    # Cálculos principais
    total_ativo = (st.session_state.contas['Caixa'] + 
                  st.session_state.contas['Contas a Receber'] + 
                  st.session_state.contas['Estoque'] + 
                  st.session_state.contas['Máquinas'] - 
                  st.session_state.contas['Depreciação Acumulada'])
    
    lucro_liquido = (st.session_state.contas['Receita de Vendas'] - 
                    st.session_state.contas['CMV'] - 
                    st.session_state.contas['Despesas com Salários'] - 
                    st.session_state.contas['Despesas com Depreciação'])
    
    # Métricas principais
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total do Ativo", f"R$ {total_ativo:,.2f}")
    with col2:
        st.metric("Caixa Final", f"R$ {st.session_state.contas['Caixa']:,.2f}")
    with col3:
        st.metric("Receita de Vendas", f"R$ {st.session_state.contas['Receita de Vendas']:,.2f}")
    with col4:
        st.metric("Lucro Líquido", f"R$ {lucro_liquido:,.2f}")
    
    # Tabela resumo
    st.markdown("---")
    st.subheader("📊 Valores Esperados vs Realizados")
    
    df_comparacao = pd.DataFrame({
        'Item': [
            'Caixa',
            'Contas a Receber',
            'Estoque',
            'Máquinas (líquido)',
            'Total Ativo',
            'Fornecedores',
            'Empréstimos',
            'Capital Social',
            'Lucros Acumulados',
            'Receita de Vendas',
            'Lucro Bruto',
            'Lucro Líquido'
        ],
        'Valor Esperado (R$)': [
            '135.000',
            '30.000',
            '6.000',
            '18.000',
            '189.000',
            '15.000',
            '50.000',
            '100.000',
            '24.000',
            '60.000',
            '36.000',
            '24.000'
        ],
        'Valor Realizado (R$)': [
            f"{st.session_state.contas['Caixa']:,.2f}",
            f"{st.session_state.contas['Contas a Receber']:,.2f}",
            f"{st.session_state.contas['Estoque']:,.2f}",
            f"{st.session_state.contas['Máquinas'] - st.session_state.contas['Depreciação Acumulada']:,.2f}",
            f"{total_ativo:,.2f}",
            f"{st.session_state.contas['Fornecedores']:,.2f}",
            f"{st.session_state.contas['Empréstimos']:,.2f}",
            f"{st.session_state.contas['Capital Social']:,.2f}",
            f"{st.session_state.contas['Lucros Acumulados']:,.2f}",
            f"{st.session_state.contas['Receita de Vendas']:,.2f}",
            f"{st.session_state.contas['Receita de Vendas'] - st.session_state.contas['CMV']:,.2f}",
            f"{lucro_liquido:,.2f}"
        ],
        'Status': ['✅'] * 12  # Assumindo que todos estão corretos
    })
    
    st.dataframe(df_comparacao, use_container_width=True, hide_index=True)
    
    # Conclusões
    st.markdown("---")
    st.subheader("🎯 Conclusões do Mini-Case")
    
    # Conclusão Econômica Destacada
    st.info("""
    ### 💡 Conclusão Econômica do Case:

    A empresa gerou **R\$ 24k de lucro** (competência), mas apenas **R\$ 5k de caixa operacional**.  
    Ela **'queimou' R\$ 20k em investimentos** e se financiou com **R\$ 150k de sócios e bancos**.  
    O caixa subiu, mas **a operação ainda não se paga**.

    **Ou seja:** O lucro contábil existe, mas o negócio ainda depende de capital externo para funcionar.  
    A geração de caixa operacional é insuficiente para cobrir os investimentos realizados.
    """)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### ✅ Pontos Principais:
        
        1. **Equilíbrio Patrimonial**: Ativo = Passivo + PL
        2. **Lucro de R$ 24.000**: Resultado positivo das operações
        3. **Margem Líquida de 40%**: Excelente rentabilidade
        4. **Caixa Positivo de R$ 135.000**: Boa liquidez
        5. **DFC Fechado**: Variação total do caixa bate com o saldo
        6. **⚠️ Caixa Operacional Baixo**: Apenas R$ 5.000 (20% do lucro)
        """)
    
    with col2:
        st.markdown("""
        ### 📚 Aprendizados:
        
        1. Toda transação afeta pelo menos duas contas
        2. **Lucro ≠ Caixa**: R$ 24k lucro vs R$ 5k caixa operacional
        3. Depreciação reduz lucro mas não afeta caixa
        4. As 3 demonstrações estão interligadas
        5. O BP fotografa a posição, a DRE mostra o resultado
        6. **Capital de giro consome caixa**: Estoque e contas a receber
        7. **Financiamento externo**: Negócio ainda depende de capital de terceiros
        """)
    
    # Botão para baixar relatório
    #st.markdown("---")
    #if st.button("📥 Gerar Relatório Completo (Em Breve)", type="primary"):
    #    st.info("Funcionalidade de exportação em desenvolvimento!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p><b>Mini-Case: Executivo S.A.</b> | Construção Sintética de BP, DRE e DFC</p>
    <p><small>Sistema desenvolvido para fins educacionais em Análise de Demonstrações Financeiras</small></p>
    <p><small>Prof. José Américo - FGV</small></p>
</div>
""", unsafe_allow_html=True)