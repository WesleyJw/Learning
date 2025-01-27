// 1. Gráficos de dados matriciais

var data = ee.List([0, 1, 2, 3, 4, 5]);

var chart = ui.Chart.array.values(data, 0, data);

// print(chart)

var chartPanel = ui.Panel(chart);

// Map.add(chartPanel)


// 2. Costruindo Gráficos para imagens

var ecoregions = ee.FeatureCollection('projects/google/charts_feature_example');

//Map.addLayer(ecoregions);

var normClim = ee.ImageCollection("OREGONSTATE/PRISM/Norm91m").toBands();

var chart1 = 
        ui.Chart.image
        .byRegion({
          image: normClim.select('[0-9][0-9]_tmean'),
          regions: ecoregions,
          reducer: ee.Reducer.mean(),
          scale: 500,
          xProperty: 'label'
        })
        .setSeriesNames([
          'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
          ])
        .setChartType('ColumnChart')
        .setOptions({
          title: 'Mean Temperature of Eco Regions',
          hAxis:
            {
              title: 'Ecoregions', titleTextStyle: {italic: false, bold: true}
            },
          vAxis: {
            title: 'Temperature (°C)', titleTextStyle: {italic: false, bold: true}
          },
          colors: [
            '604791', '1d6b99', '38a8a7', '0f8755', '76b349', 'f0af07',
            'e37d05', 'cf513e', '96356f', '724173', '9c4f97', '696969'
            ]
        });
        
print(chart1)     

// 3. Coleção de imagens expressa em gráficos

var florest = ee.FeatureCollection('projects/google/charts_feature_example')
                    .filter(ee.Filter.eq('label', 'Forest'));
                    
var vegIndexes = ee.ImageCollection("MODIS/061/MOD13A1")
                    .filter(ee.Filter.date('2010-01-01', '2020-01-01'))
                    .select(['EVI', 'NDVI']);
                    
var chart2 = 
        ui.Chart.image.series({
          imageCollection: vegIndexes,
          region: florest,
          reducer: ee.Reducer.mean(),
          scale: 500,
          xProperty: 'system:time_start'
        })
        .setSeriesNames(['EVI', 'NDVI'])
        .setOptions({
          title: 'Vegetation Index to Florest Biome',
          hAxis:
            {
              title: 'Data', titleTextStyle: {italic: false, bold: true}
            },
          vAxis: {
            title: 'Vegetation Index', titleTextStyle: {italic: false, bold: true}
          },
          lineWidth: 5,
          colors: [
            '604791', '1d6b99'
            ],
          curveType: 'function'
        });

print(chart2)

// 4. Estilo e configuração de gráficos