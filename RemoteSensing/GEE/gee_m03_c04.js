//1. Redução de Coleção de Imagens

var L5 = ee.ImageCollection("LANDSAT/LT05/C02/T1")
        .filterDate('2008-01-01', '2008-12-31')
        .filter(ee.Filter.eq('WRS_PATH', 216))
        .filter(ee.Filter.eq('WRS_ROW', 66));
        
var median = L5.reduce(ee.Reducer.median());

var vis_paramns = {
  bands: ['B4_median', 'B3_median', 'B2_median'],
  gamma: 1.6
}

//Map.setCenter(-38.3605, -8.6091, 9);

//Map.addLayer(median, vis_paramns);

//2. Estatísticas de uma região de imagens

var image = ee.ImageCollection('LANDSAT/LC08/C02/T1_L2').filterDate('2000-01-01', '2018-12-31').first();

var tropical = ee.Feature(ee.FeatureCollection("RESOLVE/ECOREGIONS/2017")
                    .filter(ee.Filter.eq('ECO_ID', 491))
                    .first());
                    
// Map.addLayer(tropical);


//3. Estatísticas de uma Vizinhança de Imagens

var meanL8 = image.reduceRegion({
  reducer: ee.Reducer.mean(),
  geometry: tropical.geometry(),
  scale: 30,
  maxPixels: 1e9
});

print(meanL8)

var redwoods = ee.Geometry.Rectangle(-124.0665, 41.0739, -123.934, 41.2029);

var naipCollection  = ee.ImageCollection('USDA/NAIP/DOQQ')
                        .filterDate('2012-01-01', '2012-12-31');


var naip = naipCollection.mosaic()
var naipNdvi = naip.normalizedDifference(['N', 'R']);

var texture = naipNdvi.reduceNeighborhood({
  reducer: ee.Reducer.stdDev(),
  kernel: ee.Kernel.circle(7)
}); // Estatisticaa de vizinhancas

//Map.addLayer(redwoods);
//Map.addLayer(naip, {}, 'naip');
//Map.addLayer(naipNdvi, {min:-1, max:1, palette: ['FF0000', "00FF00"]}, 'NDVI');
//Map.addLayer(texture, {min:0, max:0.3}, 'DP do NDVI');



//4. Estatísticas de Tabelas

var aFeatColec = ee.FeatureCollection([
                    ee.Feature(null, {foo:1, weight: 1}),
                    ee.Feature(null, {foo:2, weight: 2}),
                    ee.Feature(null, {foo:3, weight: 3}),
]);

print(aFeatColec.reduceColumns({
  reducer: ee.Reducer.mean(),
  selectors: ['foo'],
  weightSelectors: ['weight']
}))



//5. Regressão Linear


var createBandTime = function(image){
  return image.addBands(image.metadata('system:time_start').divide(1e18));
}

var colection = ee.ImageCollection('NASA/NEX-DCP30_ENSEMBLE_STATS')
                    .filter(ee.Filter.eq('scenario', 'rcp85'))
                    .filterDate(ee.Date('2006-01-01'), ee.Date('2050-01-01'))
                    .map(createBandTime);
                    
var linearFit = colection.select(['system:time_start', 'pr_mean'])
                      .reduce(ee.Reducer.linearFit());
                      
Map.addLayer(linearFit, {min:0, max:[-0.9, 8e-5, 1], bands: ['scale', 'offset', 'scale']}, 'fit')

