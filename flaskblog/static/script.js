document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.getElementById("menu-btn");
    const mobileMenu = document.getElementById("mobile-menu");
    const iconOpen = document.getElementById("icon-open");
    const iconClose = document.getElementById("icon-close");

    if (menuBtn && mobileMenu && iconOpen && iconClose) {
        menuBtn.addEventListener("click", () => {
            const isOpen = !mobileMenu.classList.contains("hidden");

            mobileMenu.classList.toggle("hidden");
            iconOpen.classList.toggle("hidden");
            iconClose.classList.toggle("hidden");
            menuBtn.setAttribute("aria-expanded", String(!isOpen));
        });

        mobileMenu.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                mobileMenu.classList.add("hidden");
                iconOpen.classList.remove("hidden");
                iconClose.classList.add("hidden");
                menuBtn.setAttribute("aria-expanded", "false");
            });
        });
    }

    const deleteBtn = document.getElementById("deleteBtn");
    const deleteModal = document.getElementById("deleteModal");
    const deleteModalBackdrop = document.getElementById("deleteModalBackdrop");
    const cancelDeleteBtn = document.getElementById("cancelDeleteBtn");

    if (deleteBtn && deleteModal && deleteModalBackdrop && cancelDeleteBtn) {
        function openModal() {
            deleteModal.classList.remove("hidden");
        }

        function closeModal() {
            deleteModal.classList.add("hidden");
        }

        deleteBtn.addEventListener("click", openModal);
        cancelDeleteBtn.addEventListener("click", closeModal);
        deleteModalBackdrop.addEventListener("click", closeModal);

        document.addEventListener("keydown", (e) => {
            if (e.key === "Escape") closeModal();
        });
    }
});