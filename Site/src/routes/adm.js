var express = require("express");
var router = express.Router();

var admController = require("../controllers/admController");

router.post("/pegarFunc", function (req, res) {
    console.log('Cheguei na rota!')
    admController.buscarFuncionarios(req, res);
});

router.post("/deleteFunc", function (req, res) {
    console.log('Cheguei na rota do delete!')
    admController.deletarFuncionarios(req, res);
    
});

router.post("/cadastro", function (req, res) {
    console.log('Cheguei na rota do cadastro!')
    admController.cadastrarFuncionarios(req, res);
});

router.post("/autenticarF", function (req, res) {
    admController.entrarFuncionario(req, res);
});


module.exports = router;