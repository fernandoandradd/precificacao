import streamlit as st

def calcular_markup(preco_custo, percentual):
    markup = preco_custo * (1 + percentual / 100)
    return markup

def calcular_margem(preco_custo, markup):
    margem = (markup - preco_custo) / markup * 100
    return margem

def calcular_preco_venda(preco_custo, margem):
    margem = margem / 100
    markup = (1 - margem)
    preco_venda = preco_custo / markup
    return preco_venda

def retornar_margem(preco_custo, preco_venda):
    resultado_venda = preco_venda - preco_custo
    margem_venda = (resultado_venda / preco_venda) * 100
    return  margem_venda


# Configuração inicial do Streamlit
st.image("image.jpg", use_column_width=True)
st.title("Calculadora de Markup e Margem")


# Entrada de dados do usuário
preco_custo = st.number_input("Informe o preço de custo:", min_value=0.0)
percentual_markup = st.number_input("Informe o percentual desejado (%):", min_value=0.0, max_value=99.99)

# Botão para calcular e exibir resultados
if st.button("Calcular"):
    markup_calculado = calcular_markup(preco_custo, percentual_markup)
    valor_markup = markup_calculado - preco_custo
    margem_calculada = calcular_margem(preco_custo, markup_calculado)

    preco_margem = calcular_preco_venda(preco_custo, percentual_markup)
    valor_margem =  preco_margem - preco_custo
    margem_preco = retornar_margem(preco_custo, preco_margem)


    # Exibindo resultados
    st.subheader("Resultado Markup:")
    st.write(f"Markup calculado = R$ {markup_calculado:.2f}".replace(".", ","))
    st.write(f"Lucro Bruto em Valores(Preço de venda - custo da mercadoria) = R$ {valor_markup:.2f}".replace(".", ","))
    st.write(f"Percentual de Lucro Sobre a Venda (Lucro Bruto / Valor de Venda ) = {margem_calculada:.2f}%".replace(".", ","))


    # Exibindo resultados
    st.subheader("Resultado margem:")
    st.write(f"Margem calculada = R$ {preco_margem:.2f}".replace(".", ","))
    st.write(f"Lucro Bruto em Valores(Preço de venda - custo da mercadoria) = R$ {valor_margem:.2f}".replace(".", ","))
    st.write(f"Percentual de Lucro Sobre a Venda (Lucro Bruto / Valor de Venda) = {margem_preco:.2f}%".replace(".", ","))

# Dica: Você pode personalizar ainda mais a aparência e o layout usando os recursos do Streamlit.
