#!/usr/bin/node
let articulos = [{ nombre: "bici", costo: 3000 },
{ nombre: "Tv", costo: 2500 },
{ nombre: "Libro", costo: 320 },
{ nombre: "Celular", costo: 10000 },
{ nombre: "Laptop", costo: 20000 },
{ nombre: "Teclado", costo: 500 },
{ nombre: "Audifonos", costo: 1700 },
];

let articulosfiltrados = articulos.filter(function(articulo){
    return articulo.costo <= 500
});
console.log(articulosfiltrados);

let nombreArticulos = articulos.map(function(articulo){
    return articulo.nombre
});
console.log(nombreArticulos);

let encuentraArtículo = articulos.find(function(articulo) {
    return articulo.nombre === "Laptop"
});
console.log(encuentraArtículo);

articulos.forEach(function(articulo) {
    console.log(articulo.nombre);
});

let articulosBaratos = articulos.some(function(articulo){
    return articulo.costo <= 700;
})
console.log(articulosBaratos);