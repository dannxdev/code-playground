/*
Clase 32 - Ejercicios: Funciones
Vídeo: https://youtu.be/1glVfFxj8a4?t=14146
*/

// NOTA: Explora diferentes sintaxis de funciones para resolver los ejercicios

function separator() {
    console.log("=========================");
};

// 1. Crea una función que reciba dos números y devuelva su suma

// classic function:

function sum(num1, num2) {
    return num1 + num2;
};

console.log(sum(5,12));

// anonymous function:

const sum2 = function(num1, num2) {return num1 + num2};

console.log(sum2(6, 8));

// arrow function:

const sum3 = (num1, num2) => {return num1 + num2};

console.log(sum3(10, 8));

// classic function with default params:

function sum4(num1 = 0, num2 = 0) {
    return num1 + num2;
};

console.log(sum4(10,5));
console.log(sum4(10));
console.log(sum4(undefined, 8));

separator();

// 2. Crea una función que reciba un array de números y devuelva el mayor de ellos

let myNumbers = [75, 15, 2, 4, 18, 26, 11, 3, 19, 13]

function maxNumArray(arrayNums) {
    let maxNum = arrayNums[0]

    for (let num of arrayNums) {   
        if (num > maxNum) {
            maxNum = num;
        };
    };

    return maxNum;
};

console.log(maxNumArray(myNumbers));

separator();

// 3. Crea una función que reciba un string y devuelva el número de vocales que contiene

let myString = "Hola, Este es codigo de javascript."

function countVocals(yourString) {
    let vocals = ['a', 'e', 'i', 'o', 'u'];
    let countVocals = 0;

    for (let char of yourString) {
        if (vocals.includes(char.toLowerCase())) {
            countVocals++;
        };
    };

    return countVocals;
};

console.log(countVocals(myString));

separator();

// 4. Crea una función que reciba un array de strings y devuelva un nuevo array con las strings en mayúsculas

let myArrayStrings = ["dannxdev", "hello", "javascript", "this is great!"]

function arrayUpper(arrayStrings) {
    let newArray = [];

    for (let str of arrayStrings) {
        newArray.push(str.toUpperCase());
    };

    return newArray;
};

console.log(arrayUpper(myArrayStrings));

separator();

// 5. Crea una función que reciba un número y devuelva true si es primo, y false en caso contrario

function isPrimeNumber(num) {
    if (num <= 1) {
        return false;
    };

    for (let i = 2; i < num; i++) {
        if (num % i == 0) {
            return false;
        };
    };

    return true;
};

console.log(isPrimeNumber(7));

// Method 2:

function isPrimeNumber2(num) {
    if (num <= 1) {
        return false;
    };

    let sqrtNum = Math.round(Math.sqrt(num))

    for (let i = 2; i < (sqrtNum + 1); i++) {
        if (num % i == 0) {
            return false;
        };
    };

    return true;
};

console.log(isPrimeNumber2(12));

separator();

// 6. Crea una función que reciba dos arrays y devuelva un nuevo array que contenga los elementos comunes entre ambos

let animals = ['perro', 'gato', 'pez', 'condor', 'aguila', 'tiburon', 'cuervo'];
let birds = ['lechuza', 'aguila', 'cuervo', 'canario'];

let digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
let otherNumbers = [1, 3, 5, 7, 9, 11, 13];

function commonItems(array1, array2) {
    let comItems = [];

    for (let item of array1) {
        if (array2.includes(item)) {
            comItems.push(item);
        };
    };

    return comItems;
};

console.log(commonItems(animals, birds));
console.log(commonItems(digits, otherNumbers));

separator();

// 7. Crea una función que reciba un array de números y devuelva la suma de todos los números pares

let myAges = [1, 5, 8, 10, 13, 14, 17, 20, 22]

function sumEvenNums(numsArray) {
    let sumEven = 0;

    for (let num of numsArray) {
        if (num % 2 == 0) {
            sumEven += num;
        };
    };

    return sumEven;
}

console.log(sumEvenNums(myAges));

separator();

// 8. Crea una función que reciba un array de números y devuelva un nuevo array con cada número elevado al cuadrado

function powNumbers(numsArray) {
    let powArray = [];

    for (let num of numsArray) {
        powArray.push(num**2);
    };

    return powArray;
};

console.log(powNumbers(myAges));

separator();

// 9. Crea una función que reciba una cadena de texto y devuelva la misma cadena con las palabras en orden inverso

let myPhrase = 'este es un string en javascript'

function reversedPhrase(yourPhrase) {
    let sepWords = [];
    let word = "";
    let revPhrase = "";

    for (let i = 0; i < yourPhrase.length; i++) {
        let char = yourPhrase[i];
        if (char != " " && (i != (yourPhrase.length - 1))) {
            word += char
        } else {
            if (i == (yourPhrase.length - 1)) {
                word += char;
            };
            sepWords.unshift(word);
            word = "";
        };
    };

    for (let k = 0; k < sepWords.length; k++) {
        let w = sepWords[k];
        revPhrase += w;
        if (k != (sepWords.length - 1)) {
            revPhrase += " ";
        };
    };
    return revPhrase;
};

console.log(reversedPhrase(myPhrase));

separator();

// 10. Crea una función que calcule el factorial de un número dado

function calcFactorial(num) {
    if (num > 1) {
        let product = 1;
        for (let i = 1; i <= num; i++) {
            product *= i;
        };
        return product;
    } else {
        return 1;
    };
};

console.log(calcFactorial(8))