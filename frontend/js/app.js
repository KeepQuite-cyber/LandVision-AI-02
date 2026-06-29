document.addEventListener("DOMContentLoaded", async () => {
    try {
        MapManager.init();
        await SidebarManager.init();
        SearchManager.init();
        AIManager.init();
        console.log("LandVision AI Started");
    }
    catch (error) {
        console.error(error);
    }
});