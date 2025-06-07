

let codigo = document.getElementById("codigo")
let codigoFinal = ""

for(let i = 0; i < 4; i++){
    let numeroAleatorio = Math.floor(Math.random() * 10)
    codigoFinal += numeroAleatorio
}

codigo.textContent = codigoFinal;

codigo.style.color = "yellow"
codigo.style.fontSize = "18px"
codigo.style.background = "black"
codigo.style.padding = "3px"

