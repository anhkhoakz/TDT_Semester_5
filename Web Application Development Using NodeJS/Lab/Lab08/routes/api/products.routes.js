const express = require("express");
const router = express.Router();
const productsController = require("../../controllers/products.controllers");
const upload = require("../../config/multer.config");

router.get("/", productsController.getAllProducts);
router.get("/:id", productsController.getProduct);
router.post("/", upload.single("image"), productsController.createProduct);
router.put("/:id", upload.single("image"), productsController.updateProduct);
router.delete("/:id", productsController.deleteProduct);

module.exports = router;
