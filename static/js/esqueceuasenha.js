document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("esqueceuSenha");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();

        const email = document.getElementById("email").value;

        if (!email) {
            document.getElementById("info").innerText = "Por favor, preencha o campo de email.";
            return;
        }

        try {
            const response = await fetch("/esqueci_senha", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ email })
            });

            const data = await response.json();
            document.getElementById("info").innerText = data.mensagem;
        } catch (error) {
            console.error("Erro ao enviar requisição:", error);
            document.getElementById("info").innerText = "Erro ao tentar enviar email. Tente novamente mais tarde.";
        }
    });
});
