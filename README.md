# MetaHamilton Cesium Viewer

A web-based interactive 3D map viewer built with [CesiumJS](https://cesium.com/cesiumjs/). Explore terrain, buildings, and a variety of geographic layers for Liverpool and Wirral areas.

![Cesium Screenshot](screenshot.png)

---

## Features

- 3D terrain using Cesium World Terrain
- OpenStreetMap imagery
- 3D buildings (OSM Buildings)
- Toggleable GeoJSON layers for:
  - Buildings
  - Education facilities
  - Financial services
  - Healthcare facilities
  - Points of interest
  - Roads and waterways
- Performance mode for lower-spec machines
- Interactive selection highlights for polygons, polylines, and billboards

---

## Installation / Running Locally

1. Clone the repository:

```bash
git clone https://github.com/harry-ellis2/CesiumLiverpool.git
cd meta-hamilton-cesium
```

## Enable GPU rendering (Optional):
If you are using a computer that has integrated graphics (I-GPU) and you also have a dedicated GPU, performance may be increased (at the expense of increased power/battery consumption) by doing the following:

### NVIDIA:
Open NVIDIA control panel > 3D Settings > Manage 3D Settings > Program Settings > Select `chrome.exe` > Select `High performance NVIDIA processor` > Apply

### AMD
Open Radeon Settings > Graphics or System > Switchable Graphics / Graphics Settings > Select `chrome.exe` > Set the profile to High-Performance > Apply

### Intel ARC
Open Intel Graphics Command Center > System > Graphics > Power or App Preferences > Select `chrome.exe` > Set the profile to High-Performance > Apply

### Finally
Naviagte to `chrome://flags/` in your chrome browser and enable the following:
Force High Performance GPU > Enabled
GPU Rasterization > Enabled
Override software rendering list > Enabled

## Start a local HTTP server to serve 3D tiles:
`npm install http-server`
`https-server "Z:\DataFromSkyline\Cesium" -p 8080 --cors`

## Start a local HTTP server to run Cesium:
Python 3.x
`python -m http.server 8000`

Open a browser and navigate to: http://localhost:8000/

