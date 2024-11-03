document.addEventListener("DOMContentLoaded", function () {
    var deleteConfirmModal = document.getElementById("deleteConfirmModal");
    deleteConfirmModal.addEventListener("show.bs.modal", function (event) {
        var button = event.relatedTarget;
        var productId = button.getAttribute("data-product-id");
        var productName = button.getAttribute("data-product-name");
        // var deleteForm = document.getElementById("deleteForm");
        var modalBody = deleteConfirmModal.querySelector(".modal-body p");

        // deleteForm.action =
        //     "/products/" + productId + "/delete";
        modalBody.textContent =
            "Bạn có chắc muốn xóa sản phẩm " + productName + "?";
    });
});
