var database = require("../database/config");


function mediaCpuCarrosModel(idEmpresa) {
    instrucaoSql = `select * from vwDashGesCPU where CodEmpresa = ${idEmpresa} order by MediaConsumo DESC`
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}
function mediaRamCarrosModel(idEmpresa) {
    instrucaoSql = `select * from vwDashGesRAM where CodEmpresa = ${idEmpresa} order by MediaConsumo DESC`
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}
function cpuTemperaturaModel() {
    instrucaoSql = `select * from vwDashGesCPUTemp`
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}


module.exports = {
    mediaCpuCarrosModel,
    mediaRamCarrosModel,
    cpuTemperaturaModel
}