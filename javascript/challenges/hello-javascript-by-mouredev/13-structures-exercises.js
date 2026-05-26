/*
Clase 28 - Ejercicios: Estructuras
Vídeo: https://youtu.be/1glVfFxj8a4?t=11451
*/

// 1. Crea un array que almacene cinco animales
let animals = ['aguila', 'perro', 'gato', 'tortuga', 'caballo'];
console.log(animals);


// 2. Añade dos más. Uno al principio y otro al final
animals.unshift('lobo'); // anadiendo al principio.
animals.push('dragon'); // anadendo al final.
console.log(animals);

// 3. Elimina el que se encuentra en tercera posición
animals.splice(3,1);
console.log(animals);

// 4. Crea un set que almacene cinco libros
let myBooks = new Set(['Crimen y Castigo', 'Cien años de soledad', 'El cuervo', 'Don Quijote', 'El Principito']);
console.log(myBooks);

// 5. Añade dos más. Uno de ellos repetido
myBooks.add('Guerra Mundial Z');
myBooks.add('Don Quijote'); // No se anade porque ya esta en el set.
console.log(myBooks);

// 6. Elimina uno concreto a tu elección
myBooks.delete('El cuervo');
console.log(myBooks);

// 7. Crea un mapa que asocie el número del mes a su nombre
let monthsNumber = new Map([
    [1, 'Enero'],
    [2, 'Febrero'],
    [3, 'Marzo'],
    [4, 'Abril'],
    [5, 'Mayo'],
    [6, 'Junio'],
    [7, 'Julio'],
    [8, 'Agosto'],
    [9, 'Septiembre'],
    [10, 'Octubre'],
    [11, 'Noviembre'],
    [12, 'Diciembre'],
]);

console.log(monthsNumber);

// 8. Comprueba si el mes número 5 existe en el map e imprime su valor
console.log(monthsNumber.has(5));
console.log(monthsNumber.get(5));

// 9. Añade al mapa una clave con un array que almacene los meses de verano
monthsNumber.set("summerMonths", ['Junio', 'Julio', 'Agosto'])
console.log(monthsNumber);

// 10. Crea un Array, transfórmalo a un Set y almacénalo en un Map
let daysWeek = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"];
console.log(daysWeek);

daysWeek = new Set(daysWeek);
console.log(daysWeek);

let daysWeekMap = new Map();
daysWeekMap.set("days", daysWeek);
console.log(daysWeekMap);