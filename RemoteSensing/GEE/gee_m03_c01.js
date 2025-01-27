// Pegar imagem de Reflectância do Sentinel - 2

var sentCol1 = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
                  .filterBounds(ee.Geometry.Point(-70.48, 43631))
                  .filterDate('2024-01-01', '2024-12-31')
                  .sort('CLOUDY_PIXEL_PERCENTAGE')
                  .first();

Map.centerObject(sentCol1)

// Composicao RGB

//Map.addLayer(sentCol1, {bands: ['B4', 'B3', 'B2'], min: 0, max: 2000}, 'Camada 1')


var img = ee.Image("COPERNICUS/S2_SR_HARMONIZED/20240816T170849_20240816T170851_T19WDU");

var paramnsVis = {
  bands: ['B4', 'B3', 'B2'],
  min: 0,
  max: 0.5,
  gamma: [0.95, 1.1, 1]
};

//Map.setCenter(-122.1899, 37.5010, 10);
//Map.addLayer(img, paramnsVis, 'True color');

var img = ee.Image('LANDSAT/LC08/C02/T1_RT_TOA/LC08_044034_20130721');


var ndwi = img.normalizedDifference(['B3', 'B5']);
var ndwiViz = {min:0.5, max:1, palette: ['00FFFF', '0000FF']};

//Map.addLayer(ndwi, ndwiViz, 'NDWI')

// Printar metadados

// print("Metadados", img)


var bandNames = img.bandNames()

//print("Band Names: ", bandNames)

/****************************************************/
/* 
Operacoes matematicas com:

- Soma: add()
- Subtracao: subtract()
- Multiplicacao: multiply()
- Divisao: divide()
- Expresoes: expression()
*/

var landSatImg = ee.Image('LANDSAT/LC08/C02/T1_RT_TOA/LC08_044034_20130721');

var ndvi2013 = landSatImg.select('B4')
                .subtract(landSatImg.select('B3'))
                .divide(landSatImg.select('B4').add(landSatImg.select('B3')));
                
// Map.addLayer(ndvi2013)


var evi = landSatImg.expression(
  '2.5 * ((NIR - RED)/(NIR + 6 * RED - 7.5 * BLUE + 1))', 
  {
    'NIR': landSatImg.select('B5'),
    'RED': landSatImg.select('B4'),
    'BLUE': landSatImg.select('B2')
  }
  );
  
//Map.centerObject(landSatImg, 9);
//Map.addLayer(evi, {min: -1, max: 1, palette: ['FF0000', '00FF00']});


// Operadores Relacionais

var nl2012 = ee.Image("NOAA/DMSP-OLS/NIGHTTIME_LIGHTS/F182012");

//ee.Image("NOAA/DMSP-OLS/CALIBRATED_LIGHTS_V4/F12-F15_20000103-20001229_V4")

var lights = nl2012.select('stable_lights');

var zones = lights.gt(30).add(lights.gt(55)).add(lights.gt(62));

var palette = ['000000', '0000FF', 'FF0000'];

//Map.setCenter(-39.3107690478887, -8.505542629923445, 10);
//Map.addLayer(zones, {min: 0, max: 3, palette:palette}, 'Urban Zones');

// Operaces Morfologicas

var image = ee.Image('LANDSAT/LC08/C02/T1_RT_TOA/LC08_044034_20130721')
                .select(4).gt(0.2);

//Map.setCenter(-122.1899, 37.5010, 13)
//Map.addLayer(image, {}, 'NIR')

var kernel = ee.Kernel.circle({radius: 1});

var opened = image
              .focal_min({kernel: kernel, iterations: 2})
              .focal_max({kernel: kernel, iterations: 2 });
              
//Map.addLayer(opened, {}, 'abertura')

// Transformacoes espectrais

var bands = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']

var image = ee.Image('LANDSAT/LC08/C02/T1/LC08_044034_20130721')
                .select(bands);
                
Map.setCenter(-122.1899, 37.5010, 13)
Map.addLayer(image, {bands: ['B4', 'B3', 'B2'], min: 0, max: 128}, 'image')

var urban = [88, 45, 48, 38, 86, 115,59]
var veg = [50, 21, 20, 35, 50, 110, 23]
var water = [51, 20, 14, 9, 7, 116, 4]

// Unmix

var fractions = image.unmix([urban, veg, water]);

Map.addLayer(fractions, {}, 'unmixed');