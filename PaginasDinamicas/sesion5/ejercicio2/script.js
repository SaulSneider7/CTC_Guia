let boton = document.getElementById("btn");

boton.addEventListener("click", validador);

function validador() {
    // Esto evita que se se mantengan mensajes de alguna validación anterior
    if (document.getElementById("mensaje")) {
        document.getElementById("mensaje").remove();
    }
    

    let nombres = document.getElementById("nombres");
    let apellidos = document.getElementById("apellidos");
    let usuario = document.getElementById("usuario");
    let fechaNacimiento = document.getElementById("nacimiento");
    let email = document.getElementById("email");
    let direccion = document.getElementById("direccion");
    let ciudad = document.getElementById("ciudad");
    let pais = document.getElementById("pais");
    let pass = document.getElementById("pass");

    let mensaje = document.createElement("p");
    mensaje.id = "mensaje";

    // Nombres: Este campo debe contener al menos 2 caracteres. Obligatorio.
    // método trim remueve espacios al inicio y final de un string.
    if (nombres.value.trim().length < 2) {
        mensaje.innerText = "Nombres inválidos.";
        nombres.parentNode.appendChild(mensaje);
        return false;
    }

    // Apellidos: Este campo debe contener al menos 3 caracteres. Obligatorio.
    if (apellidos.value.trim().length < 2) {
        mensaje.innerText = "Apellidos inválidos.";
        apellidos.parentNode.appendChild(mensaje);
        return false;
    }

    // Fecha de nacimiento: Obligatorio.
    valorFecha = new Date(fechaNacimiento.value);
    hoy = new Date();
    if (!valorFecha instanceof Date || isNaN(valorFecha)) {
        mensaje.innerText = "Campo obligatorio.";
        fechaNacimiento.parentNode.appendChild(mensaje);
        return false;
    } else if (valorFecha >= hoy) {
        mensaje.innerText = "Fecha no puede ser mayor a la actual.";
        fechaNacimiento.parentNode.appendChild(mensaje);
        return false;
    }

    // Usuario: Este campo debe contener al menos 5 caracteres, no se admiten espacios. Obligatorio.
    if (usuario.value.trim().length < 5 || usuario.value.trim().includes(" ")) {
        mensaje.innerText = "Usuario inválido.";
        usuario.parentNode.appendChild(mensaje);
        return false;
    }

    // Correo electrónico: Introduzca una dirección válida, que contenga los caracteres @ y un dominio. Obligatorio.
    if (email.value.trim().length < 6 || !email.value.trim().includes("@") || !email.value.trim().includes(".")) {
        mensaje.innerText = "Correo electrónico inválido.";
        email.parentNode.appendChild(mensaje); 
        return false;
    }

    // País: Obligatorio.
    if (pais.value.length < 1) {
        mensaje.innerText = "Seleccione un país de la lista.";
        pais.parentNode.appendChild(mensaje);
        return false;
    }

    // Contraseña: Escriba una contraseña de al menos 8 caracteres, incluyendo al menos una mayúscula, una minúscula y un número.
    let mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    let minusculas = mayusculas.toLowerCase().split("");
    mayusculas = mayusculas.split("");
    let numeros = "0123456789".split("");

    // Evaluamos mayúsculas
    let tieneMayusculas = false;
    for (let i = 0; i < mayusculas.length; i++) {
        if (pass.value.includes(mayusculas[i])) {
            tieneMayusculas = true;
            break;
        }
    }

    if (!tieneMayusculas) {
        mensaje.innerText = "Contraseña debe contener al menos 1 mayúscula.";
        pass.parentNode.appendChild(mensaje);
        return false;
    }

    // Evaluamos minúsculas
    let tieneMinusculas = false;
    for (let i = 0; i < minusculas.length; i++) {
        if (pass.value.includes(minusculas[i])) {
            tieneMinusculas = true;
            break;
        }
    }

    if (!tieneMinusculas) {
        mensaje.innerText = "Contraseña debe contener al menos 1 minúscula.";
        pass.parentNode.appendChild(mensaje);
        return false;
    }

    // Evaluamos números
    let tieneNumeros = false;
    for (let i = 0; i < numeros.length; i++) {
        if (pass.value.includes(numeros[i])) {
            tieneNumeros = true;
            break;
        }
    }

    if (!tieneNumeros) {
        mensaje.innerText = "Contraseña debe contener al menos 1 número.";
        pass.parentNode.appendChild(mensaje);
        return false;
    }

    // Si todo es correcto...
    alert("Formulario enviado exitosamente.");
}