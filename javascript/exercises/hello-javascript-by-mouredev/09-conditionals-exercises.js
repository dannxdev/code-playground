/*
Clase 24 - Ejercicios: Condicionales
Vídeo: https://youtu.be/1glVfFxj8a4?t=8652
*/

// if/else/else if/ternaria

// 1. Imprime por consola tu nombre si una variable toma su valor
let myName = 'Daniel'

if (myName == "Daniel") {
    console.log(myName)
}

// 2. Imprime por consola un mensaje si el usuario y contraseña concide con unos establecidos

let username = 'dannxdev';
let password = '12345';

if (username == 'dannxdev' && password == '12345') {
    console.log('Se ha iniciado sesion exitosamente.');
} else {
    console.log('Credenciales incorrectas, intente de nuevo.');
}

// 3. Verifica si un número es positivo, negativo o cero e imprime un mensaje

let myNumber = 1;

if (myNumber > 0) {
    console.log("El numero es positivo.");
} else if (myNumber < 0) {
    console.log("El numero es negativo.");
} else {
    console.log("El numero es cero.");
}

// 4. Verifica si una persona puede votar o no (mayor o igual a 18) e indica cuántos años le faltan

let ageUser = 7;

if (ageUser >= 18) {
    console.log('La persona puede votar.');
} else {
    console.log(`La persona no puede votar. Le faltan ${18 - ageUser} años.`);
};

// 5. Usa el operador ternario para asignar el valor "adulto" o "menor" a una variable
//    dependiendo de la edad

let state = ageUser >= 18 ? 'adulto' : 'menor'
console.log(state);

// 6. Muestra en que estación del año nos encontramos dependiendo del valor de una variable "mes"
// el invierno (dic-feb), primavera (mar-may), verano (jun-ago) y otoño (sep-nov)

let month = 'ago'

if (month == 'dic' || month == 'ene' || month == 'feb') {
    console.log('La estacion actual es Invierno.');

} else if (month == 'mar' || month == 'abr' || month == 'may') {
    console.log('La estacion actual es Primavera.');
    
} else if (month == 'jun' || month == 'jul' || month == 'ago') {
    console.log('La estacion actual es Verano.');

} else if (month == 'sep' || month == 'oct' || month == 'nov') {
    console.log('La estacion actual es Otoño.');

} else {
    console.log('Estacion del año desconocida.');
    
}

// 7. Muestra el número de días que tiene un mes dependiendo de la variable del ejercicio anterior

// 31 días: Enero, Marzo, Mayo, Julio, Agosto, Octubre, Diciembre (7 meses).
// 30 días: Abril, Junio, Septiembre, Noviembre (4 meses).
// 28 o 29 días: Febrero (28 en año común, 29 en bisiesto). 

let daysNumber;

if (['ene', 'mar', 'may', 'jul', 'ago', 'oct', 'dic'].includes(month)) {
    console.log(`El mes ${month} tiene 31 dias.`);
} else if (['abr', 'jun', 'sep', 'nov'].includes(month)) {
    console.log(`El mes ${month} tiene 30 dias.`);
} else if (month == 'feb') {
    console.log(`El mes ${month} tiene 28 - 29 dias.`);
} else {
    console.log(`Dias del mes ${month} desconocido.`);
}

// switch

// 8. Usa un switch para imprimir un mensaje de saludo diferente dependiendo del idioma

let language = 'ru';

switch (language) {
    case 'es':
        console.log('Hola, bienvenido al programa.');
        break
    case 'en':
        console.log('Hello, welcome to program');
        break
    case 'ru':
        console.log('Здравствуйте, добро пожаловать в программу.');
        break
    case 'ch':
        console.log('您好，歡迎收看本節目。');
        break
    default:
        console.log('Idioma no definido.');
}

// 9. Usa un switch para hacer de nuevo el ejercicio 6
let monthStation;

switch (month) {
    case 'dic':
        monthStation = 'Invierno';
        break
    case 'ene':
        monthStation = 'Invierno';
        break
    case 'feb':
        monthStation = 'Invierno';
        break
    case 'mar':
        monthStation = 'Primavera';
        break
    case 'abr':
        monthStation = 'Primavera';
        break
    case 'may':
        monthStation = 'Primavera';
        break
    case 'jun':
        monthStation = 'Verano';
        break
    case 'jul':
        monthStation = 'Verano';
        break
    case 'ago':
        monthStation = 'Verano';
        break
    case 'sep':
        monthStation = 'Otoño';
        break
    case 'oct':
        monthStation = 'Otoño';
        break
    case 'nov':
        monthStation = 'Otoño';
        break
    default:
        monthStation = 'Desconocida';

}

console.log(`La estacion actual es ${monthStation}`)

// 10. Usa un switch para hacer de nuevo el ejercicio 7

let monthDays;

switch (month) {
    case 'ene':
        monthDays = 31;
        break
    case 'feb':
        monthDays = 28;
        break
    case 'mar':
        monthDays = 31;
        break
    case 'abr':
        monthDays = 30;
        break
    case 'may':
        monthDays = 31;
        break
    case 'jun':
        monthDays = 30;
        break
    case 'jul':
        monthDays = 31;
        break
    case 'ago':
        monthDays = 31;
        break
    case 'sep':
        monthDays = 30;
        break
    case 'oct':
        monthDays = 31;
        break
    case 'nov':
        monthDays = 30;
        break
    case 'dic':
        monthDays = 31;
        break
    default:
        monthDays = 'Desconocido';
}

console.log(`El numero de dias del mes ${month} es ${monthDays}`);
