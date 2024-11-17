const accountController = require("../../controllers/account.controllers");
const express = require("express");
const router = express.Router();

router.get("/", accountController.getAllAccounts);

router.post("/register", accountController.createAccount);
router.post("/login", accountController.login);

module.exports = router;
