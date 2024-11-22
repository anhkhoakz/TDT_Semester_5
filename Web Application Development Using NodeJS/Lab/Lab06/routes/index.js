const express = require("express");
const router = express.Router();
const fileController = require("../controllers/file.controller");

/* GET home page. */
router.get("/", async (req, res, next) => {
    const files = await fileController.getFiles();

    res.render("index", { title: "Express", files });
});

module.exports = router;
