
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

function toggleMenu() {
    
    var sidebar = document.getElementById("sidebar");
    if (sidebar.style.right === "0px") {
        sidebar.style.right = "-292px";
    } else {
        sidebar.style.right = "0px";
    }
}


document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.getElementById("menu-icon");
    const sidebar = document.getElementById("sidebar");
    const closeBtn = document.getElementById("close-btn");

    menuIcon.addEventListener("click", function () {
        sidebar.classList.add("active");
    });

    closeBtn.addEventListener("click", function () {
        sidebar.classList.remove("active");
    });
});



