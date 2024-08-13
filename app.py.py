import streamlit as st

# Função para converter a idade humana em anos felinos
def idade_humana_para_felina(idade_humana):
    if idade_humana <= 2:
        idade_felina = idade_humana * 12
    else:
        idade_felina = 24 + (idade_humana - 2) * 4
    return idade_felina

# Função para converter o tempo fora de casa em horas humanas para a perspectiva do gato
def horas_humanas_para_felinas(horas_humanas):
    fator_conversao = 4
    horas_felinas = horas_humanas * fator_conversao
    return horas_felinas

# Configuração da página
st.title('Calculadora de Idade Felina')

# Entradas do usuário
idade_humana = st.number_input('Idade do seu gato (em anos humanos):', min_value=0.0, step=0.1)
horas_humanas = st.number_input('Horas que você fica fora de casa:', min_value=0.0, step=0.1)

# Cálculos
if idade_humana and horas_humanas:
    idade_felina = idade_humana_para_felina(idade_humana)
    horas_felinas = horas_humanas_para_felinas(horas_humanas)

    # Exibição dos resultados
    st.write(f'A idade do seu gato em anos felinos é: {idade_felina:.2f} anos.')
    st.write(f'Quando você fica fora por {horas_humanas:.2f} horas, isso equivale a {horas_felinas:.2f} horas na perspectiva do seu gato.')

# Adiciona um botão para calcular
if st.button('Calcular'):
    st.write('Os resultados estão prontos!')

