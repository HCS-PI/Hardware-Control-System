var express = require("express");
var router = express.Router();

var userController = require("../controller/userController");

router.get("/", function (req, res) {
    userController.test(req, res);
});

module.exports = router;