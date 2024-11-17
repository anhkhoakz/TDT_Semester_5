const Order = require("../models/orders.models");
const Products = require("../models/products.models");

exports.getAllOrders = async (req, res) => {
    const { user } = req;

    try {
        const orders = await Order.find({ user: user._id }).populate(
            "products.productId"
        );

        res.status(200).json(orders);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.createOrder = async (req, res) => {
    const { products } = req.body;

    if (!products || !Array.isArray(products) || products.length === 0) {
        return res.status(400).json({ message: "Products list is required" });
    }

    try {
        const productIds = products.map((item) => item.productId);

        const productDetails = await Products.find({
            _id: { $in: productIds },
        });

        if (productDetails.length !== productIds.length) {
            return res.status(404).json({ message: "Some products not found" });
        }

        const totalSellingPrice = products.reduce((total, item) => {
            const product = productDetails.find(
                (p) => p._id.toString() === item.productId
            );
            return product ? total + product.price * item.quantity : total;
        }, 0);

        const newOrder = new Order({
            totalSellingPrice,
            products,
            user: req.user._id,
        });

        const result = await newOrder.save();

        res.status(201).json({
            message: "Order created successfully",
            order: result,
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.getOrderById = async (req, res) => {
    const id = req.params.id;
    const { user } = req;

    try {
        const order = await Order.findOne({ _id: id, user: user._id }).populate(
            "products.productId"
        );

        if (!order) {
            return res.status(404).json({ message: "Order not found" });
        }

        res.status(200).json(order);
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.updateOrder = async (req, res) => {
    const id = req.params.id;
    const { products } = req.body;

    if (!products || !Array.isArray(products) || products.length === 0) {
        return res.status(400).json({ message: "Products list is required" });
    }

    try {
        const productIds = products.map((item) => item.productId);

        const productDetails = await Products.find({
            _id: { $in: productIds },
        });

        if (productDetails.length !== productIds.length) {
            return res.status(404).json({ message: "Some products not found" });
        }

        const totalSellingPrice = products.reduce((total, item) => {
            const product = productDetails.find(
                (p) => p._id.toString() === item.productId
            );
            return product ? total + product.price * item.quantity : total;
        }, 0);

        const updatedOrder = {
            totalSellingPrice,
            products,
        };

        const result = await Order.findOneAndUpdate(
            { _id: id, user: req.user._id },
            updatedOrder,
            { new: true }
        );

        if (!result) {
            return res
                .status(404)
                .json({ message: "Order not found or unauthorized" });
        }

        res.status(200).json({
            message: "Order updated successfully",
            order: result,
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.deleteOrder = async (req, res) => {
    const id = req.params.id;

    try {
        const result = await Order.findOneAndDelete({
            _id: id,
            user: req.user._id,
        });

        if (!result) {
            return res
                .status(404)
                .json({ message: "Order not found or unauthorized" });
        }

        res.status(200).json({
            message: "Order deleted successfully",
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};

exports.deleteAllOrders = async (req, res) => {
    try {
        await Order.deleteMany({ user: req.user._id });
        res.status(200).json({
            message: "All orders deleted successfully",
        });
    } catch (err) {
        res.status(500).json({ error: err.message });
    }
};
