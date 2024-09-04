/*
Crearemos un pequeño carrito de compras. Este carrito debe cumplir con lo siguiente:
→ Se debe poder revisar la lista de productos disponibles.
→ Se deben poder agregar productos al carrito.
→ Se debe poder consultar el carrito de compras y que se muestre además el total a pagar.
→ Se debe poder finalizar la compra y que no se vuelva a mostrar el menú principal (con las tres opciones anteriores).
*/

// Primero crearemos el texto del menú
let menu = "Seleccione una acción: \
            \n1. Ver productos disponibles\
            \n2. Agregar producto a mi carrito\
            \n3. Ver carrito de compras\
            \n4. Finalizar la compra";


// Crearemos la lista de productos y de precios
let productos = ["Camiseta", "Pantalones", "Zapatos", "Chaqueta", "Guantes"];
let precios = [20, 30, 40, 40, 10];

listaProductos = "";
for (let i = 0; i < productos.length; i++) {
    listaProductos += `${productos[i]} - $${precios[i]}\n`;
}

// Ahora declararemos e inicializaremos las variables necesarias.
let opcion = -1;
let carrito = [];
let total = 0;
let productoElegido = "";
let encontrado = false;
let textoCarrito = "";

// Agregaremos un mensaje de bienvenida
alert("¡Bienvenido a nuestra tienda!");

// Ahora vamos con el bucle que mostrará el menú hasta que se seleccione la 4ta opción
while (opcion != "4") {
    opcion = prompt(menu);

    switch (opcion) {
        case ("1"):
            alert(listaProductos);
            break;
        case ("2"):
            productoElegido = prompt("Escriba el nombre del producto que quiere agregar al carrito: ");

            // Debemos recorrer la lista de productos para buscar coincidencia con el escrito por el usuario.
            for (let j = 0; j < productos.length; j++) {
                if (productoElegido.toLowerCase() == productos[j].toLowerCase()) {
                    carrito.push(productos[j]);
                    total += precios[j];
                    encontrado = true;
                    break;
                }
            }

            // Si no se encuentra el producto en la lista...
            if (!encontrado) {
                alert("No hemos encontrado el producto que buscas. Inténtalo nuevamente.");
            }

            // Es importante volver a setear encontrado en false para no tener errores si se desea agregar más productos
            encontrado = false;
            break;
        case ("3"):
            // Primero borramos su contenido para evitar duplicaciones
            textoCarrito = "";
            textoCarrito += "---- Carrito ----\n";
            for (let k = 0; k < carrito.length; k++) {
                textoCarrito += carrito[k] + "\n";
            }
            textoCarrito += `Total: $${total}`;

            alert(textoCarrito);
            break;
        case ("4"):
            alert("Muchas gracias por tu visita");
            break;
    }
}