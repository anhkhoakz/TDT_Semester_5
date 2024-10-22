const express = require("express");
const router = express.Router();
const bodyParser = require("body-parser");
const jsonParser = bodyParser.json();
const upload = require("../middlewares/imageUploader");
const fs = require("fs");
require("dotenv").config();

router.use(express.urlencoded({ extended: false }));

const PRODUCT_FILE = "public/database/products.json";

const fetchProducts = async () => {
    const products = JSON.parse(fs.readFileSync(PRODUCT_FILE, "utf8"));
    return products;
};

router.get("/", async (req, res, next) => {
    const products = await fetchProducts();
    return res.status(200).json(products);
});

// router.post("/", jsonParser, (req, res, next) => {
//     const { id, name, price, image } = req.body;

//     if (!id || !name || !price) {
//         return res.status(400).json({ message: "Insufficient data" });
//     }

//     const newProduct = {
//         id: products.length + 1,
//         name,
//         price,
//     };

//     products.push(newProduct);

//     return res.status(201).json(newProduct);
// });

router.get("/add", async (req, res, next) => {
    res.render("add");
});

router.post("/add", upload.single("image"), async (req, res) => {
    const products = await fetchProducts();
    const ImagePath = "/images/" + req.file.filename;

    products.push({
        id: products.length + 1,
        name: req.body.name,
        price: req.body.price,
        image: ImagePath,
    });

    // add data to products.json

    fs.writeFileSync(PRODUCT_FILE, JSON.stringify(products, null, 4), "utf8");

    res.redirect("/");
});

router.get("/:id", async (req, res, next) => {
    const products = await fetchProducts();
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
