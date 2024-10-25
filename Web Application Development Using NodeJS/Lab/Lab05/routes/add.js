const express = require("express");
const router = express.Router();

router.get("/", (req, res, next) => {
    res.render("add", { error: null });
});

router.post("/", (req, res, next) => {
    const { num1, num2 } = req.body;
    if (isNaN(num1) || isNaN(num2)) {
        res.render("add", { error: "Please enter valid numbers" });
    } else {
        res.render("add", { result: Number(num1) + Number(num2) });
    }
});

module.exports = router;
