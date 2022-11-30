var database = require("../database/config");

function buscarFuncionarios(idEmpresa) {
    instrucaoSql = `select * from Funcionario where fk_empresa = ${idEmpresa}`;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}
function deletarFuncionarios(idFuncionario) {
    console.log(idFuncionario);
    instrucaoSql = `delete from Funcionario where id_funcionario = ${idFuncionario}`;
    console.log("Executando a instrução SQL: \n" + instrucaoSql);
    return database.executar(instrucaoSql);
}

function cadastrar(idEmpresa, cpf, nomeFuncionario, email, senha, cargo) {
    console.log("ACESSEI O USUARIO MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function cadastrarUser():", idEmpresa, cpf, nomeFuncionario, email, senha, cargo);

    // Insira exatamente a query do banco aqui, lembrando da nomenclatura exata nos valores
    //  e na ordem de inserção dos dados.
    var instrucao = `
    INSERT INTO Funcionario (nome_funcionario, cpf, email,senha,cargo,fk_empresa)
     VALUES ('${nomeFuncionario}','${cpf}','${email}', '${senha}','${cargo}' ,${idEmpresa});
    `;
    console.log("Executando a instrução SQL: \n" + instrucao);
    return database.executar(instrucao);
}

function listar() {
    console.log("ACESSEI O Funcionario MODEL \n \n\t\t >> Se aqui der erro de 'Error: connect ECONNREFUSED',\n \t\t >> verifique suas credenciais de acesso ao banco\n \t\t >> e se o servidor de seu BD está rodando corretamente. \n\n function listar()");
    var instrucao = `
        SELECT * FROM Funcionario;
    `;
    console.log("Executando a instrução SQL: \n" + instrucao);
    return database.executar(instrucao);
}


module.exports = {
    buscarFuncionarios,
    deletarFuncionarios,
    listar,
    cadastrar
}