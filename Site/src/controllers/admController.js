var admModel = require("../models/admModel");

function buscarFuncionarios(req, res) {
    var idEmpresa = req.body.idEmpresa;

    admModel.buscarFuncionarios(idEmpresa).then(function (resultado) {
        if (resultado.length > 0) {
            res.status(200).json(resultado);
        } else {
            res.status(204).send("Nenhum resultado encontrado!")
        }
    }).catch(function (erro) {
        console.log(erro);
        console.log("Houve um erro ao buscar as ultimas medidas.", erro.sqlMessage);
        res.status(500).json(erro.sqlMessage);
    });
}

function deletarFuncionarios(req, res) {
    console.log('Cheguei no controller')
    var idFuncionario = req.body.idFuncionario;

    admModel.deletarFuncionarios(idFuncionario).then(function (resultado) {
        if (resultado.length > 0) {
            res.status(200).json(resultado);
            console.log(`${idFuncionario}`)
        } else {
            res.status(204).send("Nenhum resultado encontrado!")
            console.log(`${idFuncionario}`)
        }
    }).catch(function (erro) {
        console.log(erro);
        console.log("Houve um erro ao buscar as ultimas medidas.", erro.sqlMessage);
        console.log(idFuncionario)
        res.status(500).json(erro.sqlMessage);

    });
}

function listarFuncionario(req, res) {
    admModel.listar()
        .then(function (resultado) {
            if (resultado.length > 0) {
                res.status(200).json(resultado);
            } else {
                res.status(204).send("Nenhum resultado encontrado!")
            }
        }).catch(
            function (erro) {
                console.log(erro);
                console.log("Houve um erro ao realizar a consulta! Erro: ", erro.sqlMessage);
                res.status(500).json(erro.sqlMessage);
            }
        );
}

function cadastrarFuncionarios(req, res) {
    var nomeFuncionario = req.body.nomeFuncionario;
    var email = req.body.emailFuncionario;
    var senha = req.body.senhaFuncionario;
    var idEmpresa = req.body.idEmpresa;
    var cpf = req.body.cpf;
    var cargo = req.body.cargo;

    // Faça as validações dos valores
    if (nomeFuncionario == undefined) {
        res.status(400).send("O nome da empresa está undefined!");
    } else if (email == undefined) {
        res.status(400).send("Seu email está undefined!");
    } else if (senha == undefined) {
        res.status(400).send("Sua senha está undefined!");
    }else if (cargo == undefined) {
        res.status(400).send("Sua senha está undefined!");
    } else if (cpf == undefined) {
        res.status(400).send("Sua senha está undefined!");
    } else {
        admModel.cadastrar(idEmpresa, cpf, nomeFuncionario, email, senha, cargo)
            .then(
                function (resultado) {
                    res.json(resultado);
                }
            ).catch(
                function (erro) {
                    console.log(erro);
                    console.log(
                        "\nHouve um erro ao realizar o cadastro! Erro: ",
                        erro.sqlMessage
                    );
                    res.status(500).json(erro.sqlMessage);
                }
            );
    }
}

module.exports = {
    listarFuncionario,
    buscarFuncionarios,
    deletarFuncionarios,
    cadastrarFuncionarios
}