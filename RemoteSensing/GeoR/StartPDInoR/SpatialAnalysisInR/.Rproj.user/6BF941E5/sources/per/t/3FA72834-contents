# Pacotes
library(raster)
library(rgdal)
library(rgeos)

# Carregar o arquivo raster 

botucatu <- stack("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagem_Cortada/imagem_cortada_com_indices.tif")

# Caregga o arquivo csv com os nomes das bandas

bandas <- read.csv("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagem_Cortada/nomes_bandas.csv", h = T)

#Troca os nomes das bandas no objeto botucatu
names(botucatu) <- bandas[,2]

# Carregar o arquivo shapefile com as amostras coletadas

amostras <- readOGR("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Amostras/Amostras.shp")

View(data.frame(amostras))


# Compor todas essas amostras em uma unica linha por classe
# Transformar todas as areas em um unico poligono, mantendo suas propriedades

unidos_shp <- gUnaryUnion(spgeom = amostras, id = amostras$Classe) 
names(unidos_shp)

# Extrair para amostras de campo. Criar um novo dataframe para nossa analise
# Extrai uma lista com 8 elementos correspondentes a cada classe 
atributos <- raster::extract(x = botucatu, y = unidos_shp)


# Criar um dataframe unico para cada uma das classes com as variaveis que nos temos
# Separar os elementos das listas em dataframes
Agricola <- data.frame(Classe = "Agricola", atributos[[1]])
Agricultura <- data.frame(Classe = "Agricultura", atributos[[2]])
Agua <- data.frame(Classe = "Agua", atributos[[3]])
Area_urbana <- data.frame(Classe = "Area_urbana", atributos[[4]])
Eucalipto <- data.frame(Classe = "Eucalipto", atributos[[5]])
Floresta <- data.frame(Classe = "Floresta", atributos[[6]])
Pastagem <- data.frame(Classe = "Pastagem", atributos[[7]])
Solo_exposto <- data.frame(Classe = "Solo_exposto", atributos[[8]])


# Merge  all dataframes: Amostra final

amostra_geral <- rbind(Agricola, Agricultura, Agua, Area_urbana, Eucalipto, Floresta, Pastagem, Solo_exposto)
View(amostra_geral)

#Salvando a amostra geral 
write.csv(amostra_geral, "/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Amostras/Amostra_classificacao.csv", row.names = F)

