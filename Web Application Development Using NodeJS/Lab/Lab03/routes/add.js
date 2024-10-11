const express = require("express");
const router = express.Router();
const multer = require("multer");

require("dotenv").config();

router.use(express.urlencoded({ extended: false }));

router.get("/", async (req, res, next) => {
    res.render("add");
});

router.post("/", async (req, res) => {
    console.log(req.body);
    res.send(req.body);
});

router.get("/:id", async (req, res, next) => {
    // const product = products.find(
    //     (product) => product.id === Number(req.params.id)
    // );
    // if (!product) {
    //     return res.status(404).json({ message: "Product not found" });
    // }
    // res.render("product", { product });
});

router.put("/:id", async (req, res, next) => {
    // const product = products.find(
    //     (product) => product.id === Number(req.params.id)
    // );
    // if (!product) {
    //     return res.status(404).json({ message: "Product not found" });
    // }
    // const { name, price } = req.body;
    // if (!name && !price) {
    //     return res
    //         .status(400)
    //         .json({ message: "Please provide name or price" });
    // }
    // if (name) {
    //     product.name = name;
    // }
    // if (price) {
    //     product.price = price;
    // }
    // return res.status(200).json(product);
});

module.exports = router;
