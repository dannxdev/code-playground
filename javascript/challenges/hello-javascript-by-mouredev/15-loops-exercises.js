/*
Clase 30 - Ejercicios: Bucles
Vídeo: https://youtu.be/1glVfFxj8a4?t=12732
*/

// NOTA: Explora diferentes sintaxis de bucles para resolver los ejercicios

function separator() {
    console.log("=========================")
}

// 1. Crea un bucle que imprima los números del 1 al 20

// con for:

for (let i = 1; i <= 20; i++) {
    console.log(i);
}

// con while:

let myNum = 1;

while (myNum <= 20) {
    console.log(myNum);
    myNum++;
};

separator();

// 2. Crea un bucle que sume todos los números del 1 al 100 y muestre el resultado

// con for:

let suma = 0;

for (let num = 1; num <= 100; num++) {
    suma += num;
};

console.log(suma);

// con while: 

let start = 1;
suma = 0;

while (start <= 100) {
    suma += start;
    start++;
};

console.log(suma);

separator();

// 3. Crea un bucle que imprima todos los números pares entre 1 y 50

// con for:

for (let index = 1; index <= 50; index++) {
    if (index % 2 == 0) {
        console.log(index)
    };
};

// con while:

let indice = 1;

while (indice <= 50) {
    if (indice % 2 == 0) {
        console.log(indice);
    }
    indice++;
}

separator();

// 4. Dado un array de nombres, usa un bucle para imprimir cada nombre en la consola

let myNames = ["Daniel", "Luis", "Brayan", "Dayana", "Pedro"]

// con for:

for (let i = 0; i < myNames.length; i++) {
    console.log(myNames[i]);
};

// con for of:

for (let name of myNames) {
    console.log(name);
};

// con while:

let ind = 0;

while (ind < myNames.length) {
    console.log(myNames[ind]);
    ind++;
};

separator();

// 5. Escribe un bucle que cuente el número de vocales en una cadena de texto

// con for of:

let myString = "Este es un string de prueba";
let vocals = ['a', 'e', 'i', 'o', 'u'];
let countVocals = 0;

for (let char of myString) {
    if (vocals.includes(char.toLowerCase())) {
        countVocals++;
    };
};

console.log(`Tu String contiene ${countVocals} ${countVocals == 1 ? "vocal": "vocales"}`);

// con for:

countVocals = 0;

for (let i = 0; i < myString.length; i++) {
    if (vocals.includes(myString[i].toLowerCase())) {
        countVocals++;
    };
};

console.log(`Tu String contiene ${countVocals} ${countVocals == 1 ? "vocal": "vocales"}`);

// con while:

let myIndex = 0;
countVocals = 0;

while (myIndex < myString.length) {
    if (vocals.includes(myString[myIndex].toLowerCase())) {
        countVocals++;
    };
    myIndex++
};

console.log(`Tu String contiene ${countVocals} ${countVocals == 1 ? "vocal": "vocales"}`);

separator();

// 6. Dado un array de números, usa un bucle para multiplicar todos los números y mostrar el producto

// con for of:

let arrayNumbers = [2, 7, 3, 8, 9];
let product = 1;

for (let num of arrayNumbers) {
    product *= num
}

console.log(product);

// con for:

product = 1;

for (let i = 0; i < arrayNumbers.length; i++) {
    product *= arrayNumbers[i];
};

console.log(product);

// con while:

let factor = 0 // index
product = 1

while (factor < arrayNumbers.length) {
    product *= arrayNumbers[factor];
    factor++
};

console.log(product);

separator();

// 7. Escribe un bucle que imprima la tabla de multiplicar del 5

// Con for:

for (let f = 0; f <= 10; f++) {
    console.log(`5 x ${f} = ${5 * f}`);
}

// con while:

let k = 0

while (k <= 10) {
    console.log(`5 x ${k} = ${5 * k}`);
    k++;
}

separator();

// 8. Usa un bucle para invertir una cadena de texto

// con for:

let myNickname = 'dannxdev';
let myNicknameReversed = "";

for (let i = myNickname.length - 1; i >= 0; i--) {
    myNicknameReversed += myNickname[i]
}

console.log(myNicknameReversed)

// con while:

let h = myNickname.length - 1;
myNicknameReversed = "";

while (h >= 0) {
    myNicknameReversed += myNickname[h];
    h--

}

console.log(myNicknameReversed)

separator();

// 9. Usa un bucle para generar los primeros 10 números de la secuencia de Fibonacci

// Con for:

let a = 0;
let b = 1;
let fib = 0;

for (let i = 0; i < 10; i++) {
    console.log(fib);
    fib = a + b;
    a = b;
    b = fib;
}

// Con while:

a = 0;
b = 1;
fib = 0;

let x = 0;

while (x < 10) {
    console.log(fib);
    fib = a + b;
    a = b;
    b = fib;

    x++;
}

separator();


// 10. Dado un array de números, usa un bucle para crear un nuevo array que contenga solo los números mayores a 10

// con for of:

let randomNumbers = [7, 15, 2, 4, 18, 26, 11, 3, 19, 13];
let greatNumbers = [];

for (let num of randomNumbers) {
    if (num > 10) {
        greatNumbers.push(num);
    };
}

console.log(greatNumbers);

// con for:

greatNumbers = [];

for (let i = 0; i < randomNumbers.length; i++) {
    if (randomNumbers[i] > 10) {
        greatNumbers.push(randomNumbers[i]);
    };
};

console.log(greatNumbers);

// con while:

greatNumbers = [];
let y = 0;

while (y < randomNumbers.length) {
    if (randomNumbers[y] > 10) {
        greatNumbers.push(randomNumbers[y]);
    };
    y++
};

console.log(greatNumbers);

separator();

