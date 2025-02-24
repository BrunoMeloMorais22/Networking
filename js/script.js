
document.getElementById("tema").addEventListener("click", function(){
    let body = document.body
    let botaoTema = document.getElementById("tema")

    body.classList.toggle("dark-mode")

    if(body.classList.contains("dark-mode")){
        botaoTema.textContent = "Claro"
    }
    else{
        botaoTema.textContent = "Escuro"
    }
})