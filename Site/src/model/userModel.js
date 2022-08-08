var db = require("../database/connection");

function test(query) {
    return db.execute(query);
}

module.exports = {
    test
}