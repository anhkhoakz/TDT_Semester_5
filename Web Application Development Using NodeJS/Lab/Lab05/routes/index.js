const express = require("express");
const router = express.Router();

/* GET home page. */
router.get("/", (req, res, next) => {
    res.render("index", { title: "Express" });
});

router.get("/:id", (req, res, next) => {
    res.render("profile", { title: req.params.id });
});

module.exports = router;
