// Redutores

var L8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA");

var median = L8.filterDate('2024-01-01', '2024-12-31').median();

var visParamns = {bands: ['B4', 'B3', 'B2'], max: 0.3};

// Map.addLayer(median, visParamns, 'median');

// Classificacao de Hansen Global Forest Change - Banda para corpos hidricos

var hansenImage = ee.Image("UMD/hansen/global_forest_change_2023_v1_11")

var datamask = hansenImage.select('datamask');

var mask = datamask.eq(1);

var maskComposite = median.updateMask(mask);

// Map.addLayer(maskComposite, visParamns, 'mask');

// Composicao de Mosaico

var water = mask.not(); // tudo que e agua agora e 1

water = water.mask(water)

var mosaic = ee.ImageCollection([
              median.visualize(visParamns),
              water.visualize({palette: '000044'}),
              ]).mosaic();

// Map.addLayer(mosaic, {}, 'mosaic')

var NDVI = L8.map(function(image) {
  var cloud = ee.Algorithms.Landsat.simpleCloudScore(image).select('cloud');
  var mask = cloud.lte(20);
  var ndvi = image.normalizedDifference(['B5', 'B4']).rename('NDVI');
  
  return image.addBands(ndvi).updateMask(mask)
});

// Gerar um grafico

var chart = ui.Chart.image.series({
  imageCollection: NDVI.select('NDVI'),
  region: ponto,
  reducer: ee.Reducer.first(),
  scale: 30
}).setOptions({title: 'NDVI over time'});

print(chart)