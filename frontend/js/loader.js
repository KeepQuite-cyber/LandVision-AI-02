class Loader {
    static element =
        document.getElementById("mapLoader");
    static show() {
        this.element.classList.remove("d-none");

    }
    static hide() {
        this.element.classList.add("d-none");

    }

}