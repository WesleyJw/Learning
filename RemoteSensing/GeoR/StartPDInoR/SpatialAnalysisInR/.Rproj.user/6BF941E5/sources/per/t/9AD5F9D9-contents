library(tidyverse)
library(reshape2)

# Carregar a amostra geral

amostras <- read.csv("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Amostras/Amostra_classificacao.csv", h = T)


# objetivo 1

#Calcular o espectro de reflectancia medio para cada uma das nossas classes

#Agrupar valores pela classe
media_reflec <- amostras %>% 
    group_by(Classe) %>% 
    summarise_each(mean)


#Mudar posicao da  coluna banda 8: As bandas devem estar em ordem crescente. 
media_reflec <- media_reflec[, c(1:7, 10, 8, 9, 11:14)]


# Calcular a transposta das  bandas espectrais

reflec_t <- t(media_reflec[,2:10])

# Criando cores

cores <- c("red", "yellow", "blue", "pink", "green", "darkgreen", "orange"," brown")

#Comprimento de onda
wave_length = c(490, 560, 660, 705, 740, 770, 850, 1600, 2200)

# Fzer grafico

matplot(x = wave_length, y = reflec_t, type = "l", lwd = "2", lty = 1, 
        xlab = "Comprimento de ondas (nm)", ylab = "Reflectância x10000", 
        ylim = c(0, 8000), col = cores)

legend("top", legend = media_reflec$Classe, lty = 1, col = cores, ncol = 3, lwd = 2)


# Box plot das bandas

#long format
dados_melt <- melt(amostras)

ggplot(data = dados_melt, aes(x = Classe, y = value, fill = Classe)) + 
    geom_boxplot() +
    facet_wrap(~variable, scale = 'free') +
    theme(panel.grid.major = element_line(colour = "#d3d3d3"),
          panel.grid.minor = element_blank(),
          panel.border = element_blank(),
          panel.background = element_blank(),
          text = element_text(family = "serif"),
          axis.title = element_text(face = "bold", size = 12),
          axis.text.x = element_text(colour = "white"),
          axis.text.y = element_text(size = 12),
          axis.line = element_line(size = 1, colour = "black")
          ) + 
    theme(plot.margin = unit(c(1, 1, 1, 1), "lines"))
