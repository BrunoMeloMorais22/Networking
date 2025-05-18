
function fazerLogin(event){
    event.preventDefault()

    emailLogin = document.getElementById("emailLogin").value
    senhaLogin = document.getElementById("senhaLogin").value

    fetch("/login", {
        method: "POST",
        headers: {"Content-type": "application/json"},
        body: JSON.stringify({ emailLogin, senhaLogin }),
        credentials: "include"
    })
    .then(res => res.json())
    .then(data =>{
        console.log("Resposta do servidor", data)

        document.getElementById("feedbackLogin").innerText = data.mensagem

        if(data.mensagem === "Login feito com sucesso"){
            document.getElementById("feedbackLogin").style.color = "green"

            setTimeout(() => {
                window.location.href = "/index2"
            }, 2000);
        }
    })

    .catch(error =>{
        document.getElementById("feedbackLogin").innerText = "Erro ao se conectar com o servidor"
        document.getElementById("feedbackLogin").style.color = "red"
    })
}