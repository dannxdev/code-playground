# Problema 3: Sistema de Gestión de Empleados y Bonos

Una empresa requiere un sistema para gestionar la información de sus empleados, organizados por departamentos. El sistema debe calcular el salario anual y los bonos correspondientes según el nivel de desempeño de cada trabajador.

## Requisitos del Sistema

1. **Entrada de Datos Inicial:** Solicitar al usuario el número total de empleados a registrar.
2. **Registro de Información:** Para cada empleado, se debe ingresar la siguiente información:

* **Nombre** del empleado.
* **Departamento** (Ejemplos: Ventas, Recursos Humanos, Ingeniería, Finanzas).
* **Salario mensual.**
* **Nivel de desempeño:** Una escala numérica del **1 al 5** (donde 1 es el nivel más bajo y 5 el más alto).

---

## Cálculo de Bonos Anuales

El bono se calcula aplicando un porcentaje sobre el **salario anual** del empleado, dependiendo de su calificación de desempeño:

| Nivel de Desempeño | Bono (Sobre el Salario Anual) |
| --- | --- |
| **5** | 20% |
| **4** | 15% |
| **3** | 10% |
| **2** | 5% |
| **1** | No recibe bono (0%) |

---

## Salidas del Programa (Resultados)

Al finalizar el procesamiento de los datos, el programa debe mostrar:

* **Detalle Individual:** El salario anual total para cada empleado (sumando el salario base y el bono).
* **Resumen Contable:** El total de la nómina anual de todos los empleados combinados.
* **Reconocimiento:** Identificar y mostrar el nombre del empleado con el salario anual más alto.