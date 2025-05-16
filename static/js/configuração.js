


const darkMode = document.getElementById("dark-mode")
const body = document.body


darkMode.addEventListener('change', () =>{
    if(darkMode.checked){
        body.classList.remove('light-mode')
        body.classList.add('dark-mode')
    }

    else{
        body.classList.remove('dark-mode')
        body.classList.add('light-mode')
    }
})

document.getElementById("salvar").addEventListener("click", function(){
    alert("Suas alteraçoes foram salvas com sucesso")
    return
})

document.getElementById("voltar").addEventListener("click", function(){
    window.location.href = "index2.html"
})

