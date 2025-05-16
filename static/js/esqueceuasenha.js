

document.getElementById("esqueceuSenha").addEventListener("submit", function(event){
    event.preventDefault()

    let email = document.getElementById("email").value

    if(email === ""){
        alert("Por favor, insira um email")
        return
    }

    else{
        let p = document.createElement("p")
        p.textContent = `Um email de instruções foi enviado para o seguinte email ${email}`
        p.style.color = "green"
        p.style.fontWeight = "bold"
        document.getElementById("info").appendChild(p)
    }
})