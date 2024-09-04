// ---------------- PARTE 1 ----------------
let n = parseInt(prompt("Ingrese el número de caracteres a mostrarse: "));
// Patrón 1
let division1 = parseInt(n / 2);  // Tenemos 2 caracteres distintos

let patron1 = "";

for (let i = 0; i < division1; i++) {
    patron1 += "*.";
}
// Si n es par el patrón queda tal cual, si es impar debemos agregar un asterisco más.
if (n % 2 != 0) {  // n impar
    patron1 += "*";
}

document.write(patron1 + "<br><br>");

// Patrón 2
let division2 = parseInt(n / 4);  // Tenemos 4 caracteres distintos

let patron2 = "";
for (let i = 0; i < division2; i++) {
    patron2 += "1234";
}

if (n % 4 != 0) {
    for (let j = 1; j <= n % 4; j++) {
        patron2 += j;
    }
}

document.write(patron2 + "<br><br>");


// Patrón 3
let division3 = parseInt(n / 3);  // Tenemos 3 caracteres distintos

let patron3 = "";
for (let i = 0; i < division3; i++) {
    patron3 += "||*";
}

if (n % 3 == 1) {
    patron3 += "|";
} else if (n % 3 == 2) {
    patron3 += "|";
}

document.write(patron3 + "<br><br>");


// ---------------- PARTE 2 ----------------
let m = parseInt(prompt("Ingrese el tamaño de los patrones anidados a mostrarse: "));

// Patron 1: CUADRADO
let patronAnidado1 = "";

// Fila superior
for (let i = 0; i < m; i++) {
    patronAnidado1 += "*";
}

// Luego va un salto de linea
patronAnidado1 += "<br>";

// Filas intermedias
for (let j = 0; j < m - 2; j++) {
    patronAnidado1 += "*";
    for (let k = 0; k < m - 2; k++) {
        patronAnidado1 += "&nbsp;&nbsp;";  // &nbsp; representa un espacio. Colocamos dos por estética, pero lo correcto sería poner solo uno.
    }
    patronAnidado1 += "*";
    // Luego va un salto de linea
    patronAnidado1 += "<br>";
}

// Fila inferior
if (m > 1) {
    for (let l = 0; l < m; l++) {
        patronAnidado1 += "*";
    }
}

patronAnidado1 += "<br><br>";
document.write(patronAnidado1);

// Patron 2: Z
let patronAnidado2 = "";
// Fila superior
for (let i = 0; i < m; i++) {
    patronAnidado2 += "*";
}
patronAnidado2 += "<br>";

// Diagonal
for (let j = 0; j < m - 2; j++) {
    for (let k = m - 2 - j; k > 0; k--) {
        patronAnidado2 += "&nbsp;&nbsp;";
    }
    patronAnidado2 += "*<br>";
}

// Fila inferior
if (m > 1) {
    for (let l = 0; l < m; l++) {
        patronAnidado2 += "*";
    }
}
patronAnidado2 += "<br><br>";
document.write(patronAnidado2);

// Patrón 3: X
let patronAnidado3 = "";

// Mitad superior
for (let i = 0; i < parseInt(m / 2); i++) {
    // Espacio a la izquierda de primera X
    for (let j = 0; j < i; j++) {
        patronAnidado3 += "&nbsp;&nbsp;";
    }
    // Primera X
    patronAnidado3 += "X";
    // Espacio entre las Xs
    for (let k = 0; k < m - (2 * i) - 2; k++) {
        patronAnidado3 += "&nbsp;&nbsp;";
    }
    // Segunda X
    patronAnidado3 += "X<br>";
}

// X Central en caso de m impar
if (m % 2 != 0) {
    for (let i = 0; i < parseInt(m / 2); i++) {
        patronAnidado3 += "&nbsp;&nbsp;";
    }
    patronAnidado3 += "&nbsp;X<br>";
}

// Mitad inferior
for (let i = parseInt(m / 2); i > 0; i--) {
    // Espacio a la izquierda de primera X
    for (let j = 1; j < i; j++) {
        patronAnidado3 += "&nbsp;&nbsp;";
    }
    // Primera X
    patronAnidado3 += "X";
    // Espacio entre las Xs
    for (let k = m - (2 * i); k > 0; k--) {
        patronAnidado3 += "&nbsp;&nbsp;";
    }
    // Segunda X
    patronAnidado3 += "X<br>";
}

patronAnidado3 += "<br><br>";
document.write(patronAnidado3);

// Patrón 4
let patronAnidado4 = "";

if (m > 1) {
    // Fila superior
    for (let i = 0; i < m - 1; i++) {
        patronAnidado4 += "*";
    }
    patronAnidado4 += "<br>";

    // Filas intermedias
    for (let j = 0; j < m - 2; j++) {
        // Espacios a la izquierda
        patronAnidado4 += "&nbsp;&nbsp;";
        // Asteriscos
        for (let k = 0; k < m - 2; k++) {
            patronAnidado4 += "*";
        }
        patronAnidado4 += "<br>";
    }

    // Fila inferior, comienza con un espacio
    patronAnidado4 += "&nbsp;&nbsp;";
    // Asteriscos
    for (let l = 0; l < m - 1; l++) {
        patronAnidado4 += "*";
    }
    patronAnidado4 += "<br>";
} else {  // Si n = 1
    patronAnidado4 += "*";
}

patronAnidado4 += "<br><br>";
document.write(patronAnidado4);