import streamlit as st

# Lista global para almacenar actividades
if "actividades" not in st.session_state:
    st.session_state.actividades = []


menu = st.sidebar.selectbox(
    "Menú",
    ["Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4"]
)

# Agregando las opciones mínimas del menú
if menu == "Home":
    st.title("Módulo 1 - Python Fundamental")
    st.write("Nombre: Gianella Blanca Vasquez Calderón")
    st.write("Curso: Especialización en Python for Analytics")
    st.write("Año: 2026")
    st.write("Descripción: Aplicación desarrollada en Streamlit que integra variables, estructuras de datos, funciones, programación funcional y POO.")
    st.write("Tecnologías: Python, Streamlit")

#INICIO DE LOS EJERCICIOS 

#  EJERCICIO 1
elif menu == "Ejercicio 1":
    st.subheader("Verificador de Presupuesto y Gasto")

    presupuesto = st.number_input("Ingrese su presupuesto", min_value=0.00)
    gasto = st.number_input("Ingrese su gasto contemplado", min_value=0.00)

    if st.button("Evaluar"):
        diferencia = presupuesto - gasto
        
        if gasto <= presupuesto:
            st.success("El gasto está dentro del presupuesto.")
        else:
            st.warning("El presupuesto fue excedido.")

        st.write(f"La diferencia del presupuesto con respecto al gasto es: {diferencia}")

#EJERCICIO 2

elif menu == "Ejercicio 2":
    st.subheader("Registro de Actividades")

    nombre = st.text_input("Nombre actividad")
    tipo = st.text_input("Tipo")
    presupuesto = st.number_input("Presupuesto")
    gasto_real = st.number_input("Gasto real")

    if st.button("Agregar actividad"):
        actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real
        }
        st.session_state.actividades.append(actividad)

    st.write("Lista de actividades:")
    st.dataframe(st.session_state.actividades)

    for act in st.session_state.actividades:
        if act["gasto_real"] <= act["presupuesto"]:
            st.write(f"{act['nombre']} está dentro del presupuesto")
        else:
            st.write(f"{act['nombre']} excedió el presupuesto")

#EJERCICIO 3

elif menu == "Ejercicio 3":
    st.title("Cálculo de Retorno Esperado")

    tasa = st.slider("Tasa", 0.0, 1.0, 0.1)
    meses = st.number_input("Meses", min_value=1)

    def calcular_retorno(actividad, tasa, meses):
        return actividad["presupuesto"] * tasa * meses

    if st.button("Calcular retorno"):
        retornos = list(map(lambda act: calcular_retorno(act, tasa, meses), st.session_state.actividades))

        for i, act in enumerate(st.session_state.actividades):
            st.write(f"{act['nombre']} → Retorno esperado: {retornos[i]}")


#EJERCICIO 4

elif menu == "Ejercicio 4":
    st.subheader("Programación Orientada a Objetos")

    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        def esta_en_presupuesto(self):
            return self.gasto_real <= self.presupuesto

        def mostrar_info(self):
            return f"{self.nombre} - {self.tipo} | Presupuesto: {self.presupuesto} | Gasto: {self.gasto_real}"

    objetos = []

    for act in st.session_state.actividades:
        obj = Actividad(
            act["nombre"],
            act["tipo"],
            act["presupuesto"],
            act["gasto_real"]
        )
        objetos.append(obj)

    for obj in objetos:
        st.write(obj.mostrar_info())
        if obj.esta_en_presupuesto():
            st.success("Esta dentro del presupuesto")
        else:
            st.warning("Excede el presupuesto")
