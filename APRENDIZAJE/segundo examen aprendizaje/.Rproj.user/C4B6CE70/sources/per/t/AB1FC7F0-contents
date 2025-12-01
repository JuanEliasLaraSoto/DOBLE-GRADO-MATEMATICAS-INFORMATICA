# PROBLEMA 1
#JUAN ELIAS LARA SOTO
#DOBLE GRADO MATEMATICAS E INGENIERIA INFORMATICA

library(nnet)
library(randomForest)
library(rpart)

set.seed(1234)

# Dataset Kyphosis del paquete rpart
data(kyphosis)
datos <- kyphosis
datos$Kyphosis <- as.factor(datos$Kyphosis)

# Partición global train/test (75% train, 25% test)
n <- nrow(datos)
ind <- sample(n, n)
n_test <- floor(0.25 * n)
idx_test <- ind[1:n_test]

dtest_global  <- datos[idx_test, ]
dtrain_global <- datos[-idx_test, ]


#1) ENSEMBLE CON TRES PERCEPTRONES (nnet)


lista_atributos <- list(
  c("Age",    "Number"),
  c("Age",    "Start"),
  c("Number", "Start")
)

numeroPerceptrones <- 3
listaPerceptrones  <- list()
sizes_optimos      <- numeric(numeroPerceptrones)

for (p in 1:numeroPerceptrones) {
  attrs <- lista_atributos[[p]]
  idx_train_p <- sample(n, floor(0.75 * n))
  dtrain_p_global <- datos[idx_train_p, c(attrs, "Kyphosis")]
  mejor_accuracy <- 0
  mejor_size     <- 1
  mejor_modelo   <- NULL
  
  for (sizeN in 1:10) {
    # Validación cruzada sencilla sobre dtrain_global (75/25)
    n_train <- nrow(dtrain_p_global)
    ind_cv  <- sample(n_train, n_train)
    n_cvtest <- floor(0.25 * n_train)
    idx_cvtest <- ind_cv[1:n_cvtest]
    
    dtest_cv  <- dtrain_p_global[idx_cvtest, ]
    dtrain_cv <- dtrain_p_global[-idx_cvtest, ]    
    modelo <- nnet(
      Kyphosis ~ .,
      data  = dtrain_cv,
      size  = sizeN,
      maxit = 500,
      decay = 1,
      trace = FALSE
    )
    
    pred_cv <- predict(modelo, dtest_cv, type = "class")
    mc_cv   <- table(pred_cv, dtest_cv$Kyphosis)
    acc_cv  <- sum(diag(mc_cv)) / sum(mc_cv)
    
    if (acc_cv > mejor_accuracy) {
      mejor_accuracy <- acc_cv
      mejor_size     <- sizeN
      mejor_modelo   <- modelo
    }
  }
  
  sizes_optimos[p]     <- mejor_size
  listaPerceptrones[[p]] <- mejor_modelo
  cat("Perceptrón", p, "con atributos", attrs,
      " -> mejor size =", mejor_size,
      "accuracy CV =", mejor_accuracy, "\n")
}


for (p in 1:numeroPerceptrones) {
  attrs <- lista_atributos[[p]]
  sizeN <- sizes_optimos[p]
  
  dtrain_p <- dtrain_global[, c(attrs, "Kyphosis")]
  
  modelo_p <- nnet(
    Kyphosis ~ .,
    data  = dtrain_p,
    size  = sizeN,
    maxit = 500,
    decay = 1,
    trace = FALSE
  )
  
  listaPerceptrones[[p]] <- modelo_p
}

lista_predicciones <- list()
for (p in 1:numeroPerceptrones) {
  attrs <- lista_atributos[[p]]
  modelo_p <- listaPerceptrones[[p]]
  
  dtest_p <- dtest_global[, c(attrs, "Kyphosis")]
  pred_p  <- predict(modelo_p, dtest_p, type = "class")
  
  lista_predicciones[[p]] <- pred_p
}

predicciones_df <- as.data.frame(do.call(cbind, lista_predicciones))
colnames(predicciones_df) <- paste0("P", 1:numeroPerceptrones)

# Función de moda (voto mayoritario)
calcular_moda <- function(x) {
  tabla <- table(x)
  names(tabla)[which.max(tabla)]
}

voto_mayoritario <- apply(predicciones_df, 1, calcular_moda)
voto_mayoritario <- factor(voto_mayoritario, levels = levels(dtest_global$Kyphosis))

# Matriz de confusión y accuracy del ensemble
mc_ensemble <- table(voto_mayoritario, dtest_global$Kyphosis,
                     dnn = c("Predicción_ensemble", "Real"))
accuracy_ensemble <- sum(diag(mc_ensemble)) / sum(mc_ensemble)

cat("Accuracy del ensemble de perceptrones (test global):",
    accuracy_ensemble, "\n")
print(mc_ensemble)

# 2) COMPARACIÓN CON RANDOM FOREST + IMPORTANCIA VARIABLES


# Entrenamos Random Forest sobre el mismo train_global
rf <- randomForest(
  Kyphosis ~ .,
  data = dtrain_global,
  ntree = 500,
  mtry  = 2,
  importance = TRUE
)

# Predicción en test
pred_rf <- predict(rf, newdata = dtest_global)
mc_rf   <- table(pred_rf, dtest_global$Kyphosis,
                 dnn = c("Pred_RF", "Real"))
accuracy_rf <- sum(diag(mc_rf)) / sum(mc_rf)

cat("Accuracy del Random Forest (test global):",
    accuracy_rf, "\n")
print(mc_rf)

# Importancia de los atributos
cat("Importancia de los atributos en el Random Forest:\n")
print(importance(rf))


# COMENTARIO SOBRE EL DESARROLLO Y LOS RESULTADOS
# Como suposición metodológica, se empleó validación hold-out en 
# lugar de k-fold debido a que el enunciado solicitaba validación 
# pero no imponía un método concreto. Además, se mantuvo fija la 
# partición global de test para poder realizar una comparación 
# justa entre el ensemble de perceptrones y el Random Forest.

# Comparación de Resultados:
# En la comparación final, el Random Forest obtuvo un accuracy mayor 
# que el ensemble de perceptrones, mostrando mayor robustez en la 
# clasificación del conjunto Kyphosis. Este comportamiento era esperable 
# dada la naturaleza del dataset (muy pequeño y con clases desbalanceadas) 
# y la capacidad del RF para manejar relaciones no lineales.

# El ensemble de perceptrones mostró dificultades para identificar la 
# clase minoritaria 'present', mientras que el Random Forest sí logró 
# clasificar correctamente algunas de estas instancias.

# Según las medidas de importancia del Random Forest, el atributo 'Start' 
# resultó ser el más influyente en la predicción, mientras que 'Number' 
# aportó una importancia menor, lo que coincide con su menor relevancia 
# clínica en la determinación de la cifosis postoperatoria.

