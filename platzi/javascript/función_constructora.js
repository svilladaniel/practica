#!/usr/bin/node

function auto(marca, modelo, annio) {
    this.marca = marca;
    this.modelo = modelo;
    this.annio = annio;
}
let autoNuevo = new auto("Tesla", "Model 3", 2020);
console.log(autoNuevo);