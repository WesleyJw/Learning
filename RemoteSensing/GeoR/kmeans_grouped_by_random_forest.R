#install.packages("terra", dependencies = T)
library(terra)
library(cluster)
library(ClusterR)
library(raster)

# import raster

iris1 <- iris[, -5]
head(iris1)

set.seed(123)

kmenas_r <- kmeans(iris1, centers = 3, nstart = 20)
cm <- table(iris$Species, kmenas_r$cluster)


plot(iris1[c('Sepal.Length', 'Petal.Width')], col = kmenas_r$cluster)

clusplot(iris1[c('Sepal.Length', 'Petal.Width')],
    kmenas_r$cluster,
    lines = 0,
    shade = TRUE,
    color = TRUE,
    labels = 2,
    plotchar = FALSE,
    span = TRUE,
    main = "Cluster Iris")


library(factoextra)

# NUmero Otimo de cluster
gap <- clusGap(iris1,
            FUN=kmeans,
            nstar = 25,
            K.max = 10,
            B = 50)

fviz_gap_stat(gap)

# Kmeans com Random Forest

imagem <- stack("minha_imagem.tif")
plotRGB(imagem, r=3, g=2,  b = 1)

kmenas_2 <- kmeans(imagem[], 4)
res <- raster(imagem[[1]])
res <- setValues(res, kmenas_2$cluster)
plot(res)

library(randomForest)
valores <- getValues(imagem)
index <- which(!is.na(valores))
valores <- na.omit(valores)

res_rf <- clara(valores, k=4, samples = 500, metric = "manhattan", pamLike = TRUE)
imagemClara <- raster(imagem)
imagemClara[index] <- res_rf$clustering
plot(imagemClara)

imagemAmostra <- valroes[sample(nrow(valores), 500),]
rf <- randomForest(imagemAmostra)
rf_prox <- randomForest(imagemAmostra, ntree = 100, proximity = TRUE)$proximity

E_rf <- kmeans(rf_prox, 4)
rf <- randomForest(imagemAmostra, as.factor(E_rf$cluster), ntree = 100)
rf_faster <- predict(imagem, rf)

plot(rf_faster)