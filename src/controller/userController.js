var userModel = require("../model/userModel");

function test(req, res){
    userModel('SELECT * FROM  WHERE ').then(
        function (result) {
            if (result.length == 1) {
                res.json(result[0]);
            } else if (result.length == 0) {
                res.status(403).send("Not found data");
            }
        }
    );
}

module.exports = {
    test
}