'use strict';

var app = require("express")();
var bodyParser = require("body-parser");
var os = require("os");

app.set("view engine", "ejs");
app.set("views", __dirname + "/templates");
app.use(bodyParser.urlencoded({ extended: false }));

app.get("/product", (req, res) => { res.render("page-product", { page : 'Product', hostname : os.hostname() }); });

app.listen(80, '0.0.0.0');
