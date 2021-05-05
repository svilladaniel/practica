#!/usr/bin/node

let estudiantes = ["Maria", "Sergio", "Rosa", "Daniel"];

function saludarEstudiante(estudiante){
    console.log(`Hola, ${estudiante}`);
}

for(let i = 0; i < estudiantes.length; i++){
    saludarEstudiante(estudiantes[i]);
}

for(let estudiante of estudiantes)
{
    saludarEstudiante(estudiante);
}

while(estudiantes.length > 0){
    let estudiante = estudiantes.shift();
    saludarEstudiante(estudiante);
}