var express = require("express");
var router = express.Router();

var dashTecnicoController = require("../controllers/dashTecnicoController");

router.post("/carrosMonitorados", function (req, res) {
    console.log('Chegou na rota!')
    dashTecnicoController.carrosMonitorados(req, res);
});

router.post("/verCarros", function (req, res) {
    console.log('Cheguei na rota!')
    dashTecnicoController.buscarCarros(req, res);
});

module.exports = router;