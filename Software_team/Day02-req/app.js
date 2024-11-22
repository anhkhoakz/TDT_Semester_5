var createError = require("http-errors");
var express = require("express");
var path = require("path");
var cookieParser = require("cookie-parser");
var logger = require("morgan");
var fs = require("fs");

var indexRouter = require("./routes/index");

var app = express();

// view engine setup
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.use(logger("dev"));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, "public")));

app.use("/", indexRouter);

// Route to get users.json
app.get("/users", (req, res) => {
    fs.readFile("users.json", "utf8", (err, data) => {
        if (err) {
            res.status(500).send("Error reading file");
            return;
        }
        res.json(JSON.parse(data));
    });
});

// Route to post data to users.json
app.post("/users", (req, res) => {
    fs.readFile("users.json", "utf8", (err, data) => {
        if (err) {
            res.status(500).send("Error reading file");
            return;
        }
        const users = JSON.parse(data);
        let maxId = 0;
        users.forEach((user) => {
            if (user.id > maxId) {
                maxId = user.id;
            }
        });
        req.body.id = maxId + 1;
        users.push(req.body);

        fs.writeFile("users.json", JSON.stringify(users, null, 4), (err) => {
            if (err) {
                res.status(500).send("Error writing file");
                return;
            }
            res.status(201).send("User added");
        });
    });
});

// catch 404 and forward to error handler
app.use(function (req, res, next) {
    next(createError(404));
});

// error handler
app.use(function (err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get("env") === "development" ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render("error");
});

module.exports = app;
