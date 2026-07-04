class ApiService {
    static async request(endpoint, params = {}) {
        try {
            const url = new URL(
                CONFIG.BASE_URL + endpoint
            );
            Object.entries(params).forEach(([key, value]) => {
                if (value !== null &&value !== undefined &&value !== "") {
                    url.searchParams.append(key, value);
                }
            });
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(
                    `HTTP ${response.status} : ${response.statusText}`
                );
            }
            const data = await response.json();
            if (Array.isArray(data)) {
                return data;
            }
            if (data.results) {
                return data.results;
            }
            return data;
        }
        catch (error) {
            console.error(
                "API Error:",
                error.message
            );
            return [];
        }
    }

    static async getStates() {
        return await this.request(
            CONFIG.ENDPOINTS.STATES
        );

    }

    static async getDistricts(stateId = "") {
        return await this.request(
            CONFIG.ENDPOINTS.DISTRICTS,
            {
                state: stateId
            }
        );

    }

    static async getTehsils(districtId = "") {
        return await this.request(
            CONFIG.ENDPOINTS.TEHSILS,
            {
                district: districtId
            }
        );

    }

    static async getVillages(tehsilId = "") {
        return await this.request(
            CONFIG.ENDPOINTS.VILLAGES,
            {
                tehsil: tehsilId
            }
        );
    }

    static async getPlots(filters = {}) {
        return await this.request(
            CONFIG.ENDPOINTS.PLOTS,
            filters
        );
    }

    static async getMapData(villageId = "") {
        return await this.request(
            CONFIG.ENDPOINTS.MAP,
            {
                village: villageId
            }
        );
    }
    
    static async getPlot(plotId) {
       return await this.request(
            CONFIG.ENDPOINTS.PLOTS + plotId + "/"
        );
    }

    static async searchPlot(keyword) {
    return await this.request(
        CONFIG.ENDPOINTS.SEARCH_PLOT,
        {
            search: keyword
        }
    );
}
static async chat(message) {

    try {

        const response = await fetch(

            CONFIG.BASE_URL +

            CONFIG.ENDPOINTS.AI_CHAT,

            {

                method: "POST",

                headers: {

                    "Content-Type": "application/json"

                },

                body: JSON.stringify({

                    message

                })

            }

        );

        if (!response.ok) {

            throw new Error(
                `HTTP ${response.status}`
            );

        }

        return await response.json();

    }

    catch (error) {

        console.error(
            "AI Error:",
            error
        );

        return null;

    }

}
}