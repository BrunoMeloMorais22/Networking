
function fazerCadastro(event){
    event.preventDefault()

    nomeCadastro = document.getElementById("nomeCadastro").value
    emailCadastro = document.getElementById("emailCadastro").value
    senhaCadastro = document.getElementById("senhaCadastro").value
    confirmarSenha = document.getElementById("confirmarSenha").value

    fetch("/cadastro", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: ({ nomeCadastro, emailCadastro, senhaCadastro, confirmarSenha })
    })
    .then(res => res.json())
    .then(data =>{
        console.log("Resposta do servidor", data)
        document.getElementById("feedbackCadastro").innerHTML = data.mensagem

        if(data.sucesso){
            document.getElementById("feedbackCadastro").style.color = "green"
        }
        else{
            document.getElementById("feedbackCadastro").style.color = "red"
        }
        console.log(data)
    })

    .catch(error =>{
        document.getElementById("feedbackCadastro").innerText = "Erro ao se conectar com o servidor"
        document.getElementById("feedbackCadastro").style.color = "red"
        console.error(error)
    })
}