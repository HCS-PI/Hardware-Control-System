var mediaCarrosModel = require("../models/dashGestorModel");

function mediaCpuCarrosController(req, res) {

    var idEmpresa = req.body.idEmpresa;
    console.log(`Recuperando as médias de CPU por Modelo de Carro`);

    mediaCarrosModel.mediaCpuCarrosModel(idEmpresa).then(function (resultado) {
        if (resultado.length > 0) {
            res.status(200).json(resultado);
        } else {
            res.status(204).send("Nenhum resultado encontrado!")
        }
    }).catch(function (erro) {
        console.log(erro);
        console.log("Houve um erro ao buscar as médias de Consumo de CPU por modelo de carro.", erro.sqlMessage);
        res.status(500).json(erro.sqlMessage);
    });
}
function mediaRamCarrosController(req, res) {

    var idEmpresa = req.body.idEmpresa;
    console.log(`Recuperando as médias de CPU por Modelo de Carro`);

    mediaCarrosModel.mediaRamCarrosModel(idEmpresa).then(function (resultado) {
        if (resultado.length > 0) {
            res.status(200).json(resultado);
        } else {
            res.status(204).send("Nenhum resultado encontrado!")
        }
    }).catch(function (erro) {
        console.log(erro);
        console.log("Houve um erro ao buscar as médias de Consumo de CPU por modelo de carro.", erro.sqlMessage);
        res.status(500).json(erro.sqlMessage);
    });
}

module.exports = {
    mediaCpuCarrosController,
    mediaRamCarrosController,
}