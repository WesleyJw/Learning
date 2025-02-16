#Ler arquivo raster
library(raster)
library(rgdal)
library(sp)

#ler uma banda 
banda_5 <- raster("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Imagem_Bruta/T22KGV_20210104T132231_B05_20m.jp2")


#Plotar um grafico
plot(banda_5)

# Plotar com niveis de cinza
plot(banda_5, col = gray(0:100/100))

#remove banda 5
rm(banda_5)

# Composicao colorida: Criar uma Stack

#Pegar os nomes dos arquivos
arquivos <- list.files(path = "/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Imagem_Bruta/",
                       pattern="_B", full.names = T)

all_bands <- stack(arquivos)

#plot em composicao colorida

#cor verdadeira
plotRGB(all_bands, r = 3, g = 2, b = 1, axes = T, stretch = 'lin', main = "Sentinel 2 cor verdadeira")

#Composicao falsa cor: utilizando a banda_8 "proximo do vermelho" no red informar a posicao da banda
plotRGB(all_bands, r = 9, g = 2, b = 1, axes = T, stretch = 'lin', main = "Sentinel 2 falsa cor")

# Dar Zoom na imagem
croped = crop(all_bands, extent(780000, 800000, 7470000, 7480000))

# plotar
plotRGB(croped, r = 9, g = 2, b = 1, axes = T, stretch = 'lin', main = "Sentinel 2 falsa cor")


## Como abrir um arquivo Shapefile

#carregando as imagens
arquivos <- list.files(path = "/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Imagem_Bruta/",
                       pattern="_B", full.names = T)

img <- stack(arquivos)

#Carregar o Shapefile
botucatu <- readOGR("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Shapefiles_classificacao/MunicipioBotucatu/Botucatu.shp")
plot(botucatu, usePolypath = FALSE)

#Verificar o sistema de coordenadas da imagem e do shape

# Coordenada da Imagem
crs(img) #output: +proj=utm +zone=22 +south +datum=WGS84 +units=m +no_defs 

# Coordenada do shape
crs(botucatu) #output: +proj=longlat +datum=WGS84 +no_defs 

#Transfomando coordenada de longlat para utm
botucatu_utm <- spTransform(x = botucatu, CRSobj = crs(img)) #ou colocar: "+proj=utm +zone=22 +south +datum=WGS84 +units=m +no_defs" 

# Verificando novamente o sistema de coordenadas
crs(botucatu_utm)

#### Recortar para a area do Municipio

# Usando a funcao mascara
botucatu_mask <- mask(x = img, mask = botucatu_utm)

#Usando a funcao crop
botucatu_crop <- crop(botucatu_mask, botucatu_utm)

#Plotando o grafico

par(mfrow = c(1, 2))
plot(botucatu_mask$T22KGV_20210104T132231_B8A_20m) # O mask corta a imagem para os limites do municipio, mas nao corta os limites dos eixos do mapa
plot(botucatu_crop$T22KGV_20210104T132231_B8A_20m) # Com crop é possível cortar os limites do eixo do municipio

names(botucatu_crop)

# Salvar arquivo no formato tiff

writeRaster(x = botucatu_crop, filename = "/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagem_Cortada/imagem_cortada.tif")
