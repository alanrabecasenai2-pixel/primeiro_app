import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Calculadora - Pilar do Sul SP",
    page_icon="🌲",
    layout="centered"
)

# Estilização CSS personalizada
st.markdown("""
    <style>
    /* Fundo da aplicação */
    .stApp {
        background-color: #F0F7F4;
    }

    /* Estilização da imagem do brasão */
    .brasao-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 120px;
        margin-bottom: 10px;
    }

    /* Botão de ação estilizado em verde */
    .stButton>button {
        background-color: #2E8B57;
        color: white;
        border-radius: 12px;
        border: none;
        font-weight: bold;
        font-size: 18px;
        width: 100%;
        padding: 12px;
        transition: all 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #1E5631;
        color: #FFFFFF;
        transform: scale(1.02);
    }

    /* Destaque nos títulos */
    h1 {
        color: #1E5631;
        text-align: center;
    }

    /* Animação Pop-In para o resultado */
    @keyframes popIn {
        0% {
            opacity: 0;
            transform: scale(0.5) rotate(-3deg);
        }
        80% {
            transform: scale(1.05) rotate(1deg);
        }
        100% {
            opacity: 1;
            transform: scale(1) rotate(0deg);
        }
    }

    /* Cartão de Resultado Pilarense */
    .result-card-pilar {
        background: linear-gradient(135deg, #2E8B57 0%, #1E5631 100%);
        padding: 24px;
        border-radius: 20px;
        text-align: center;
        color: #FFFFFF;
        font-size: 36px;
        font-weight: bold;
        margin-top: 20px;
        box-shadow: 0 10px 25px rgba(30, 86, 49, 0.3);
        animation: popIn 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    }
    </style>
""", unsafe_allow_html=True)

# Exibição do Brasão Oficial de Pilar do Sul
st.markdown(
    '''
    <img src="https://upload.wikimedia.org/wikipedia/commons/2/23/Brasao-pilardosul-sp.PNG" class="brasao-img" alt="Brasão de Pilar do Sul SP">
    ''',
    unsafe_allow_html=True
)

# Título e cabeçalho
st.title("🌲 Calculadora Pilarense")
st.write("Um toque de Pilar do Sul - SP para as suas contas do dia a dia!")

st.divider()

# Formulário de entrada
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro Número", value=0.0, step=1.0)

with col2:
    num2 = st.number_input("Segundo Número", value=0.0, step=1.0)

# Seleção da operação
operacao = st.radio(
    "Escolha a Operação:",
    ["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"],
    horizontal=True
)

st.divider()

# Botão de Ação e Lógica de Cálculo
if st.button("Calcular em Pilar do Sul"):
    resultado = None

    if operacao == "Soma (+)":
        resultado = num1 + num2
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
    elif operacao == "Divisão (/)":
        if num2 == 0:
            st.error("Ops! Não é possível dividir por zero.")
        else:
            resultado = num1 / num2

    # Exibição do resultado com o efeito
    if resultado is not None:
        st.balloons()

        st.markdown(
            f'''
            <div class="result-card-pilar">
                Resultado: {resultado:g} 🍇
            </div>
            ''', 
            unsafe_allow_html=True
        )

# Feito
        
