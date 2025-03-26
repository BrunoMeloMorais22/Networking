
document.getElementById("inscricaoFormulario").addEventListener("submit", function(event){
    event.preventDefault()

    let name = document.getElementById("name").value
    let email = document.getElementById("email").value
    let phone = document.getElementById("phone").value
    let cpf = document.getElementById("cpd").value
    let info = document.getElementById("info")

    info.innerHTML = "" 

    if(name === "" || email === "" || phone === "" || cpf === ""){
        let p = document.createElement("p")
        p.textContent = "Prencha todos os espaços em branco"
        p.style.color = "red"
        p.style.fontWeight = "bold"
        document.getElementById("info").appendChild(p)
    }

    else{
        let p2 = document.createElement("p")
        let button = document.createElement("button")
        p2.textContent = "Inscrição enviada com sucesso."
        button.style.padding = "10px"
        button.textContent = "Voltar ao menu principal"
        button.style.background = "green"
        button.style.marginTop = "10px"
        button.style.fontSize = "18px"
        button.style.borderRadius = "20px"
        button.style.cursor = "pointer"
        button.style.border = "black"
        button.style.fontFamily = "Courier New', Courier, monospace;"
        p2.style.color = "green"
        p2.style.fontSize = "20px"
        p2.style.fontWeight = "bold"
        document.getElementById("info").appendChild(p2)
        document.getElementById("info").appendChild(button)

        button.onclick = () =>{
            window.location.href = "index2.html"
        }
    }
})