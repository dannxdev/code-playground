/*
Clase 20 - Ejercicios: Operadores
Vídeo: https://youtu.be/1glVfFxj8a4?t=6458
*/

// 1. Crea una variable para cada operación aritmética
let suma = 22 + 18;
let resta = 22 - 18;
let multipl = 22 * 18;
let division = 22 / 18;
let resto = 22 % 18;
let potencia = 22 ** 18;

// 2. Crea una variable para cada tipo de operación de asignación,
//    que haga uso de las variables utilizadas para las operaciones aritméticas

suma = 40;
console.log(suma == resta);
console.log(resta === "4");
console.log(multipl !== 100);

// 3. Imprime 5 comparaciones verdaderas con diferentes operadores de comparación
console.log(suma < multipl);
console.log(potencia > resta);
console.log(suma >= division);
console.log(multipl <= potencia);
console.log(resta == "4");

// 4. Imprime 5 comparaciones falsas con diferentes operadores de comparación
console.log(suma >= multipl);
console.log(potencia < 100);
console.log(suma >= "41");
console.log(multipl == potencia);
console.log(resta > 10);

// 5. Utiliza el operador lógico and
console.log(suma > 10 && resta > division);

// 6. Utiliza el operador lógico or
console.log(multipl < 1 || resto < 1.5);

// 7. Combina ambos operadores lógicos
console.log(10 < suma && 50 >= resto || division !== 0);

// 8. Añade alguna negación
console.log(!(resta > 120))

// 9. Utiliza el operador ternario
let age = 8;
(age >= 18) ? console.log('Es mayor de edad.'): console.log('Es menor de edad.'); 

// 10. Combina operadores aritméticos, de comparáción y lógicas

console.log(!((suma+50)>((resta) / (resta+1))) && ((80/2) === (suma*1)));