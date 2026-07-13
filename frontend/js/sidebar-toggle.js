class SidebarToggle {

    static init() {

        this.sidebar =
            document.getElementById("sidebar");

        this.button =
            document.getElementById("sidebarToggle");

        this.button.addEventListener("click", () => {

            this.sidebar.classList.toggle("open");

            if (this.sidebar.classList.contains("open")) {

                this.button.innerHTML = "✕";

            } else {

                this.button.innerHTML = "☰";

            }

        });

    }

}