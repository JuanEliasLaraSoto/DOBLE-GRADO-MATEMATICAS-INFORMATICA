#JUAN ELIAS LARA SOTO
#DOBLE GRADO MATEMATICAS E INGENIERIA INFORMATICA
# PROBLEMA 2

library(rpart.plot)
library(rpart)
library(e1071)
library(adabag)

set.seed(1234)

#1) PREPROCESAMIENTO DE iris



data(iris)

iris2 <- subset(iris, Species %in% c("versicolor", "virginica"))

iris2$Species <- factor(iris2$Species)

iris2$y <- ifelse(iris2$Species == "versicolor", 1, -1)

x_features <- iris2[, 1:4]


# 2) ENTRENAR CLASIFICADOR BOOSTING (árboles) CON CV


n <- nrow(iris2)
ind <- sample(n, n)
n_test <- floor(0.3 * n)
idx_test <- ind[1:n_test]

dtest_boost  <- iris2[idx_test, ]
dtrain_boost <- iris2[-idx_test, ]

modelo_boost <- boosting(
  Species ~ .,
  data = dtrain_boost[, c(colnames(iris2)[1:4], "Species")],
  mfinal = 10,
  boos   = TRUE,
  control = rpart.control(maxdepth = 1)
)



# 3) PREDICCIÓN EN TEST, ACCURACY, PESOS Y ÁRBOL


pred_boost <- predict(modelo_boost,
                      newdata = dtest_boost[, c(colnames(iris2)[1:4], "Species")])

mc_boost <- table(pred_boost$class, dtest_boost$Species,
                  dnn = c("Pred_Boost", "Real"))
accuracy_boost <- sum(diag(mc_boost)) / sum(mc_boost)

cat("Accuracy del modelo boosting (árboles) en test:",
    accuracy_boost, "\n")
print(mc_boost)

cat("Pesos de las instancias (weights) en el modelo boosting:\n")
print(modelo_boost$weights)

arbol1 <- modelo_boost$trees[[1]]
rpart.plot(arbol1, type = 4, extra = 101, under = TRUE, faclen = 0, cex = 1)




# 4) ENSEMBLE CON SVM (VARIANTE AdaBoost.M1)


X <- as.matrix(x_features)
y_num <- iris2$y  # -1 o 1

nSVM <- 10
listaSVM <- list()

for (m in 1:nSVM) {
  idx_train_svm <- sample(nrow(X), floor(0.7 * nrow(X)))
  
  X_train_svm <- X[idx_train_svm, ]
  y_train_svm <- y_num[idx_train_svm]
  
  y_train_factor <- factor(
    ifelse(y_train_svm == 1, "versicolor", "virginica"),
    levels = c("virginica", "versicolor")
  )
  
  datos_svm <- data.frame(X_train_svm, Species = y_train_factor)
  
  svm_m <- svm(
    Species ~ .,
    data   = datos_svm,
    kernel = "linear",
    cost   = 0.1,
    scale  = FALSE
  )
  
  listaSVM[[m]] <- svm_m
}


#5) PREDICCIÓN DEL ENSEMBLE SVM USANDO alpha, test1 y test2


#Prediccion EN test1

pred_matrix_test1 <- sapply(listaSVM, function(mod) {
  pred_factor <- predict(mod, newdata = as.data.frame(test1))
  # Pasamos de factor ("versicolor"/"virginica") a {-1,1}
  ifelse(pred_factor == "versicolor", 1, -1)
})


score_test1 <- as.vector(pred_matrix_test1 %*% alpha)

y_pred_test1 <- ifelse(score_test1 >= 0, 1, -1)

cat("Predicción final del ensemble SVM para test1:\n")
print(y_pred_test1)

#Prediccion EN test2

pred_matrix_test2 <- sapply(listaSVM, function(mod) {
  pred_factor <- predict(mod, newdata = as.data.frame(test2))
  ifelse(pred_factor == "versicolor", 1, -1)
})

score_test2 <- as.vector(pred_matrix_test2 %*% alpha)
y_pred_test2 <- ifelse(score_test2 >= 0, 1, -1)

cat("Predicción final del ensemble SVM para test2:\n")
print(y_pred_test2)


# 6)  
# Comentario:
# - En el primer boosting (árboles) se ha usado AdaBoost.M1 clásico
#   con 10 clasificadores débiles rpart de baja profundidad. Se ha
#   separado iris2 en train/test y se ha calculado el accuracy sobre
#   el test, además de mostrar los pesos de instancia y el primer árbol.
# - En la variante con SVM, se han entrenado 10 SVM lineales con
#   subconjuntos de entrenamiento distintos. La combinación final se ha
#   hecho como en AdaBoost.M1, usando un vector de pesos alpha
#   proporcionado en el fichero del problema:
#     F(x) = sign( sum_t alpha_t * h_t(x) )
#- Se ha supuesto que el fichero proporcionado por el profesor carga
#   en el entorno los objetos alpha, test1 y test2, con formato
#   compatible con las características de iris (4 atributos numéricos).

