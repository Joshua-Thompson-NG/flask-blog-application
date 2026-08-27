document.addEventListener("DOMContentLoaded", () => {
    const menuBtn = document.getElementById("menu-btn");
    const mobileMenu = document.getElementById("mobile-menu");
    const iconOpen = document.getElementById("icon-open");
    const iconClose = document.getElementById("icon-close");

    if (!menuBtn || !mobileMenu || !iconOpen || !iconClose) {
        return;
    }

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
});