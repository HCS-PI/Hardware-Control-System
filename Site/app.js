var express = require("express");
var cors = require("cors");
var path = require("path");
var port = 3333;

var app = express();

var userRouter = require("./src/routes/user");

app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(express.static(path.join(__dirname, "view")));

app.use(cors());

app.use("/user", userRouter);

app.listen(port, function () {
    console.log(`Rodando em: http://localhost:${port}`);
});