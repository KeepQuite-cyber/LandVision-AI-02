class SearchManager {
    static searchInput = document.getElementById("plotSearch");
    static searchButton = document.getElementById("searchBtn");
    static init() {
        this.registerEvents();
    }
    static registerEvents() {
        this.searchButton.addEventListener(
            "click",
            () => this.search()
        );

        this.searchInput.addEventListener(
            "keypress",
            (event) => {
                if (event.key === "Enter") {
                    this.search();
                }
            }
        );
    }
    static async search() {
        const keyword = this.searchInput.value.trim();
        if (!keyword) {
            alert("Please enter a plot number.");
            return;
        }
        const plots = await ApiService.searchPlot(keyword);
        if (!plots || plots.length === 0) {
            alert("No plot found.");
            return;
        }
        const plot = plots[0];
        const found = MapManager.highlightPlot(
            plot.plot_number
        );

        if (!found) {
            alert(
                "Plot exists but is not loaded on map.\nSelect its village first."
            );
        }
    }
}