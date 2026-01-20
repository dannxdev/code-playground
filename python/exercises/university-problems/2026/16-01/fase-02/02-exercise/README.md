# Ejercicio 2: Control de Reservas de Salas de Estudio

Una biblioteca universitaria requiere gestionar las reservas de salas de estudio. Cada reserva debe tener un usuario responsable, una hora de inicio y una tarifa por hora.

---

### Especificaciones de la Clase: `ReservaSala`

* **Atributos privados:** * `_usuario`
* `_hora_inicio`
* `_tarifa_hora`


* **Métodos:**
* `registrar_inicio(hora)`
* `registrar_fin(hora)`
* `calcular_costo(hora_fin)`
* `obtener_usuario()`

---

### Requerimientos del Programa

El programa debe cumplir con las siguientes funciones:

* **Crear reservas** y almacenarlas en una lista.
* Permitir **seleccionar una reserva** y registrar la hora de fin.
* **Calcular automáticamente** el costo final.
* **Validar** horas incorrectas o vacías.