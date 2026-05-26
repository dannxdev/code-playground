/*
Clase 22 - Ejercicios: Strings
Vídeo: https://youtu.be/1glVfFxj8a4?t=7226
*/

// 1. Concatena dos cadenas de texto
let myText = "Lorep ipsum dal";
let secondText = " fact kan replace"
let joinTexts = myText + secondText + "???";
console.log(joinTexts)

// 2. Muestra la longitud de una cadena de texto
console.log(joinTexts.length);

// 3. Muestra el primer y último carácter de un string
console.log(joinTexts[0]);
console.log(joinTexts[34]);

// 4. Convierte a mayúsculas y minúsculas un string
console.log(joinTexts.toLowerCase());
console.log(joinTexts.toUpperCase());

// 5. Crea una cadena de texto en varias líneas
let multiLineText = `
Un string de varias lineas.
muy util para hacer el 
texto mas legible.
`;

console.log(multiLineText);

// 6. Interpola el valor de una variable en un string
let myName = 'Daniel';
let age = 22;

console.log(`Hola!, soy ${myName} y tengo ${age} años.`);

// 7. Reemplaza todos los espacios en blanco de un string por guiones
console.log(myText.replace(" ", "_"));
console.log(joinTexts.replaceAll(" ", "_"));

// 8. Comprueba si una cadena de texto contiene una palabra concreta
console.log(myText.includes('ipsum'));

// 9. Comprueba si dos strings son iguales
console.log(myText === myName);

// 10. Comprueba si dos strings tienen la misma longitud
console.log(myName.length === myText.length);