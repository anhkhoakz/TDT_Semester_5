const express = require("express");
const bodyParser = require("body-parser");
const session = require("express-session");
require("dotenv").config();

const indexRouter = require("./routes/index");
const loginRouter = require("./routes/login");
const productRouter = require("./routes/product");
const addRouter = require("./routes/add");

const isLoggedIn = require("./middlewares/isLoggedIn");

const app = express();
const PORT = process.env.PORT || 8080;

app.use(bodyParser.urlencoded({ extended: false }));
app.set("view engine", "ejs");
app.use(
    session({
        secret: process.env.SESSION_SECRET,
        resave: false,
        saveUninitialized: true,
        cookie: { secure: false },
    })
);

app.use("/login", loginRouter);

// app.use(isLoggedIn);

app.use("/", indexRouter);
app.use("/products", productRouter);
app.use("/add", addRouter);

app.use((err, req, res, next) => {
    res.locals.message = err.message;
    res.locals.error = err;
    return res.status(err.status || 500).json({
        code: err.status || 500,
        message: err.message || "Internal Server Error",
    });
});

app.listen(PORT, () => {
    console.log("Server is running on http://localhost:" + PORT);
});
