let count = 1;

while (count <= 5) {
    console.log("Número:", count);
    count++;
}
// Imprime: Número: 1, Número: 2, ..., Número: 5

for (let i = 0; i < 5; i++) {
    console.log(`Iteración ${i + 1}`);
}
// Imprime: Iteración 1, Iteración 2, ..., Iteración 5

let age = 18;

if (age >= 18) {
    console.log("Eres mayor de edad.");
} else {
    console.log("Eres menor de edad.");
}
// Imprime: Eres mayor de edad.

let fruit = "manzana";

switch (fruit) {
    case "manzana":
        console.log("Es una manzana.");
        break;
    case "plátano":
        console.log("Es un plátano.");
        break;
    case "naranja":
        console.log("Es una naranja.");
        break;
    default:
        console.log("Fruta desconocida.");
}
// Imprime: Es una manzana.

// Datos de inicio de sesión predefinidos
const correctUsername = "usuario123";
const correctPassword = "contraseña123";

// Solicita al usuario que ingrese su nombre de usuario
const username = prompt("Ingrese su nombre de usuario:");

// Solicita al usuario que ingrese su contraseña
const password = prompt("Ingrese su contraseña:");

// Verifica si las credenciales son correctas
if (username === correctUsername && password === correctPassword) {
    alert("Inicio de sesión exitoso. ¡Bienvenido!");
} else {
    alert("Credenciales incorrectas. Por favor, intente de nuevo.");
}



/*
// Datos correctos para iniciar sesión
const correctUsername = "admin";
const correctPassword = "1234";

// Solicitar usuario y contraseña al usuario
const username = prompt("Ingrese su nombre de usuario:");
const password = prompt("Ingrese su contraseña:");

// Variable para el estado del inicio de sesión
let loginStatus;

if (username === correctUsername && password === correctPassword) {
    loginStatus = "success";
} else if (username !== correctUsername && password === correctPassword) {
    loginStatus = "usernameError";
} else if (username === correctUsername && password !== correctPassword) {
    loginStatus = "passwordError";
} else if (username === "") {
    loginStatus = "emptyUsername";
} else if (password === "") {
    loginStatus = "emptyPassword";
} else {
    loginStatus = "bothError";
}

// Evaluar el estado con switch
switch (loginStatus) {
    case "success":
        alert("Inicio de sesión exitoso. ¡Bienvenido!");
        break;
    case "usernameError":
        alert("Error: Nombre de usuario incorrecto.");
        break;
    case "passwordError":
        alert("Error: Contraseña incorrecta.");
        break;
    case "emptyUsername":
        alert("Error: El campo de nombre de usuario está vacío.");
        break;
    case "emptyPassword":
        alert("Error: El campo de contraseña está vacío.");
        break;
    case "bothError":
        alert("Error: Ambos campos son incorrectos.");
        break;
    default:
        alert("Ocurrió un error inesperado.");
}

*/