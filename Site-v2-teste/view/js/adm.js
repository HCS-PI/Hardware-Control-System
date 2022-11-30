var idFunc = 0;
var nome = '';
var idEmpresa = sessionStorage.ID_EMPRESA;
var email = '';

fetch("/adm/pegarFunc", {
    method: 'POST',
    headers: {
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        idEmpresa: idEmpresa
    })
}).then(function (resposta) {
    if (resposta.ok) {

        resposta.json().then(json => {
            for (var index = 0; index < json.length; index++) {
                idFuncionario = json[index].id_funcionario
                nome = json[index].nome_funcionario;
                email = json[index].email; cargo = json[index].cargo;
                cpf = json[index].cpf;


                if (cargo == "GES") {
                    cad_ApresentarGes.innerHTML += `<div class="box_func">
                                                   <span>${nome}</span> <b>|</b><span>${cpf}</span>  <b>|</b><span>${email}</span><b>|</b>   <button onclick="excluirFunc(${idFuncionario})" class="btExcluir">Excluir</button>
                                                </div>`
                } else if (cargo == "TEC") {
                    cad_ApresentarTec.innerHTML += `<div class="box_func">
                    <span>${nome}</span> <b>|</b><span>${cpf}</span>  <b>|</b><span>${email}</span><b>|</b>   <button onclick="excluirFunc(${idFuncionario})" class="btExcluir">Excluir</button>
                 </div>`
                }

            }
        })

    }
})

function excluirFunc(idFuncionario) {
    fetch("/adm/deleteFunc", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            idFuncionario: idFuncionario
        })
    }).then(function (resposta) {
        if (resposta.ok) {
            document.location.reload(true)
        }
    })
}


function cadastrar() {
    var nome = ipt_nome.value;
    var email = ipt_email.value;
    var senha = ipt_senha.value;
    var cpf = ipt_cpf.value;
    var idEmpresaVar = sessionStorage.ID_EMPRESA;


    if (ipt_cargo.value == 1) {
        var cargo = "GES"
    } else if (ipt_cargo.value == 2) {
        var cargo = "TEC"
    } else {
        alert("Entre com um cargo")
        return false;
    }

    console.log("resposta: ", idEmpresaVar, nome, email, senha, cpf, cargo);

    //Adicionar verificações
    if (nome == "" || email == "" || senha == "" || cpf == "") {
        alert("Preencha todos os campos para prosseguir!");
        return false;
    }

    if (email.indexOf("@") == -1 || email.indexOf(".com") == -1) {

        alert("Ops, e-mail inválido! Verifique e tente novamente.");

        return false;
    }
    if (senha.length < 8) {
        alert("Senha não preenche os requisitos de segurança: Tenha pelo menos algum 8 caracteres")
        return false;
    }
    if(cpf.length != 14){
        alert("Entre com um CPF valido!");
        return false;
    }

    // Enviando o valor da nova input
    fetch("/adm/cadastro", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            // crie um atributo que recebe o valor recuperado aqui
            // Agora vá para o arquivo routes/usuario.js
            nomeFuncionario: nome,
            idEmpresa: idEmpresaVar,
            cpf: cpf,
            emailFuncionario: email,
            senhaFuncionario: senha,
            cargo: cargo

        })
    }).then(function (resposta) {

        console.log("resposta: ", resposta);

        if (resposta.ok) {
            alert("cadastro realizado com sucesso!")
            window.location = "/dashADM.html";
        } else {
            throw ("Houve um erro ao tentar realizar o cadastro!");
        }
    }).catch(function (resposta) {
        console.log(`#ERRO: ${resposta}`);

    });

    return false;
}

var visivel = true;
function trocar() {
    if (visivel) {
        btCadastro.style = "display: none";
        btVer.style = "display: block;";
        divCadApresentar1.style = "display: none;"
        divCadApresentar2.style = "display: none;"
        divCard.style = "display: block;"
        visivel = false;
    } else {
        btCadastro.style = "display: block";
        btVer.style = "display: none;";
        divCard.style = "display: none;";
        divCadApresentar1.style = "display: block;"
        divCadApresentar2.style = "display: block;"
        visivel = true;
    }
}