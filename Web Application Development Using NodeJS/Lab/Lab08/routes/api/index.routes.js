const express = require("express");
const router = express.Router();

const authMiddleware = require("../../middlewares/auth.middlewares");

const productsRoutes = require("./products.routes");
const ordersRoutes = require("./orders.routes");
const accountRoutes = require("./account.routes");

router.use("/products", productsRoutes);
router.use("/orders", authMiddleware.verifyToken, ordersRoutes);
router.use("/account", accountRoutes);

module.exports = router;
