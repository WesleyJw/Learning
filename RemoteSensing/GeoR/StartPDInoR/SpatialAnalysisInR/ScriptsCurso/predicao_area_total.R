#packages

library(randomForest)
library(e1071)
library(caret)
library(raster)
library(prettymapr)

# Carregar os modelos

rf_model <- readRDS("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Amostras/random_forest_model.rds")
svm_model <- readRDS("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Amostras/suport_vector_machine_model.rds")


## Carregar o tif com os nomes das variaveis

img = stack("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagem_Cortada/imagem_cortada_com_indices.tif")

bandas <- read.csv("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagem_Cortada/nomes_bandas.csv")


names(img) <- bandas[, 2]

## Predicao para o raster

#Random forest
rf_raster <- predict(img, rf_model)

#Support vector machine
svm_raster <- predict(img, svm_model)

## Plot para predicao do random forest

cores <- c("red", "yellow", "blue", "pink", "green", "darkgreen", "orange"," brown")

classes <- c("Agrícola", "Agricultura", "Água", "Area Urbana", "Eucalipto", "Floresta", "Pastagem", "Solo Exposto")

pdf(file = "/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagem_Cortada/random_forest_classification.pdf",
     width = 15, height = 15)

plot(rf_raster, legend = F, col = cores, main = "Random Forest Classification \n Botucatu-SP",
     cex.axis = 1.5, cex.main = 1.5)

legend("topleft", legend = classes, fill = cores, border = F, cex = 1.3)

addscalebar()
addnortharrow(cols = c("black", "black"), scale = 0.755)
dev.off()

# Sanvando os tiff's classificados

writeRaster(rf_raster, "/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagem_Cortada/imagem_classificada_radom_forest.tif")
writeRaster(svm_raster, "/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagem_Cortada/imagem_classificada_support_vector.tif")


