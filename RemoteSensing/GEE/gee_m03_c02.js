// Filtros

var s2col = ee.ImageCollection("COPERNICUS/S2_SR")
              .filterDate('2018-01-01', '2019-01-01');

var s2col2 = ee.ImageCollection("COPERNICUS/S2_SR")
              .filter(ee.Filter.calendarRange(172, 242, 'day_of_year'));

var s2col3 = ee.ImageCollection("COPERNICUS/S2_SR")
              .filterBounds(ee.Geometry.Point(-122.1, 37.2));
              

var s2col4 = ee.ImageCollection("COPERNICUS/S2_SR")
              .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGEM', 50));
              

var s2col5 = ee.ImageCollection("COPERNICUS/S2_SR")
              .filterDate('2018-01-01', '2019-01-01')
              .filterBounds(ee.Geometry.Point(-122.1, 37.2))
              .filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGEM', 50));
              
// Reducers

var L8 = ee.ImageCollection("LANDSAT/LC08/C02/T1_RT_TOA")
            .filter(ee.Filter.eq("WRS_PATH", 44))
            .filter(ee.Filter.eq("WRS_ROW", 34))
            .filterDate('2014-01-01', '2015-01-01');

var median = L8.median();

//Map.setCenter(-122.3578, 37.7726, 12)
//Map.addLayer(median, {bands: ['B4', 'B3', 'B2'], max: 0.3}, 'median');

// Mosaicos

var naip2004_2012 = ee.ImageCollection("USDA/NAIP/DOQQ")
                        .filterBounds(ee.Geometry.Point(-71.08841, 42.39823))
                        .filterDate('2004-07-01', '2012-12-31')
                        .select(['R', 'G', 'B']);

var composite = naip2004_2012.max();
Map.setCenter(-71.12532, 42.3712, 12);
Map.addLayer(composite, {}, 'Max Values');

var naip2012 = ee.ImageCollection("USDA/NAIP/DOQQ")
                    .filterBounds(ee.Geometry.Rectangle(-71.17695, 42.35125, -71.08824, 42.40584))
                    .filterDate('2012-01-01', '2012-12-31');

var mosaic = naip2012.mosaic()

Map.addLayer(composite, {}, 'Max Values');
Map.addLayer(mosaic, {}, 'mosaic')