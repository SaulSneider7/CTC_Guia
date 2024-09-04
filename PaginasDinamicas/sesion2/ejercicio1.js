/*
Crearemos un programa que generará un número al azar entre 0 y 100 que el jugador deberá adivinar.

El jugador tendrá 5 intentos para ingresar el número que cree correcto y el navegador deberá evaluar 
el número recibido.

→ Si el número corresponde al generado por el programa, se mostrará un mensaje de felicitaciones y 
el número de intentos que se necesitaron para adivinar el número.

→ Si el número es incorrecto, se mostrará al jugador un mensaje que indique si el número ingresado 
es menor o mayor al generado por el programa. Además se mostrarán los intentos restantes.
*/

// Primero generaremos el número. Utilizaremos el método random de la librería Math, el cual genera 
// número aleatorio decimal entre 0 y 1, por lo que deberemos multiplicarlo por 100 y transformarlo en entero
// para que el número generado esté entre 0 y 100.
let numeroGenerado = parseInt(Math.random() * 100);

// Se puede agregar console.log(numeroGenerado) aquí para conocer el número

// Luego declararemos el número de intentos máximos permitidos y los intentos gastados al iniciar
// el juego.
const intentosMaximos = 5;
let intentosGastados = 0;

// Ahora le explicaremos las reglas al jugador utilizando un alert.
alert("Tu misión es adivinar el número en el que está pensando la computadora. Este número está entre 0 y 100.\nTienes 5 intentos.");

// Antes de solicitar al usuario que ingrese un número, declararemos una variable que almacene precisamente
// este número.
let numeroIngresado = -1;  // Primero valdrá -1 (que no está dentro del rango de números) para evitar errores.

// También agregaremos una variable con valor booleano que almacene si el número ingresado por el jugador
// es igual al generado.
let correcto = false;

// Se pedirá al jugador que ingrese un número mientras le queden intentos y no haya acertado.
while (intentosGastados < intentosMaximos && !correcto) { // también se puede escribir correcto == false
    numeroIngresado = prompt(`Ingrese un número entre 0 y 100.`);

    // Aumentamos en 1 intentosGastados
    intentosGastados++;

    if (numeroIngresado == numeroGenerado) {
        correcto = true;
    } else if (numeroIngresado < numeroGenerado) {
        // La sintaxis utilizada para construir el string permite crear cadenas de caracteres con formato, es decir,
        // que incluyen fragmentos que serán reemplazados con el valor de la o las variables deseadas.
        alert(`El número ingresado es menor al correcto.\nTe quedan ${intentosMaximos - intentosGastados} intentos.`);
    } else {
        alert(`El número ingresado es mayor al correcto.\nTe quedan ${intentosMaximos - intentosGastados} intentos.`);
    }
}

// Se termina el ciclo si: a) se adivinó el número, b) se acabaron los intentos.
if (correcto) {  // también puede escribirse: correcto == true (aunque esto es redundante)
    alert(`¡Has ganado! Felicidades, el número correcto es ${numeroGenerado}.\nTe tomó ${intentosGastados} intentos adivinarlo.`);
} else {
    alert(`Se te han acabado los intentos. El número correcto era ${numeroGenerado}.`);
}