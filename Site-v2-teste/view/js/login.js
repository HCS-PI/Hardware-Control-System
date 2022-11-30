function entrar() {
    // aguardar();

    var emailVar = ipt_email.value;
    var senhaVar = ipt_senha.value;

    // TODO: VERIFICAR AS VALIDAÇÕES QUE ELES ESTÃO APRENDENDO EM ALGORITMOS 
    if (emailVar == "" || senhaVar == "") {
      
        alert('Preencha todos os campos para prosseguir!');
        // finalizarAguardar();
        return false;
    } 
    // else {
    //     setInterval(sumirMensagem, 5000)
    // }

    if (emailVar.indexOf("@") == -1 || emailVar.startsWith("@") == true || emailVar.endsWith("@") == true || (emailVar.endsWith(".com") == false && emailVar.endsWith(".school") == false && emailVar.endsWith(".com.br") == false)) {
        
        alert('Ops, e-mail inválido! Verifique e tente novamente.')
        // finalizarAguardar();
        return false;
    } 

    console.log("FORM LOGIN: ", emailVar);
    console.log("FORM SENHA: ", senhaVar);

    fetch("/usuarios/autenticar", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            emailServer: emailVar,
            senhaServer: senhaVar
        })
    }).then(function (resposta) {
        console.log("ESTOU NO THEN DO entrar()!")

        if (resposta.ok) {
            console.log(resposta);

            resposta.json().then(json => {
                console.log(json);
                console.log(JSON.stringify(json));

                sessionStorage.EMAIL_USUARIO = json.email;
                sessionStorage.NOME_USUARIO = json.nome;
                sessionStorage.ID_EMPRESA = json.fk_empresa;
                sessionStorage.CARGO = json.cargo;


                setTimeout(function () {
                    if (json.cargo == "ADM") {
                        window.location = "/dashADM.html";
                    }
                    else if (json.cargo == "GES") {
                        window.location = "/dashGES.html";
                    }
                    else if (json.cargo == "TEC") {
                        window.location = "/dashTEC.html";
                    }
                }, 500); // apenas para exibir o loading

            });

        } else {

            alert ('Ops, a conta não foi encontrada ! Verifiueye seu Email e Senha');

            resposta.text().then(texto => {
                console.error(texto);
                finalizarAguardar(texto);
            });
        }

    }).catch(function (erro) {
        console.log(erro);
    })

    return false;
}