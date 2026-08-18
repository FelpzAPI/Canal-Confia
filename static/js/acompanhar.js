const parametros = new URLSearchParams(window.location.search);

const protocoloURL = parametros.get("protocolo");


if(protocoloURL){

    document.getElementById("protocoloInput").value = protocoloURL;

    consultar();

}



async function consultar(){

    const protocolo = document
        .getElementById("protocoloInput")
        .value
        .trim();


    if(protocolo === ""){

        alert("Informe o protocolo.");

        return;

    }



    try{


        const resposta = await fetch(

            "http://127.0.0.1:5000/protocolo/" + 
            encodeURIComponent(protocolo)

        );



        const dados = await resposta.json();



        if(!resposta.ok){

            alert(dados.erro || "Protocolo não encontrado.");

            return;

        }



        document.getElementById("resultado").style.display = "block";



        document.getElementById("codigo").textContent =
            dados.protocolo;



        document.getElementById("categoria").textContent =
            dados.categoria;



        document.getElementById("status").textContent =
            dados.status;



        document.getElementById("prioridade").textContent =
            dados.prioridade;



        // PRAZO DE RESPOSTA INICIAL

        document.getElementById("prazo").textContent =
            dados.prazo_resposta || "Não definido";



        document.getElementById("data").textContent =
            dados.ultima_atualizacao;



        document.getElementById("observacao").textContent =
            dados.observacao_rh || 
            "Ainda não há observações do RH.";




        let mensagem = "";



        switch(dados.status){


            case "Recebida":

                mensagem =
                    "Sua ocorrência foi recebida e será analisada pelo RH.";

                break;



            case "Em análise":

                mensagem =
                    "Sua ocorrência está sendo analisada pelo RH.";

                break;



            case "Concluída":

                mensagem =
                    "A análise da ocorrência foi concluída.";

                break;



            case "Resolvida":

                mensagem =
                    "Esta ocorrência foi concluída. O prazo de resposta inicial definido era de "
                    + dados.prazo_resposta + ".";

                break;



            default:

                mensagem =
                    "Status atualizado.";

        }



        document.getElementById("mensagem").textContent =
            mensagem;



    }



    catch(erro){


        console.error(erro);


        alert("Não foi possível conectar à API.");


    }


}