var express = require("express");
var router = express.Router();

var dashGestorController = require("../controllers/dashGestorController");

router.post("/mediaCpuCarros", function (req, res) {
    console.log('Chegou na rota!')
    dashGestorController.mediaCpuCarrosController(req, res);
});
router.post("/mediaRamCarros", function (req, res) {
    console.log('Chegou na rota!')
    dashGestorController.mediaRamCarrosController(req, res);
});


module.exports = router;