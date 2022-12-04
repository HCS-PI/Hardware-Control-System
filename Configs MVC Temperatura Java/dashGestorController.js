var mediaCarrosModel = require("../models/dashGestorModel");


// Inserir esta função no Controller da DashGestor

function cpuTemperaturaController(req,res) {
    
    var idEmpresa = req.body.idEmpresa;
    console.log(`Recuperando a última temperatura e uso de CPU inseridos`);

    mediaCarrosModel.cpuTemperaturaModel().then(function (resultado) {
        if (resultado.length > 0) {
            res.status(200).json(resultado);
        } else {
            res.status(204).send("Nenhum resultado encontrado!")
        }
    }).catch(function (erro) {
        console.log(erro);
        console.log("Houve um erro ao buscar última temperatura e uso de CPU inseridos.", erro.sqlMessage);
        res.status(500).json(erro.sqlMessage);
    });
}

// Não esquecer de colocar o export dela

module.exports = {
    mediaCpuCarrosController,
    mediaRamCarrosController,
    cpuTemperaturaController
}