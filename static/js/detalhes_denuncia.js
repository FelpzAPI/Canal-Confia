const parametros = new URLSearchParams(window.location.search);

const id = parametros.get("id");


// =============================
// CARREGAR OCORRÊNCIA
// =============================

async function carregarDenuncia(){

    if(!id){

        alert("Ocorrência não encontrada.");

        window.location.href = "/dashboard";

        return;

    }


    try{


        const resposta = await fetch(

            "/denuncias/" + id

        );


        const dados = await resposta.json();



        if(!resposta.ok){

            alert("Erro ao carregar ocorrência.");

            return;

        }



        document.getElementById("protocolo").value = dados.protocolo;


        document.getElementById("categoria").value = dados.categoria;


        document.getElementById("setor").value = dados.setor || "";


        document.getElementById("local").value = dados.local || "";


        document.getElementById("data_ocorrido").value = dados.data_ocorrido || "";


        document.getElementById("descricao").value = dados.descricao;


        document.getElementById("status").value = dados.status;


        document.getElementById("prioridade").value = dados.prioridade;



        // NOVO CAMPO
        document.getElementById("prazo_resposta").value = 
            dados.prazo_resposta || "Não definido";



        document.getElementById("observacao").value = 
            dados.observacao_rh || "";




        if(dados.anexo){


            document.getElementById("areaAnexo").innerHTML = `

                <div class="anexo-botao">

                    <a
                    href="/uploads/${dados.anexo}"
                    target="_blank"
                    class="btn principal">

                    Abrir Anexo

                    </a>

                </div>

            `;

        }


    }


    catch(erro){


        alert("Não foi possível conectar à API.");

        console.error(erro);


    }

}





// =============================
// SALVAR ALTERAÇÕES
// =============================

async function salvar(){


    const dados = {


        status: document
            .getElementById("status")
            .value,
            

        prioridade: document
        .getElementById("prioridade")
        .value,


        observacao_rh: document
            .getElementById("observacao")
            .value


    };



    try{


        const resposta = await fetch(


            "/denuncias/" + id,


            {


                method: "PUT",


                headers:{


                    "Content-Type":"application/json"


                },


                body: JSON.stringify(dados)


            }


        );



        const retorno = await resposta.json();




        if(resposta.ok){


            alert("Ocorrência atualizada com sucesso!");


            window.location.href = "/dashboard";


        }


        else{


            alert(

                retorno.erro ||

                "Erro ao atualizar ocorrência."

            );


        }



    }


    catch(erro){


        alert("Não foi possível conectar à API.");

        console.error(erro);


    }


}






// =============================
// LOGOUT
// =============================

function logout(){


    localStorage.clear();


    window.location.href = "/login";


}






// =============================
// EVENTOS
// =============================

document
    .getElementById("btnSalvar")
    .addEventListener(
        "click",
        salvar
    );





// =============================
// INICIALIZAÇÃO
// =============================

carregarDenuncia();