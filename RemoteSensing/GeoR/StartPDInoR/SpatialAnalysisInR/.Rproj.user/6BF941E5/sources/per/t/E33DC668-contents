
#packages

library(dplyr)
library(randomForest)
library(e1071)
library(caret)
library(caTools)

# Carregar os arquivos com as amostras

dados <- read.csv("/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Amostras/Amostra_classificacao.csv", h = T)

str(dados)

# Transform class in factor
dados$Classe <- as.factor(dados$Classe)


# Separar as amostras dos dados

# Amostras q serao selecionadas
set.seed(1234)    #Semente geradora de numeros aleatorios
amostras_train <- sample.split(dados$Classe, SplitRatio = .7)   #Separa de acordo com as proporcoes das classses

# Definir dados de treino e validacao

# Train
treino <- dados[amostras_train, ]

# Validacao
validacao  <- dados[amostras_train == F, ]

## Machine Learning: Random Forest
set.seed(1234)

# Random
set.seed(1234)
rf_model <- randomForest(Classe ~ ., data = treino, ntree = 100, mtry = 5, importance = T)

# Importancia das variaveis
varImpPlot(rf_model)

importance(rf_model)

# Support vector machine

set.seed(1234)

svm_model <- svm(Classe ~., kernel = "polynomial", data = treino)


# Validacao dos modelos

pred_rf <- predict(rf_model, validacao)

pred_svm <- predict(svm_model, validacao)


# Matriz de confusao

cm_rf <- confusionMatrix(data = pred_rf, reference = validacao$Classe)
print(cm_rf)

cm_svm <- confusionMatrix(data = pred_svm, reference = validacao$Classe)
print(cm_svm)

# Salvar os modelos

saveRDS(object = rf_model, file = "/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Amostras/random_forest_model.rds")
saveRDS(object = svm_model, file = "/home/wesley/Documentos/ImagensSatelites/MaterialCursoStartPDI/Dados_curso/Imagens_sentinel/Amostras/suport_vector_machine_model.rds")
