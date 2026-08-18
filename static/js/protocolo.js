function obterParametro(nome){

    const parametros = new URLSearchParams(window.location.search);

    return parametros.get(nome);

}

const protocolo = obterParametro("protocolo");

if(protocolo){

    document.getElementById("protocolo").textContent = protocolo;

}else{

    document.getElementById("protocolo").textContent = "Protocolo não encontrado";

}

function copiarProtocolo(){

    const codigo = document.getElementById("protocolo").textContent;

    navigator.clipboard.writeText(codigo);

    const toast = document.getElementById("toast");

    toast.classList.add("show");

    setTimeout(() => {

        toast.classList.remove("show");

    }, 2500);

}

const botao = document.getElementById("btnAcompanhar");

if(protocolo){

    botao.href =
        "{{ url_for('pages.acompanhar') }}" +
        "?protocolo=" +
        encodeURIComponent(protocolo);

}