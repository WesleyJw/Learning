// Lista de numeros

var listaNumeros = [0, 1, 2, 3, 4, 5];

print(listaNumeros)

var objeto = {
  tipo: 'Carro',
  modelo: 'sedan',
  ano_disponivel: [2016, 2017, 2018]
}

print(objeto.ano_disponivel[1])

var sequence = ee.List.sequence(1, 5)

var value = sequence.get(4)

print(sequence.get(0))

// Adicionar valor em metodos do servidor
print(ee.Number(value).add(2))

// Criar Dicionario no GEE

var dict = ee.Dictionary({
  e: Math.E,
  pi: Math.PI,
  phi: (1 + Math.sqrt(5))/2,
  my_number: 21
})

print("Euler", dict.get('e'));
print('my_number', dict.my_number);

var data = ee.Date(2021-12-31);

var now = ee.Date(Date.now());
print(now);

var aData = ee.Date.fromYMD(2017, 1, 15);

var theDate = ee.Date.fromYMD({
  day: 13,
  month: 1,
  year: 2017
  });
  
print(aData);
print(theDate);

// Uso do map

var my_list = ee.List.sequence(1, 10);

var quadrado = function(number) {
  return ee.Number(number).pow(2);
};

print(my_list.map(quadrado))

var getOddNumbers = function(number) {
  number = ee.Number(number);
  var remainder = number.mod(2);
  return number.multiply(remainder);
};

var newList = my_list.map(getOddNumbers);

var oddNumber = newList.removeAll([0]);

var oddSquare = oddNumber.map(quadrado)
print(oddSquare)

var collection = ee.ImageCollection('LANDSAT/LC08/C02/T1_TOA');

var subset1 = collection.filter(ee.Filter.lt('SUN_ELEVATION', 40));
var subset2 = collection.filter(ee.Filter.gte('SUN_ELEVATION', 40));

var processed1 = subset1.map(function(image){
  return image.multiply(2);
});

var processed2 = subset2.map(function(image){
  return image.multiply(1);
});

var final = processed1.merge(processed2);

print(final.size());

// Sequence de Fibonacci

var algorithm = function(current, previous) {
  previous = ee.List(previous);
  var n1 = ee.Number(previous.get(-1));
  var n2 = ee.Number(previous.get(-2));
  
  return previous.add(n1.add(n2));
};

var numInteration = ee.List.repeat(1, 10);
var start = [0, 1];
var sequence = numInteration.iterate(algorithm, start);
print(sequence);