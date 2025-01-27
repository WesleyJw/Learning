// Lista no lado cliente //
var retangulo = 
    /* color: #d63000 */
    /* displayProperties: [
      {
        "type": "rectangle"
      }
    ] */
    ee.Geometry.Polygon(
        [[[-37.89591425378765, -8.058843850407118],
          [-37.89591425378765, -8.518166525944759],
          [-37.1735631795689, -8.518166525944759],
          [-37.1735631795689, -8.058843850407118]]], null, false);
var client_list = [];

// Adicionar a elementos a lista //
for(var i = 0; i < 8; i++){
  client_list.push(i + 1)
}

print(client_list)

// Usando recursos do servidor //

var server_list = ee.List.sequence(0, 7);

server_list = server_list.map(function(n){
  return ee.Number(n).add(1)
});

print(server_list)

// Filtros e Mascaras //

var imagens = ee.ImageCollection("LANDSAT/LC08/C02/T1_TOA")

var imagensFiltradas = imagens.filterBounds(retangulo)
                              .filterDate('2024-03-28', '2024-12-31')

Map.addLayer(imagensFiltradas)


// Mascaras //

// Redutores - reduzir varias imagens com resultados medios de media, mediana ou outras estatisticas //

var imagensFiltradas = imagens.filterBounds(retangulo)
                              .filterDate('2024-03-28', '2024-12-31')
                              .reduce('mean');
  
  var stats = imagensFiltradas.reduceRegion({
    reducer: ee.Reducer.mean().combine({
      reducer2: ee.Reducer.stdDev(),
      sharedInputs: true
    }),
    geometry: retangulo,
    scale: 10,
    bestEffort: true
  });
  
  print(stats);
  
  Map.addLayer(imagensFiltradas);
  
  var means = stats.toImage().select('.*_mean');
  var stdsImage = stats.toImage().select('.*_stdDev');

print(means);
print(stdsImage);


// Exportacao //

Export.table.toDrive({
  collection: ee.FeatureCollection([ee.Feature(null, stats)]),
  description: 'Exportando_Dados',
  fileFormat: "CSV"
})





