# Libraries
library(raster)

## Abrindo a imagem tartada : imagem cortada no script lendo_arquivo_raster

#stack nao carrega na memoria ran
img <- stack("/home/wesley/Documentos/ImagensSatelites/AnaliseCabrobo/Imagem_Cabrobo/imagem_cortada_cabrobo.tif") #ler todas as bandas

#modifica o nome das bandas
names(img) <- c("B02", "B03", "B04", "B05", "B06", "B07", "B11", "B12", "B8A")

plot(img$B8A)


#Calculo dos Indices de Vegetacao

#NDVI
NDVI <- (img$B8A - img$B04)/(img$B8A + img$B04)

img$NDVI <- NDVI


#Plot do indice
plot(NDVI)

#RS: Simple Ratio
img$Simple_ratio <- img$B8A/img$B04

#Plot do indice
plot(img$Simple_ratio)



#EVI: indice de vegetacao melhorado
img$EVI <- (2.5 * (img$B8A - img$B04)/10000)/(img$B8A/10000 + 6 * img$B04/10000 - 7.5 * img$B02/10000 + 1)

#Plot do indice
plot(img$EVI)

#NDWI: indice da diferenca normalizada 
img$NDWI <- (img$B03 - img$B12)/(img$B03 + img$B12)

#Plot do indice
plot(img$NDWI)

# Fazendo grafico de comparacao entre os 4 indices
par(mfrow= c(2,2))

#Em escala de cinza
plot(img$NDVI, col = gray(0:100/100), main = "NDVI")
plot(img$Simple_ratio, col = gray(0:100/100), main = "Simple Ratio")
plot(img$EVI, col = gray(0:100/100), main = "EVI")
plot(img$NDWI, col = gray(0:100/100), main = "NDWI")

#Salvando o arquivo TIF
writeRaster(x = img, filename = "/home/wesley/Documentos/ImagensSatelites/AnaliseCabrobo/Imagem_Cabrobo/imagem_cabrobo_com_indices.tif")

#Salvando os noems das bandas
write.csv(names(img), "/home/wesley/Documentos/ImagensSatelites/AnaliseCabrobo/Imagem_Cabrobo/nomes_bandas.csv")


