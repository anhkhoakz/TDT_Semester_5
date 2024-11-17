const path = require("path");
const Products = require("../models/products.models");
const fs = require("fs");

exports.getAllProducts = async (req, res) => {
    try {
        const products = await Products.find();
        res.status(200).json(products);
    } catch (err) {
        res.status(500).json({ error: err });
    }
};

exports.getProduct = async (req, res) => {
    const { id } = req.params;
    const product = await Products.findById(id);
    if (!product) {
        return res.status(404).json({ message: "Product not found" });
    }
    res.status(200).json(product);
};

exports.createProduct = async (req, res) => {
    const { productName, price, description } = req.body;

    const areEmptyFields = !productName || !price || !description;
    if (areEmptyFields) {
        return res
            .status(400)
            .json({ code: 400, message: "Missing required fields" });
    }

    try {
        const existingProduct = await Products.findOne({ productName });
        if (existingProduct) {
            return res
                .status(403)
                .json({ code: 403, message: "Product already exists" });
        }

        const newProduct = new Products({
            productName,
            price,
            description,
            image: req.file ? `/images/uploads/${req.file.filename}` : null,
        });

        const result = await newProduct.save();
        res.status(201).json({
            message: "Product created successfully",
            Product: result,
        });
    } catch (err) {
        res.status(500).json({ code: 500, error: err.message });
    }
};

exports.updateProduct = async (req, res) => {
    const { id } = req.params;
    const { productName, price, description } = req.body;

    try {
        const updateData = {};
        if (productName) updateData.productName = productName;
        if (price) updateData.price = price;
        if (description) updateData.description = description;
        if (req.file) {
            const existingProduct = await Products.findById(id);
            if (existingProduct && existingProduct.image) {
                fs.unlink(
                    path.join(__dirname, "../public/", existingProduct.image),
                    (err) => {
                        if (err) {
                            console.error("Error deleting file:", err);
                        }
                    }
                );
            }
            updateData.image = `/images/uploads/${req.file.filename}`;
        }

        const result = await Products.findOneAndUpdate(
            { _id: id },
            updateData,
            { new: true }
        );

        if (!result) {
            return res
                .status(404)
                .json({ code: 404, message: "Product not found" });
        }

        res.status(200).json({
            message: "Product updated successfully",
            Product: result,
        });
    } catch (err) {
        res.status(500).json({ code: 500, error: err.message });
    }
};

exports.deleteProduct = async (req, res) => {
    const { id } = req.params;

    try {
        const existingProduct = await Products.findById(id);
        if (!existingProduct) {
            return res
                .status(404)
                .json({ code: 404, message: "Product not found" });
        }

        if (existingProduct.image) {
            fs.unlink(existingProduct.image, (err) => {
                if (err) {
                    console.error("Error deleting file:", err);
                }
            });
        }

        await existingProduct.deleteOne();
        res.status(200).json({ message: "Product deleted successfully" });
    } catch (err) {
        res.status(500).json({ code: 500, error: err.message });
    }
};
