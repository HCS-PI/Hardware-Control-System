var database = require("../database/config");

// Colocar esta function na model da DashGestor

function cpuTemperaturaModel() {
    instrucaoSql = `select * from vwDashGesCPUTemp`
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}

// Não esquecer o export dessa model

module.exports = {
    mediaCpuCarrosModel,
    mediaRamCarrosModel,
    cpuTemperaturaModel
}