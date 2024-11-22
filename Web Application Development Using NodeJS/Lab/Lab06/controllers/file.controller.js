const fs = require("fs");
const path = require("path");

const uploadsDir = path.join(__dirname, "../uploads/4");

const convertSize = (fileSize) => {
    const sizes = ["Bytes", "KB", "MB", "GB", "TB"];
    if (fileSize == 0) return "0 Byte";
    const i = parseInt(Math.floor(Math.log(fileSize) / Math.log(1024)));
    const size = Math.round(fileSize / Math.pow(1024, i), 2);

    return `${size} ${sizes[i]}`;
};

const formatDate = (date) => {
    const day = date.getDate().toString().padStart(2, "0");
    const month = (date.getMonth() + 1).toString().padStart(2, "0");
    const year = date.getFullYear();
    const hours = date.getHours().toString().padStart(2, "0");
    const minutes = date.getMinutes().toString().padStart(2, "0");

    return `${day}/${month}/${year} ${hours}:${minutes}`;
};

const getFiles = (dir) => {
    try {
        const directory = fs.readdirSync(uploadsDir);
        const directoryMap = directory.map((file) => {
            const filePath = path.join(uploadsDir, file);
            const stats = fs.statSync(filePath);

            return {
                name: file,
                path: filePath,
                isDirectory: stats.isDirectory(),
                size: convertSize(stats.size),
                date: formatDate(stats.mtime),
            };
        });
        return directoryMap;
    } catch (err) {
        console.error(err);
        return [];
    }
};

module.exports = {
    getFiles,
};
