# Juego del Cazador de Contraseñas

Cada estudiante deberá desarrollar, de manera individual, un juego interactivo en Python, utilizando Programación Orientada a Objetos y principios de aleatoriedad, validación estricta y manejo de excepciones. El propósito del juego es que el estudiante, en el rol de un Cazador de 3 Contraseñas, genere contraseñas válidas para abrir cofres y acumular puntos, al mismo tiempo que enfrenta penalizaciones cuando la contraseña generada no cumple con los requisitos establecidos.

## Requerimientos de la contraseña

El programa debe generar contraseñas completamente aleatorias y verificar que cumplan las siguientes condiciones obligatorias:

- Longitud definida por el usuario (mínimo 8 caracteres).
- Debe contener al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un número,
  - un carácter especial de esta lista: `¿¡?=)(/¨*+-%&$#!`
- No debe tener caracteres repetidos.

La asignación de caracteres debe ser aleatoria, sin orden predecible.

## Manejo de errores

El sistema debe manejar errores mediante excepciones personalizadas cuando el usuario ingrese una longitud inválida, datos no numéricos o cuando la contraseña sea incorrecta.

## Estructura de clases (obligatorio)

El juego debe estar estructurado obligatoriamente en Programación Orientada a Objetos, incluyendo al menos las siguientes clases:

- **Clase Contraseña**: encargada de generar y validar contraseñas.
- **Clase Cofre**: representa los cofres que se abren dependiendo de la calidad de la contraseña; pueden ser:
  - Común (+10 puntos)
  - Raro (+25 puntos)
  - Legendario (+50 puntos)
  - Maldito (–20 puntos cuando la contraseña es inválida)
- **Clase JuegoCazador**: administra el puntaje, controla el flujo del juego, maneja las excepciones y permite que el usuario juegue varias rondas.

## Funcionamiento del juego

El juego debe permitir al estudiante generar contraseñas tantas veces como quiera. Cada contraseña válida abrirá un cofre aleatorio que otorga puntos positivos; una contraseña inválida abrirá un cofre maldito que resta puntos. El juego debe mostrar la contraseña generada, el tipo de cofre obtenido, los puntos acumulados y permitir al usuario decidir si continúa jugando o desea salir.

## Entregable

El estudiante deberá entregar un archivo `.py` totalmente funcional, con comentarios explicativos, código limpio y evidencia de ejecución del juego.