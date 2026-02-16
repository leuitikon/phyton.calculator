import streamlit as st

def add(n1, n2): return n1 + n2
def subtract(n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2): 
    return n1 / n2 if n2 != 0 else "Erro: Divisão por zero"

functions = {"+": add, "-": subtract, "*": multiply, "/": divide}

st.title("🔢 Minha Calculadora Web")

# Campos para os números
n1 = st.number_input("Digite o primeiro número", value=0.0)
n2 = st.number_input("Digite o segundo número", value=0.0)

# Seleção da operação
op = st.selectbox("Escolha a operação", list(functions.keys()))

if st.button("Calcular"):
    resultado = functions[op](n1, n2)
    st.divider()
    st.subheader(f"Resultado: {resultado}")
    if isinstance(resultado, (int, float)):
        st.balloons()
