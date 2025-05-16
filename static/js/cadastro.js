
document.getElementById("formCadastro").addEventListener("submit", function(event){
    event.preventDefault()

    let nomeCadastro = document.getElementById("nomeCadastro").value
    let emailCadastro = document.getElementById("emailCadastro").value
    let senhaCadastro = document.getElementById("senhaCadastro").value
    let confirmarSenha = document.getElementById("confirmarSenha").value
    let feedbackCadastro = document.getElementById("feedbackCadastro")

    const regex = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;

    if(confirmarSenha !== senhaCadastro){
        feedbackCadastro.style.color = "red"
        feedbackCadastro.textContent = "As senhas não combinam"
        feedbackCadastro.style.fontWeight = "bold"
        return
    }

    if(regex.test(senhaCadastro)){
        localStorage.setItem("email", emailCadastro)
        localStorage.setItem("senha", senhaCadastro)

        feedbackCadastro.style.color = "green"
        feedbackCadastro.textContent = "Cadastrado com sucesso. Faça Login"
        feedbackCadastro.style.fontWeight = "bold"
    }

    else{
        feedbackCadastro.style.color = "red"
        feedbackCadastro.textContent = "A senha precisa conter 8 caracteres, 1 letra maiúscula, 1 caractere especia e 1 número"
        feedbackCadastro.style.fontWeight =  "bold"
    }
})