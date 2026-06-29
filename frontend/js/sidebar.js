class SidebarManager {
    static stateSelect = document.getElementById("stateSelect");
    static districtSelect = document.getElementById("districtSelect");
    static tehsilSelect = document.getElementById("tehsilSelect");
    static villageSelect = document.getElementById("villageSelect");

    static async init() {
    this.registerEvents();
    await this.loadStates();
    }
    static populateDropdown(selectElement, data, placeholder) {
        selectElement.innerHTML = "";
        const defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.textContent = placeholder;
        selectElement.appendChild(defaultOption);
        data.forEach(item => {
            const option = document.createElement("option");
            option.value = item.id;
            option.textContent = item.name;
            selectElement.appendChild(option);
        });
    }
    static resetDropdown(selectElement, placeholder) {
        selectElement.innerHTML = "";
        const option = document.createElement("option");
        option.value = "";
        option.textContent = placeholder;
        selectElement.appendChild(option);
    }
static resetHierarchy(level) {
        switch (level) {
            case "state":
                this.resetDropdown(
                    this.districtSelect,
                    "Select District"
                );
                this.resetDropdown(
                    this.tehsilSelect,
                    "Select Tehsil"
                );
                this.resetDropdown(
                    this.villageSelect,
                    "Select Village"
                );
                break;

            case "district":

                this.resetDropdown(
                    this.tehsilSelect,
                    "Select Tehsil"
                );

                this.resetDropdown(
                    this.villageSelect,
                    "Select Village"
                );

                break;
            case "tehsil":
                this.resetDropdown(
                    this.villageSelect,
                    "Select Village"
                );
                break;
        }
    }
    static async loadStates() {
        const states = await ApiService.getStates();
        this.populateDropdown(
            this.stateSelect,
            states,
            "Select State"
        );
    }

static async loadDistricts(stateId) {
    this.resetHierarchy("state");
    if (!stateId) return;
    const districts = await ApiService.getDistricts(stateId);
    this.populateDropdown(
        this.districtSelect,
        districts,
        "Select District"
    );

}
static async loadTehsils(districtId) {
    this.resetHierarchy("district");
    if (!districtId) return;
    const tehsils = await ApiService.getTehsils(districtId);
    this.populateDropdown(
        this.tehsilSelect,
        tehsils,
        "Select Tehsil"
    );

}
    static async loadVillages(tehsilId) {
        this.resetHierarchy("tehsil");
    if (!tehsilId) return;
    const villages = await ApiService.getVillages(tehsilId);
    this.populateDropdown(
        this.villageSelect,
        villages,
        "Select Village"
    );

}

static async onStateChange(event) {
    const stateId = event.target.value;
    await this.loadDistricts(stateId);
}

static async onDistrictChange(event) {
    const districtId = event.target.value;
    await this.loadTehsils(districtId);
}

static async onTehsilChange(event) {
    const tehsilId = event.target.value;
    await this.loadVillages(tehsilId);
 }

static async onVillageChange(event) {
    const villageId = event.target.value;
    if (!villageId) {
        MapManager.clearPlots();
        this.clearPlotInfo();
        return;
    }
    await this.loadVillagePlots(villageId);
}

static async loadVillagePlots(villageId) {
    const plots = await ApiService.getMapData(villageId);
    if (!plots || plots.length === 0) {
        MapManager.clearPlots();
        this.updatePlotInfo([]);
        return;
    }

    const geojson = {
        type: "FeatureCollection",
        features: []
    };

    plots.forEach(plot => {
        geojson.features.push({
            type: "Feature",
            geometry: plot.polygon,
            properties: {
                id: plot.id,
                plot_number: plot.plot_number,
                owner_name: plot.owner_name,
                area: plot.area,
                land_use: plot.land_use,
                village_name: plot.village_name,
                tehsil_name: plot.tehsil_name,
                district_name: plot.district_name,
                state_name: plot.state_name,
                remarks: plot.remarks
            }
        });
    });
    MapManager.drawPlots(geojson);
    this.updatePlotInfo(plots);
}
static updatePlotInfo(plots) {
    const container = document.getElementById("plotInfo");
    if (!plots || plots.length === 0) {
        console.log(plots)
        container.innerHTML = `
            <h5>Plot Details</h5>
            <p>No plots found.</p>
        `;
        return;
    }
    const village = plots[0];
    let totalPlot = []
    for(let i=0; i < plots.length; i++){
        totalPlot.push(plots[i].plot_number)
    }
    
    container.innerHTML = `
        <h5>Village Summary</h5>
        <hr>
        <p><strong>Total Plots:</strong> ${plots.length}</p>
        <p><strong>Village:</strong> ${village.village_name}</p>
        <p><strong>District:</strong> ${village.district_name}</p>
        <p><strong>State:</strong> ${village.state_name}</p>

        <h6>Available Plot Numbers</h6>

        <div class="plot-list">
            ${totalPlot}
        </div>
    `;
}
static clearPlotInfo() {
    document.getElementById("plotInfo").innerHTML = `
        <h5>Plot Details</h5>
        <p>Select a village to view plots.</p>
    `;
}
 static registerEvents() {
    this.stateSelect.addEventListener(
        "change",
        this.onStateChange.bind(this)
    );

    this.districtSelect.addEventListener(
        "change",
        this.onDistrictChange.bind(this)
    );

    this.tehsilSelect.addEventListener(
        "change",
        this.onTehsilChange.bind(this)
    );

    this.villageSelect.addEventListener(
        "change",
        this.onVillageChange.bind(this)
    );
    }
}