const express = require("express");
const router = express.Router();
require("dotenv").config();

const products = [
    { id: 1, name: "iPhone 12 Pro Max", price: 15000000 },
    { id: 2, name: "iPhone 13 Pro Max", price: 20000000 },
    { id: 3, name: "iPhone 14 Pro Max", price: 25000000 },
];

router.get("/", (req, res, next) => {
    return res.status(200).json(products);
});

router.get("/:id", (req, res, next) => {
    const product = products.find(
        (product) => product.id === Number(req.params.id)
    );
    if (!product) {
        return res.status(404).json({ message: "Product not found" });
    }
    return res.status(200).json(product);
});

router.put("/:id", async (req, res, next) => {
    const product = products.find(
        (product) => product.id === Number(req.params.id)
    );

    if (!product) {
        return res.status(404).json({ message: "Product not found" });
    }

    const { name, price } = req.body;

    if (!name && !price) {
        return res
            .status(400)
            .json({ message: "Please provide name or price" });
    }

    if (name) {
        product.name = name;
    }

    if (price) {
        product.price = price;
    }

    return res.status(200).json(product);
});

module.exports = router;
