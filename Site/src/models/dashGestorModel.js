var database = require("../database/config");


function mediaCpuCarrosModel(idEmpresa) {
    instrucaoSql = `select * from vw_dashGES_CPU where CodEmpresa = ${idEmpresa}`
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}
function mediaRamCarrosModel(idEmpresa) {
    instrucaoSql = `select * from vw_dashGES_RAM where CodEmpresa = ${idEmpresa}`
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}



module.exports = {
    mediaCpuCarrosModel,
    mediaRamCarrosModel
}