const tipoUsuario = localStorage.getItem("tipo");

if (tipoUsuario !== "gerente") {

    alert("Apenas o gerente pode acessar esta página.");

    window.location.href = "/dashboard";

}


// ======================================
// CARREGAR ADMINISTRADORES
// ======================================

async function carregarAdmins() {

    try {

        const resposta = await fetch("/api/admin");

        const admins = await resposta.json();

        const tabela = document.getElementById("tabelaAdmins");

        tabela.innerHTML = "";

        admins.forEach(admin => {

            let botaoExcluir = "";

            if (admin.tipo !== "gerente") {

                botaoExcluir = `

                    <button
                        class="btn secundario"
                        onclick="excluirAdmin(${admin.id})">

                        Excluir

                    </button>

                `;

            }

            tabela.innerHTML += `

                <tr>

                    <td>${admin.id}</td>

                    <td>${admin.nome}</td>

                    <td>${admin.email}</td>

                    <td>${admin.tipo}</td>

                    <td>

                        ${botaoExcluir}

                    </td>

                </tr>

            `;

        });

    }

    catch (erro) {

        alert("Erro ao carregar administradores.");

        console.error(erro);

    }

}


// ======================================
// CADASTRAR ADMINISTRADOR
// ======================================

async function cadastrarAdmin() {

    const nome = document.getElementById("nome").value.trim();

    const email = document.getElementById("email").value.trim();

    const senha = document.getElementById("senha").value;

    if (nome === "" || email === "" || senha === "") {

        alert("Preencha todos os campos.");

        return;

    }

    // ======================================
    // VALIDAÇÃO DA SENHA
    // ======================================

    const senhaForte =
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&.#_\-])[A-Za-z\d@$!%*?&.#_\-]{8,}$/;

    if (!senhaForte.test(senha)) {

        alert(
            "A senha deve conter:\n\n" +
            "• No mínimo 8 caracteres\n" +
            "• Pelo menos uma letra maiúscula\n" +
            "• Pelo menos uma letra minúscula\n" +
            "• Pelo menos um número\n" +
            "• Pelo menos um caractere especial"
        );

        return;

    }

    try {

        const resposta = await fetch("/api/admin", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({

                nome: nome,

                email: email,

                senha: senha,

                tipo: "administrador"

            })

        });

        const dados = await resposta.json();

        alert(dados.mensagem || dados.erro);

        if (resposta.ok) {

            document.getElementById("nome").value = "";

            document.getElementById("email").value = "";

            document.getElementById("senha").value = "";

            carregarAdmins();

        }

    }

    catch (erro) {

        alert("Erro ao conectar com a API.");

        console.error(erro);

    }

}


// ======================================
// EXCLUIR ADMINISTRADOR
// ======================================

async function excluirAdmin(id) {

    if (!confirm("Deseja realmente excluir este administrador?")) {

        return;

    }

    try {

        const resposta = await fetch("/api/admin/" + id, {

            method: "DELETE"

        });

        const dados = await resposta.json();

        alert(dados.mensagem || dados.erro);

        carregarAdmins();

    }

    catch (erro) {

        alert("Erro ao conectar com a API.");

        console.error(erro);

    }

}


// ======================================
// LOGOUT
// ======================================

function logout() {

    localStorage.clear();

    window.location.href = "/login";

}


// ======================================
// INICIALIZAÇÃO
// ======================================

carregarAdmins();