import streamlit as st

st.logo("https://www.onlinelogomaker.com/blog/wp-content/uploads/2017/07/medical-logo.jp")
st.title("calculadora IMC")
st.subheader("meu primeiro programa Streamlit")

altura = st.number_input("digite a sua altura: ",min_value = 0.0)
peso = st.number_input("digite o seu peso: ", min_value = 0.0)

if st.button("calcular"):
    imc = peso / altura **2

    if imc < 18.5: 
        #st.image ("https://images.cults3d.com/IkjtyivjbhQRUER2fa1XdO8AxQI=/516x516/filters:no_upscale():format(webp)/https://fbi.cults3d.com/uploaders/31765151/illustration-file/7f6329ca-5f38-4bda-98f1-16fcfa28c2dc/Creeper.png", width=150)
        st.error ("abaixo do peso. ")

    elif imc < 24.9:
        
        st.success("peso normal") 
    elif imc <  29.9:
        
        st.warning("sobre peso")   
    elif imc < 34.4:
       
        st.error("obesidade Grau I") 
    elif imc < 39.9:
        st.error ("obesidade Grau II")    

    else:
        st.error("obesidade Grau III")














