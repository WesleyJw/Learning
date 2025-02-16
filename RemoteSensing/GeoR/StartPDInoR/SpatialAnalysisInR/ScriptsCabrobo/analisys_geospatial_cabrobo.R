library(raster)
library(rgdal)
library(sp)
library(tidyverse)

# carregar a banda  5
banda_5 <- raster("/home/wesley/Documentos/ImagensSatelites/AnaliseCabrobo/Imagem_Bruta/T24LVR_20211229T130249_B05_20m.jp2")

# plotar o grafico
plot(banda_5)

# Plotar com niveis de cinza
plot(banda_5, col = gray(0:100/100))


# Plot com cor verdadeira
arquivos <- list.files(path = "/home/wesley/Documentos/ImagensSatelites/AnaliseCabrobo/Imagem_Bruta/",
                       pattern="_B", full.names = T)

img <- stack(arquivos)

#cor verdadeira
plotRGB(img, r = 3, g = 2, b = 1, axes = T, stretch = 'lin', main = "Sentinel 2 cor verdadeira")

#Composicao falsa cor: utilizando a banda_8 "proximo do vermelho" no red informar a posicao da banda
plotRGB(img, r = 9, g = 2, b = 1, axes = T, stretch = 'lin', main = "Sentinel 2 falsa cor")

# Visualizar o curso d'agua
# Dar Zoom na imagem
croped = crop(img, extent(427410, 482310, 9040100, 9072550))

par(oma=c(1.5,2,1.5,0))

# plotar
plotRGB(croped, r = 9, g = 2, b = 1, axes = T, stretch = 'lin', main = "Sentinel 2 falsa cor")

# Ler os dados dos Municipios de PE

municipios <- readOGR("/home/wesley/Documentos/ImagensSatelites/AnaliseCabrobo/MunicipiosPE/PE_Municipios_2021.shp")

#transformar para um data frame
pe_dados <- slot(object=municipios, name="data");

#encontrar codigo do municipio
cod_cabrobo <- pe_dados[pe_dados$NM_MUN == "Cabrobó",]$CD_MUN


#Separar Shape de Cabrobo
cabrobo <- municipios[municipios$CD_MUN == cod_cabrobo,]

#Grafico do municipio
plot(cabrobo, usePolypath = FALSE)

# Coordenadas da Imagem e do mapa
crs(cabrobo)
crs(img)

#Transfomando coordenada de longlat para utm
cabrobo_utm <- spTransform(x = cabrobo, CRSobj = crs(img)) #ou colocar: "+proj=utm +zone=22 +south +datum=WGS84 +units=m +no_defs" 

# Verificando novamente o sistema de coordenadas
crs(cabrobo_utm)

#### Recortar para a area do Municipio

# Usando a funcao mascara
cabrobo_mask <- mask(x = img, mask = cabrobo_utm)

#Usando a funcao crop
cabrobo_crop <- crop(cabrobo_mask, cabrobo_utm)
names(cabrobo_crop)

#Plotando o grafico

par(mfrow = c(1, 2))
plot(cabrobo_mask$T24LVR_20211229T130249_B8A_20m) # O mask corta a imagem para os limites do municipio, mas nao corta os limites dos eixos do mapa
plot(cabrobo_crop$T24LVR_20211229T130249_B8A_20m) # Com crop é possível cortar os limites do eixo do municipio

# Salvar arquivo no formato tiff

writeRaster(x = cabrobo_crop, filename = "/home/wesley/Documentos/ImagensSatelites/AnaliseCabrobo/Imagem_Cabrobo/imagem_cortada_cabrobo.tif")

