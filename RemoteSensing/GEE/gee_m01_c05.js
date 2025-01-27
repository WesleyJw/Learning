// Utilizando biblioteca de tabelas

//var table = ee.FeatureCollection("FAO/GAUL/2015/level0")
//Map.addLayer(table)

// Enviado arquivos shapefiles (Asset)

var amostrasCitrus = ee.FeatureCollection('projects/ee-marioneijunior/assets/amostras_citricultura')
var amostra1 = amostrasCitrus.filterMetadata('cd_evidenc', 'equals', 12955);

var NOA = ee.ImageCollection("NASA/GIMMS/3GV0");
var MODIS = ee.ImageCollection("MODIS/006/MOD13A2")

Map.addLayer(NOA.median().clip(amostra1), null, 'NOA');
Map.addLayer(MODIS.median().clip(amostra1), null, 'MODIS');


// Criando Coleções

// Recorte e visualização de mapas