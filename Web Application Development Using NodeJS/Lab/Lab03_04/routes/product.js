const express = require("express");
const router = express.Router();
require("dotenv").config();

const products = [
    {
        id: 1,
        name: "iPhone 14",
        price: 599,
        image: "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-14-model-unselect-gallery-1-202209?wid=5120&hei=2880",
    },
    {
        id: 2,
        name: "iPhone 15",
        price: 699,
        image: "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-15-model-unselect-gallery-1-202309?wid=5120&hei=2880",
    },
    {
        id: 3,
        name: "iPhone 16",
        price: 799,
        image: "https://store.storeimages.cdn-apple.com/1/as-images.apple.com/is/iphone-16-model-unselect-gallery-1-202409?wid=5120&hei=2880",
    },
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
    return res.status(200).render("product", { product });
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
