

function fazerInscricao(event){
    event.preventDefault()

    let name = document.getElementById("name").value
    let email = document.getElementById("email").value
    let telefone = document.getElementById("telefone").value
    let inscricao = document.getElementById("respostaInscricao")

    fetch("/inscricao", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ name, email, telefone})
    })
    .then(res => res.json())
    .then(data => {
        console.log("Resposta do servidor", data)

        document.getElementById("respostaInscricao").innerText = data

        if(data.mensagem === "Inscricao Feita com sucesso"){
            inscricao.style.color = "green"
            inscricao.style.fontSize = "20px"

            setTimeout(() => {
                window.location.href = "/minhasinscricoes"
            })
        }
        else{
            inscricao.innerText = "Erro no backend"
        }
    })
}

document.getElementById("btn_enviar").addEventListener("click", function(){
    let email = document.getElementById("email").value

    fetch("/enviar_email", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({email})
    })
    .then(res => res.json())
    .then(data => {
        console.log(data.mensagem || data.erro)
    })

    .catch(error => {
        console.error("Erro ao enviar email", error)
    })
})