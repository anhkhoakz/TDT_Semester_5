const multer = require("multer");
const path = require("path");

let imagePath = "";

const storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, "public/images");
    },
    filename: (req, file, cb) => {
        const originalName = file.originalname;
        const extension = path.extname(originalName);
        const baseName = path.basename(originalName, extension);
        const currentDate = new Date().getTime();

        let finalName = originalName;

        finalName = `${baseName}-${currentDate}${extension}`;

        cb(null, finalName);
    },
});

const imageFileFilter = (req, file, cb) => {
    if (!file.mimetype.startsWith("image/")) {
        return cb(new Error("Only image files are allowed!"), false);
    }
    cb(null, true);
};

const upload = multer({ storage: storage, fileFilter: imageFileFilter });

module.exports = upload;
