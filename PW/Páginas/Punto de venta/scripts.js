// Productos con categorías, precios e imágenes
const products = {
    dulces: [
        { name: "Gomitas", price: 10, img: "img/gomitas.jpg" },
        { name: "Paletas", price: 5, img: "img/paletas.jpg" },
        { name: "Chocolate", price: 20, img: "img/choco.jpg" },
        { name: "Mazapán", price: 8, img: "img/mazapan.jpg" },
        { name: "Chicles", price: 7, img: "img/chicles.jpg" },
        { name: "Tamarindo", price: 12, img: "img/tama.jpg" }
    ],
    bebidas: [
        { name: "Refresco (600ml)", price: 15, img: "img/refre.jpg" },
        { name: "Agua (1L)", price: 10, img: "img/agua.jpg" },
        { name: "Jugo de Naranja", price: 18, img: "img/naranja.jpg" },
        { name: "Leche (1L)", price: 25, img: "img/leche.jpg" },
        { name: "Café (vaso)", price: 30, img: "img/cafe.jpg" }
    ],
    botanas: [
        { name: "Papas Fritas", price: 18, img: "img/papas.jpg" },
        { name: "Cacahuates", price: 20, img: "img/caca.jpg" },
        { name: "Palomitas", price: 22, img: "img/palo.jpg" },
        { name: "Chicharrones", price: 19, img: "img/chicha.jpg" },
        { name: "Semillas", price: 15, img: "img/semi.jpg" }
    ]
};

let cart = [];

// Inicializa productos según la categoría seleccionada
function updateProducts() {
    const category = document.getElementById("category").value;
    const productSelect = document.getElementById("product");
    productSelect.innerHTML = "";

    products[category].forEach(p => {
        const option = document.createElement("option");
        option.value = p.name;
        option.text = p.name;
        productSelect.appendChild(option);
    });

    updateProductImage();
}

// Actualiza la imagen del producto seleccionado
function updateProductImage() {
    const category = document.getElementById("category").value;
    const productName = document.getElementById("product").value;
    const product = products[category].find(p => p.name === productName);
    // Usamos una imagen genérica por si algo falla
    document.getElementById("productImage").src = product ? product.img : "https://via.placeholder.com/150";
}

// Agregar producto al carrito
function addToCart() {
    const category = document.getElementById("category").value;
    const productName = document.getElementById("product").value;
    const quantity = parseInt(document.getElementById("quantity").value);
    const product = products[category].find(p => p.name === productName);

    if (!product || quantity < 1) return; // Validación de cantidad

    // Si el producto ya existe en el carrito, actualiza la cantidad
    const existing = cart.find(item => item.name === productName);
    if (existing) {
        existing.quantity += quantity;
    } else {
        cart.push({ ...product, quantity });
    }

    updateCart();
}

// Actualiza la tabla del carrito y el total
function updateCart() {
    const tbody = document.getElementById("cartTable").querySelector("tbody");
    tbody.innerHTML = "";
    let totalAmount = 0;

    cart.forEach(item => {
        const row = document.createElement("tr");
        const subtotal = item.price * item.quantity;
        totalAmount += subtotal;

        row.innerHTML = `
            <td>${item.name}</td>
            <td>${item.quantity}</td>
            <td>$${item.price.toFixed(2)}</td>
            <td>$${subtotal.toFixed(2)}</td>
        `;
        tbody.appendChild(row);
    });

    // Aseguramos que el total siempre muestre dos decimales
    document.getElementById("total").innerText = `Total: $${totalAmount.toFixed(2)}`;
}

// Vaciar carrito
function clearCart() {
    cart = [];
    updateCart();
}

// Eventos iniciales
document.getElementById("category").addEventListener("change", updateProducts);
document.getElementById("product").addEventListener("change", updateProductImage);

// Inicializa la página
updateProducts();