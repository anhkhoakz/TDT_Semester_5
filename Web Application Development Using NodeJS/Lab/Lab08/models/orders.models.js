const mongoose = require("mongoose");

const orderSchema = new mongoose.Schema({
    totalSellingPrice: {
        type: Number,
        required: true,
    },
    products: [
        {
            productId: {
                type: mongoose.Schema.Types.ObjectId,
                ref: "Product",
                required: true,
            },
            quantity: {
                type: Number,
                required: true,
                min: 1,
            },
        },
    ],
    user: {
        type: mongoose.Schema.Types.ObjectId,
        ref: "Account",
        required: true,
    },
    createdAt: {
        type: Date,
        default: Date.now,
    },
});

module.exports = mongoose.model("Order", orderSchema);
