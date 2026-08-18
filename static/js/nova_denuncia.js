const form = document.getElementById("formDenuncia");
const botao = document.getElementById("btnEnviar");

const mapaPrioridades = {

    "Assédio Moral": "Alta",

    "Assédio Sexual": "Alta",

    "Discriminação ou Preconceito": "Alta",

    "Conflito entre Colaboradores": "Média",

    "Problemas de Conduta": "Média",

    "Irregularidade ou Descumprimento de Normas": "Média",

    "Segurança ou Condições de Trabalho": "Média",

    "Sugestão de Melhoria": "Baixa",

    "Reclamação Geral": "Baixa",

    "Outro": "Baixa"

};


document.getElementById("categoria").addEventListener("change", function(){

    const prioridade =
        mapaPrioridades[this.value] || "";

    document.getElementById("prioridade").value = prioridade;

});

form.addEventListener("submit", async function(e){

    e.preventDefault();


    botao.disabled = true;
    botao.textContent = "Enviando...";


    const formData = new FormData();


    formData.append(
        "categoria",
        document.getElementById("categoria").value
    );

    formData.append(
    "prioridade",
    mapaPrioridades[
        document.getElementById("categoria").value
    ]
    );


    formData.append(
        "setor",
        document.getElementById("setor").value
    );


    formData.append(
        "local",
        document.getElementById("local").value
    );


    formData.append(
        "data_ocorrido",
        document.getElementById("data_ocorrido").value
    );


    formData.append(
        "descricao",
        document.getElementById("descricao").value
    );



    const arquivo = document.getElementById("anexo").files[0];


    if(arquivo){

        formData.append(
            "anexo",
            arquivo
        );

    }



    try{


        const resposta = await fetch(
            "/denuncias",
            {
                method:"POST",
                body:formData
            }
        );



        const dados = await resposta.json();



        if(resposta.ok){


            window.location.href =
                "/acompanhar?protocolo=" +
                encodeURIComponent(
                    dados.protocolo
                );


        }else{


            alert(
                dados.erro ||
                "Erro ao enviar ocorrência."
            );


            botao.disabled = false;

            botao.textContent =
                "Enviar ocorrência";


        }


    }catch(erro){


        console.error(erro);


        alert(
            "Não foi possível conectar à API."
        );


        botao.disabled = false;


        botao.textContent =
            "Enviar ocorrência";


    }


});