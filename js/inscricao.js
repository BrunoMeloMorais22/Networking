
document.getElementById("inscricaoFormulario").addEventListener("submit", function(event){
    event.preventDefault()

    let name = document.getElementById("name").value
    let email = document.getElementById("email").value
    let phone = document.getElementById("phone").value

    if(name === "" || email === "" || phone === ""){
        let p = document.createElement("p")
        p.textContent = "Inscrição enviada com sucesso"
        p.style.color = "green"
        p.style.fontWeight = "bold"
        document.getElementById("info").appendChild(p)
    }

    else{
        let p2 = document.createElement("p")
        p2.textContent = "Inscrição enviada com sucesso."
        p2.style.color = "green"
        p2.style.fontSize = "20px"
        p2.style.fontWeight = "bold"
        document.getElementById("info").appendChild(p2)
    }
})