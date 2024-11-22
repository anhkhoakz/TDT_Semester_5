const express = require("express");
const router = express.Router();
const accountController = require("../controllers/account.controller");

router.use(express.urlencoded({ extended: false }));

router.get("/login", (req, res) => {
    res.render("login", {
        error: null,
    });
});

router.post("/login", (req, res) => {
    accountController.login(req, res);
});

router.get("/register", (req, res) => {
    res.render("register", {
        error: null,
    });
});
router.post("/register", (req, res) => {
    accountController.createAccount(req, res);
});

module.exports = router;
