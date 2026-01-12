## 📝 Problema 1: Gestión de Inscripciones a Cursos

Este problema es una **evaluación final** en la que el estudiante debe desarrollar un programa para gestionar la inscripción de estudiantes en una escuela técnica.

---

### 🏫 Oferta de Cursos

La escuela ofrece tres cursos, cada uno con un costo por mes, duración y un descuento aplicable solo al **Pago Completo**.

| Curso | Costo por Mes | Duración (Meses) | Descuento por Pago Completo |
| :--- | :---: | :---: | :---: |
| **Programación** | $300,000 | 6 | 20% |
| **Diseño Gráfico** | $250,000 | 4 | 15% |
| **Redes** | $200,000 | 5 | 10% |

> **Nota:** El costo total del curso se calcula multiplicando el **Costo por Mes** por la **Duración**.

---

### 💳 Modalidades de Pago

La escuela maneja dos (2) modalidades de pago para los estudiantes:

* **Pago Completo:** Se aplica el **descuento** especificado en la tabla anterior.
* **Pago Mensual:** **No** se aplica ningún descuento.

---

### 💻 Requerimiento del Programa

Se requiere desarrollar un programa que permita inscribir a un número **X** de estudiantes. Al finalizar las inscripciones, el programa debe mostrar los siguientes **cinco (5) resultados** consolidados:

1.  **Cantidad de Estudiantes** inscritos en cada curso (Programación, Diseño Gráfico, Redes).
2.  **Duración Total en Meses** de **todos** los cursos inscritos.
3.  **Costo Total Bruto** de todos los cursos inscritos (sin aplicar ningún descuento).
4.  **Monto Total de Descuentos** aplicados (solo para los estudiantes que eligieron Pago Completo).
5.  **Valor Neto Total** de todas las inscripciones (después de aplicar los descuentos).