let map;
let plotLayer;
const plotLayers = new Map();
let markerLayer = L.layerGroup();
let activeLayer = null;
let blinkInterval = null;
class MapManager {
    static init() {
        map = L.map("map", {
            zoomControl: true
        }).setView([26.7606, 83.3732], 11);
        L.tileLayer(
            "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
            {
                maxZoom: 20,
                attribution:
                    "&copy; OpenStreetMap Contributors"
            }
        ).addTo(map);

        markerLayer.addTo(map)

    }
    static defaultStyle(feature) {
        return {
            color: "#198754",
            weight: 2,
            opacity: 1,
            fillColor: "#20c997",
            fillOpacity: 0.5
        };
    }
    static resetHighlightedPlot() {
    if (blinkInterval) {
        clearInterval(blinkInterval);
        blinkInterval = null;
    }

    if (activeLayer && plotLayer) {
        plotLayer.resetStyle(activeLayer);
    }

    activeLayer = null;
}
    static highlightStyle(layer) {
        layer.setStyle({
            color: "#0d6efd",
            weight: 4,
            fillColor: "#0d6efd",
            fillOpacity: 0.65
        });
        layer.bringToFront();
    }
    static resetStyle(event) {
        plotLayer.resetStyle(event.target);
    }

    static buildPopup(properties) {
        return `
            <div class="plot-popup">
                <h5 class="text-success mb-3">
                    Plot ${properties.plot_number}
                </h5>
                <table class="table table-sm table-bordered mb-0">
                    <tr>
                        <th>Owner</th>
                        <td>${properties.owner_name ?? "-"}</td>
                    </tr>
                    <tr>
                        <th>Area</th>
                        <td>${properties.area ?? "-"} Sq.m</td>
                    </tr>
                    <tr>
                        <th>Land Use</th>
                        <td>${properties.land_use ?? "-"}</td>
                    </tr>
                    <tr>
                        <th>Village</th>
                        <td>${properties.village_name ?? "-"}</td>
                    </tr>
                    <tr>
                        <th>Tehsil</th>
                        <td>${properties.tehsil_name ?? "-"}</td>
                    </tr>
                    <tr>
                        <th>District</th>
                        <td>${properties.district_name ?? "-"}</td>
                    </tr>
                    <tr>
                        <th>State</th>
                        <td>${properties.state_name ?? "-"}</td>
                    </tr>
                    <tr>
                        <th>Remarks</th>
                        <td>${properties.remarks || "-"}</td>
                    </tr>
                </table>
            </div>
        `;
    }

    static drawPlots(geojson) {
        if (plotLayer) {
        this.resetHighlightedPlot();
        map.removeLayer(plotLayer);
        }
        markerLayer.clearLayers();
        plotLayer = L.geoJSON(geojson, {
            style: this.defaultStyle,
            onEachFeature: (feature, layer) => { const plotNumber = feature.properties.plot_number.toString();
                 plotLayers.set( plotNumber, layer );
                layer.bindPopup(
                    this.buildPopup(feature.properties)
                );
                const center = layer.getBounds().getCenter();
                const marker = L.marker(center, {
                     icon: L.divIcon({
                        className: "plot-marker",
                        html: `
                            <div class="plot-pin">
                📍
                                <span>${feature.properties.plot_number}</span>
                            </div>
                        `,
                        iconSize: [40, 40],
                        iconAnchor: [20, 40]
                        })
                    });

                    marker.bindPopup(this.buildPopup(feature.properties));
                    markerLayer.addLayer(marker);
                layer.on({
                    mouseover: (e) => {
                        this.highlightStyle(e.target);
                    },
                    mouseout: (e) => {
                        this.resetStyle(e);
                    },
                    click: (e) => {
                        map.fitBounds(
                            e.target.getBounds(),
                            {
                                padding: [40, 40]
                            }
                        );
                    }
                });
            }

        }).addTo(map);

        if (plotLayer.getLayers().length > 0) {

            map.fitBounds(
                plotLayer.getBounds(),
                {
                    padding: [30, 30]
                }
            );

        }

    }
static getPlotLayer(plotNumber) {
    return plotLayers.get(
        plotNumber.toString()
    );

}

static zoomToPlot(plotNumber) {
    const layer = this.getPlotLayer(plotNumber);
    if (!layer) {
        return false;
    }
    map.fitBounds(
        layer.getBounds(),
        {
            padding: [50, 50],
            maxZoom: 20
        }
    );

    layer.openPopup();
    return true;
}


static highlightPlot(plotNumber) {
    const layer = this.getPlotLayer(plotNumber);
    if (!layer) {
        return false;
    }
    this.resetHighlightedPlot();
    activeLayer = layer;
    map.flyToBounds(layer.getBounds(), {
        padding: [70, 70],
        duration: 1.8,
        maxZoom: 20
    });
    layer.openPopup();
    let visible = true;
    blinkInterval = setInterval(() => {
        if (visible) {
            layer.setStyle({
                color: "#ff0000",
                weight: 7,
                fillColor: "#ffff00",
                fillOpacity: 1
            });

        } else {

            layer.setStyle({
                color: "#198754",
                weight: 2,
                fillColor: "#20c997",
                fillOpacity: 0.45
            });

        }

        visible = !visible;

    }, 400);
    setTimeout(() => {
        if (activeLayer === layer) {
            clearInterval(blinkInterval);
            blinkInterval = null;
            layer.setStyle({
                color: "#ff0000",
                weight: 6,
                fillColor: "#ffff00",
                fillOpacity: 0.8
            });
        }
    }, 5000);
    return true;
}
static clearPlots() {
    this.resetHighlightedPlot();
    if (plotLayer) {
        map.removeLayer(plotLayer);
        plotLayer = null;
    }
    plotLayers.clear();
}
}