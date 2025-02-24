

document.getElementById("formLogin").addEventListener("submit", function(event){
    event.preventDefault()

    let emailLogin = document.getElementById("emailLogin").value
    let senhaLogin = document.getElementById("senhaLogin").value
    let feedbackLogin = document.getElementById("feedbackLogin")

    const emailSalvo = localStorage.getItem("email")
    const senhaSalva = localStorage.getItem("senha")

    if(emailLogin === emailSalvo && senhaLogin === senhaSalva){
        feedbackLogin.style.color = "green"
        feedbackLogin.style.fontWeight = "bold"
        feedbackLogin.textContent = "Login bem-sucedido. Voltando..."
            
        setTimeout(() => {
            window.location.href = "index2.html"
        }, 2000);
    }

    else{
        feedbackLogin.style.color = "red"
        feedbackLogin.style.fontWeight = "bold"
        feedbackLogin.textContent = "Email ou Senha inválidos"
    }
})