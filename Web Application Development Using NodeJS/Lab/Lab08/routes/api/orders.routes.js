const express = require("express");
const router = express.Router();
const orderController = require("../../controllers/orders.controllers");
const authMiddleware = require("../../middlewares/auth.middlewares");

router.get("/", orderController.getAllOrders);
router.get("/:id", orderController.getOrderById);
router.use(authMiddleware.verifyToken);
router.post("/", orderController.createOrder);
router.put("/:id", orderController.updateOrder);
router.delete("/:id", orderController.deleteOrder);
// router.delete("/", orderController.deleteAllOrders);

module.exports = router;
