const express = require("express");
const router = express.Router();
const bodyParser = require("body-parser");
require("dotenv").config();

router.use(bodyParser.urlencoded({ extended: false }));

router.get("/", (req, res, next) => {
    res.render("login");
});

router.post("/", (req, res, next) => {
    const { email, password } = req.body;
    if (!email || !password) {
        return res.status(400).render("login", {
            message: "Please provide all required fields",
        });
    }

    // Additional checkers
    if (!validateEmail(email)) {
        return res.status(400).render("login", {
            message: "Invalid email format",
        });
    }

    if (
        email !== process.env.LOGIN_EMAIL ||
        password !== process.env.LOGIN_PASSWORD
    ) {
        return res.status(401).render("login", {
            message: "Invalid login credentials",
        });
    }

    req.session.isLoggedIn = true;
    return res.redirect("/");
});

const validateEmail = (email) => {
    const re =
        /[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?/g;
    return re.test(email);
};

module.exports = router;
