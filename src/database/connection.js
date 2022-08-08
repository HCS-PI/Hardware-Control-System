var mysql = require("mysql2");

var mySQLuser = {
    host: "localhost",
    user: "fmsUser",
    database: "fms",
    password: "fmsUser",
};

function execute(querySent) {
        return new Promise(function (resolve, reject) {
        var conexao = mysql.createConnection(mySQLuser);
        conexao.connect();
        conexao.query(querySent, function (erro, resultados) {
            conexao.end();
            if (erro) {
                reject(erro);
            }
            console.log(resultados);
            resolve(resultados);
        });
        conexao.on('error', function (erro) {
            return (erro.sqlMessage);
        });
    });
}

module.exports = {
    execute
}