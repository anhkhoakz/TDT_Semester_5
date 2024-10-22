const express = require("express");
const bodyParser = require("body-parser");
const session = require("express-session");
const path = require("path");
require("dotenv").config();

// Routers
const indexRouter = require("./routes/index");
const loginRouter = require("./routes/login");
const productRouter = require("./routes/product");
const errorRouter = require("./routes/error");

// Middlewares
const isLoggedIn = require("./middlewares/isLoggedIn");

// App
const app = express();
const SERVER = process.env.SERVER || "localhost";
const PORT = process.env.PORT || 8080;

// Middlewares Configurations
app.use(bodyParser.urlencoded({ extended: false }));
app.set("view engine", "ejs");
app.use(
    session({
        secret:
            process.env.SESSION_SECRET || "pAr8MznVH7H17quHbeNEUs6KwcdwzQkR",
        resave: false,
        saveUninitialized: true,
        cookie: { secure: false },
    })
);
app.use(express.static(path.join(__dirname, "public")));

// Routes
app.use("/login", loginRouter);
// app.use(isLoggedIn);
app.use("/", indexRouter);
app.use("/products", productRouter);

app.use("*", errorRouter);

app.listen(PORT, () => {
    console.log(`Server is running on http://${SERVER}:${PORT}`);
});
