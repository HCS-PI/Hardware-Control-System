var express = require("express");
var router = express.Router();

var dashGestorController = require("../controllers/dashGestorController");

// Inserir essa rota no Router da DashGestor

router.post("/cpuTemperaturaServer", function (req, res) {
    console.log('Chegou na rota!')
    dashGestorController.cpuTemperaturaController(req, res);
});


module.exports = router;