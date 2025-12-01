# Árbol de decisión RPART - JUAN ELIAS LARA SOTO


library(rpart)
library(rpart.plot)
library(caret)
library(dplyr)
library(pROC)

# 1. CARGAMOS DATOS 
german <- read.csv("GermanCredit.csv", header = TRUE, sep = ",")

# 2. SELECCIONAMOS LAS VARIABLES INDICADAS EN EL ENUNCIADO 
german_subset <- german %>%
  select(
    Age,
    Job.Management.SelfEmp.HighlyQualified,
    Housing.Rent,
    Housing.ForFree,
    Housing.Own,
    SavingsAccountBonds.500.to.1000,
    CheckingAccountStatus.lt.0,
    CheckingAccountStatus.0.to.200,
    Amount,
    Duration,
    Purpose.NewCar,
    Class
  )

# Convertimos variables a factor (si son de texto)
german_subset <- german_subset %>%
  mutate(across(where(is.character), as.factor),
         Class = as.factor(Class))

# 3. DIVISIÓN 70% ENTRENAMIENTO / 30% TEST 
set.seed(123)
trainIndex <- createDataPartition(german_subset$Class, p = 0.7, list = FALSE)
trainData <- german_subset[trainIndex, ]
testData  <- german_subset[-trainIndex, ]

cat("Tamaño entrenamiento:", nrow(trainData), " - Tamaño test:", nrow(testData), "\n")

# 4. ENTRENAMIENTO RPART 
modelo_rpart <- rpart(
  Class ~ .,
  data = trainData,
  method = "class",
  control = rpart.control(cp = 0.001)
)

# Tabla y curva de complejidad
printcp(modelo_rpart)
plotcp(modelo_rpart, main = "Curva de error vs cp (entrenamiento)")

# 5. ACCURACY ÁRBOL SIN PODAR 
pred_train <- predict(modelo_rpart, newdata = trainData, type = "class")
pred_test  <- predict(modelo_rpart, newdata = testData, type = "class")

acc_train <- mean(pred_train == trainData$Class)
acc_test  <- mean(pred_test == testData$Class)

cat("Accuracy SIN podar - Train:", round(acc_train, 3), " Test:", round(acc_test, 3), "\n")

# 6. ÁRBOL PODADO (mínimo xerror) 
opt <- which.min(modelo_rpart$cptable[, "xerror"])
cp_minimo <- modelo_rpart$cptable[opt, "CP"]

arbol_podado_min <- prune(modelo_rpart, cp = cp_minimo)

pred_test_min <- predict(arbol_podado_min, newdata = testData, type = "class")
acc_podado_min <- mean(pred_test_min == testData$Class)
cat("Accuracy árbol PODADO (mín xerror):", round(acc_podado_min, 3), "\n")

# 7. ÁRBOL PODADO (regla 1-SE) 
xerror_min <- modelo_rpart$cptable[opt, "xerror"]
xstd_min <- modelo_rpart$cptable[opt, "xstd"]
threshold <- xerror_min + xstd_min
i_1se <- which(modelo_rpart$cptable[, "xerror"] <= threshold)[1]
cp_1se <- modelo_rpart$cptable[i_1se, "CP"]

arbol_podado_1se <- prune(modelo_rpart, cp = cp_1se)

pred_test_1se <- predict(arbol_podado_1se, newdata = testData, type = "class")
acc_podado_1se <- mean(pred_test_1se == testData$Class)
cat("Accuracy árbol PODADO (1-SE):", round(acc_podado_1se, 3), "\n")

# 8. COMPARACIÓN DE RESULTADOS 
resultados <- data.frame(
  Modelo = c("Sin podar", "Podado mín xerror", "Podado 1-SE"),
  Accuracy_Test = c(acc_test, acc_podado_min, acc_podado_1se)
)
print(resultados)

# 9. CURVA ROC Y AUC DEL MEJOR MODELO (mín xerror)
prob_pred <- predict(arbol_podado_min, newdata = testData, type = "prob")[, 2]
roc_obj <- roc(testData$Class, prob_pred)
auc_val <- auc(roc_obj)
cat("AUC (Área bajo la curva) =", round(auc_val, 3), "\n")
plot(roc_obj, main = paste("Curva ROC - AUC =", round(auc_val, 3)))

# 10. VISUALIZACIÓN INDIVIDUAL DE LOS ÁRBOLES 
par(mfrow = c(1, 1))

rpart.plot(modelo_rpart,
           main = "Árbol sin podar",
           extra = 104,
           under = TRUE, faclen = 0)

rpart.plot(arbol_podado_min,
           main = "Árbol podado (mín xerror)",
           extra = 104,
           under = TRUE, faclen = 0)

rpart.plot(arbol_podado_1se,
           main = "Árbol podado (1-SE)",
           extra = 104,
           under = TRUE, faclen = 0)




