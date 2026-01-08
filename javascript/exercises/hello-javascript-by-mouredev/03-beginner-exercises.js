/*
Clase 18 - Ejercicios: primeros pasos
Vídeo: https://youtu.be/1glVfFxj8a4?t=4733
*/

// 1. Escribe un comentario en una línea

// Este es un comentario en una linea 😒.

// 2. Escribe un comentario en varias líneas

/*
Un comentario de varia lineas es muy util para
documentar nuestro codigo y que se vea mas chevere.
*/

/**
 * Este es otro tipo de comentarios multilinea
 * mas visibles y mas bonitos de vizualizar.
 */

// 3. Declara variables con valores asociados a todos los datos de tipo primitivos

let myName = 'Daniel'; //string
let myAge = 22; // number
let myHeight = 1.78; // number
let isMale = true; // boolean
let isFemale = false; // boolean
let isChild = 22 > 18 // boolean
let hisFuture; // undefined
let herFuture = undefined; // undefined
let hisPrice = null; // null
let mySymbol = Symbol("dannx"); // symbol
let hisMoney = BigInt(1234567891011121314151617181920); // BigInt
let hisBuys = 1234567891011121314151617181920n; // BigInt

// 4. Imprime por consola el valor de todas las variables

console.log(myName)
console.log(myAge)
console.log(myHeight)
console.log(isMale)
console.log(isFemale)
console.log(isChild)
console.log(hisFuture)
console.log(herFuture)
console.log(hisPrice)
console.log(mySymbol)
console.log(hisMoney)
console.log(hisBuys)

// 5. Imprime por consola el tipo de todas las variables

console.log(typeof myName)
console.log(typeof myAge)
console.log(typeof myHeight)
console.log(typeof isMale)
console.log(typeof isFemale)
console.log(typeof isChild)
console.log(typeof hisFuture)
console.log(typeof herFuture)
console.log(typeof hisPrice)
console.log(typeof mySymbol)
console.log(typeof hisMoney)
console.log(typeof hisBuys)

// 6. A continuación, modifica los valores de las variables por otros del mismo tipo

myName = "Daniel Benavides";
myAge = 23;
isMale = false

// 7. A continuación, modifica los valores de las variables por otros de distinto tipo

myName = 43131;
myAge = "veintidos";
isMale = "yes";
isFemale = "no";
isChild = "es un joven";
hisFuture = true;
hisPrice = BigInt(1234567891011121314151617181920);;
mySymbol = "dannx";

// 8. Declara constantes con valores asociados a todos los tipos de datos primitivos

const bornYear = 2003;
const fullName = 'Everson Daniel Cumbalaza Benavides';
const hisGirlfriend = false;
const theFuture = undefined;
const hisRegister = null;
const nickname = Symbol('danny');
const bigNumber = BigInt(33322332222221566977899545033874);

// 9. A continuación, modifica los valores de las constantes

/*
theFuture = 'software';
hisRegister = true;
nickname = Symbol('dannx');
*/

// 10. Comenta las líneas que produzcan algún tipo de error al ejecutarse

// hecho ✅