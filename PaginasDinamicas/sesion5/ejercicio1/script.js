// Primero accedemos a los elementos que nos interesan utilizando el DOM.
let texto = document.getElementById("texto");  // elemento que queremos modificar.

let colorBox = document.getElementById("color-texto");  // select que controlará color de texto.
let bgBox = document.getElementById("color-fondo");  // select que controlará color de fondo.

// Ahora definimos un evento para cada select, ambos se ejecutarán cada vez que se cambie el valor del elemento (options)
colorBox.addEventListener("change", changeColor);
bgBox.addEventListener("change", changeBg);

// Cada evento lleva asociada una acción, las cuales definiremos dentro de funciones.
function changeColor() {
    texto.style.color = colorBox.value;
}

function changeBg() {
    texto.style.backgroundColor = bgBox.value;
}