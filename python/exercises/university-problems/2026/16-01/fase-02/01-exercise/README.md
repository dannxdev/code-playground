# Ejercicio 1: Sistema de Control de Bicicletas en un Taller

Un taller de bicicletas requiere un sistema que permita registrar el ingreso de bicicletas para mantenimiento y calcular el costo total del servicio según el tiempo transcurrido.

El estudiante debe desarrollar una aplicación que gestione bicicletas usando **Programación Orientada a Objetos** y **encapsulación**.

---

### Especificaciones de la Clase: `BicicletaTaller`

* **Atributos privados:** * `_serial`
* `_hora_ingreso`
* `_costo_por_hora`


* **Métodos:**
* `registrar_ingreso(hora)`: Para almacenar la hora de ingreso.
* `registrar_salida(hora)`: Para registrar la salida.
* `calcular_total(hora_salida)`: Para calcular el costo final.
* `obtener_serial()`: Para identificar la bicicleta.

---

### Requerimientos del Sistema

El sistema debe cumplir con las siguientes funcionalidades:

1. **Registrar** bicicletas con sus datos correspondientes.
2. **Guardarlas** en una lista interna.
3. Permitir **seleccionar** una bicicleta para registrar su salida.
4. **Calcular** automáticamente el costo.
5. **Validar** que la hora de salida sea mayor a la de ingreso.