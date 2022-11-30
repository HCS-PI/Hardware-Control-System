var tecnicoModel = require("../models/dashTecnicoModel");

function carrosMonitorados(req, res) {
    var idEmpresa = req.body.idEmpresa;
    console.log(`Recuperando a quantidade de carros monitorados`);

    tecnicoModel.carrosMonitorados(idEmpresa).then(function (resultado) {
        if (resultado.length > 0) {
            res.status(200).json(resultado);
        } else {
            res.status(204).send("Nenhum resultado encontrado!")
        }
    }).catch(function (erro) {
        console.log(erro);
        console.log("Houve um erro ao buscar os carros monitorados.", erro.sqlMessage);
        res.status(500).json(erro.sqlMessage);
    });
}

function buscarCarros(req, res) {
    var idEmpresa = req.body.idEmpresa;

    tecnicoModel.verCarrosProblema(idEmpresa).then(function (resultado) {
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

module.exports = {
    carrosMonitorados,
    buscarCarros
}