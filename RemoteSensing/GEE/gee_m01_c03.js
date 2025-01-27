/* Compara dois momentos iniciale final para avaliar o nível de antropização */

var area_indigena = /* color: #009999 */geometry2;
          
          
var colLandSat8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA").filterDate("2013-05-01", "2024-12-31");

// Centralizar o mapa para uma latitude e longitude com um zoom.

//Map.setCenter(-38.56447400877353, -9.145455645279581, 10)

// Adionar imagens ao mapa

// Map.addLayer(colLandSat8)

var vizParams = {
  bands: ["B5", "B4", "B3"],
  min: 0,
  max: 0.5,
  gamma: [0.95, 1.1, 1]
}

var landSat8 = ee.Image("LANDSAT/LC08/C02/T1_TOA/LC08_216066_20151121");


Map.addLayer(landSat8.clip(area_indigena), vizParams, 'false color composite')