var database = require("../database/config");

function carrosMonitorados(idEmpresa) {
    instrucaoSql = `
    SELECT fk_empresa, COUNT(id_carro) AS 'qtdCarro' FROM Carro WHERE fk_empresa = ${idEmpresa};`;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}
function verCarrosProblema(idEmpresa) {
    instrucaoSql = `
    SELECT * from vw_dashTec WHERE CodEmpresa = ${idEmpresa};`;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}


module.exports = {
    carrosMonitorados,
    verCarrosProblema
}