let denuncias = [];

let filtroCard = "";


// =========================
// Carrega Dashboard
// =========================

async function carregarDashboard() {

    try {


        const respostaDashboard = await fetch(
            "/api/dashboard"
        );


        const dashboard = await respostaDashboard.json();



        document.getElementById("total").textContent =
            dashboard.total;



        document.getElementById("recebidas").textContent =
            dashboard.recebidas;



        document.getElementById("analise").textContent =
            dashboard.analise;



        document.getElementById("concluidas").textContent =
            dashboard.concluidas;





        const respostaLista = await fetch(
            "/denuncias"
        );


        denuncias = await respostaLista.json();



        atualizarTabela();


    }


    catch (erro) {


        alert("Não foi possível conectar à API.");


        console.error(erro);


    }


}





// =========================
// Filtro pelos Cards (KPIs)
// =========================

function filtrarPorCard(status){


    filtroCard = status;



    document
    .querySelectorAll(".dash-card")
    .forEach(card => {

        card.classList.remove("ativo");

    });




    const cardSelecionado = document.querySelector(
        `.dash-card[data-status="${status}"]`
    );



    if(cardSelecionado){

        cardSelecionado.classList.add("ativo");

    }



    atualizarTabela();


}







// =========================
// Atualiza tabela
// =========================

function atualizarTabela(){



    const tabela = document.getElementById(
        "tabelaDenuncias"
    );



    tabela.innerHTML = "";





    const pesquisa = document
        .getElementById("pesquisa")
        .value
        .toLowerCase();





    const categoria = document
        .getElementById("filtroCategoria")
        .value;





    const prioridade = document
        .getElementById("filtroPrioridade")
        .value;







    const lista = denuncias.filter(d => {



        const protocoloOK =
            d.protocolo
            .toLowerCase()
            .includes(pesquisa);




        const categoriaOK =
            categoria === "" ||
            d.categoria === categoria;





        const prioridadeOK =
            prioridade === "" ||
            d.prioridade === prioridade;





        const statusOK =
            filtroCard === "" ||
            d.status === filtroCard;





        return protocoloOK &&
               categoriaOK &&
               prioridadeOK &&
               statusOK;



    });







    if(lista.length === 0){



        tabela.innerHTML = `

        <tr>

            <td colspan="5">

                Nenhuma ocorrência encontrada.

            </td>

        </tr>

        `;



        return;


    }







    lista.forEach(d => {



        let classe = "";



        switch(d.status){


            case "Recebida":

                classe = "recebida";

                break;



            case "Em análise":

                classe = "analise";

                break;



            case "Concluída":

                classe = "concluida";

                break;



        }






        tabela.innerHTML += `


        <tr>


            <td>
                ${d.protocolo}
            </td>



            <td>
                ${d.categoria}
            </td>



            <td>

                <span class="status ${classe}">

                    ${d.status}

                </span>

            </td>



            <td>
                ${d.data_criacao}
            </td>



            <td>

                <a
                href="/detalhes_denuncia?id=${d.id}"
                class="btn principal">

                    Visualizar

                </a>

            </td>



        </tr>


        `;



    });



}







// =========================
// Eventos
// =========================


document
.getElementById("pesquisa")
.addEventListener(
    "input",
    atualizarTabela
);




document
.getElementById("filtroCategoria")
.addEventListener(
    "change",
    atualizarTabela
);




document
.getElementById("filtroPrioridade")
.addEventListener(
    "change",
    atualizarTabela
);









// =========================
// Login
// =========================


const usuario = localStorage.getItem("usuario");

const tipo = localStorage.getItem("tipo");




if(!usuario){

    window.location.href = "/login";

}




if(tipo === "gerente"){



    document.getElementById(
        "btnAdministradores"
    ).style.display = "inline-block";



    document.getElementById(
        "areaGerente"
    ).style.display = "block";



}







// =========================
// Logout
// =========================

function logout(){


    localStorage.clear();


    window.location.href="/login";


}








// =========================
// Inicialização
// =========================


carregarDashboard();




setInterval(
    carregarDashboard,
    30000
);