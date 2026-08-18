const form = document.getElementById("loginForm");

form.addEventListener("submit", async function(e){

    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const senha = document.getElementById("senha").value;

    const erro = document.getElementById("erro");
    erro.textContent = "";

    try{

        const resposta = await fetch("/login",{

            method:"POST",

            headers:{
                "Content-Type":"application/json"
            },

            body:JSON.stringify({

                email:email,
                senha:senha

            })

        });

        const dados = await resposta.json();

        if(resposta.ok && dados.sucesso){

            localStorage.setItem("id", dados.id);
            localStorage.setItem("usuario", dados.usuario);
            localStorage.setItem("email", dados.email);
            localStorage.setItem("tipo", dados.tipo);

            window.location.href = "/dashboard";

        }

        else{

            erro.textContent =
                dados.mensagem || "E-mail ou senha inválidos.";

        }

    }

    catch(error){

        console.error(error);

        erro.textContent =
            "Não foi possível conectar à API.";

    }

});