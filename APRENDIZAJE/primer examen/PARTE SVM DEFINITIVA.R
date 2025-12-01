#EJERCICIO SVN: JUAN ELIAS LARA SOTO

library(kernlab)

# Datos
X <- matrix(c(1,2,  2,-1,  3,-1,  2,3,  3,-3), byrow=TRUE, ncol=2)
y <- c(+1,-1,-1,+1,-1)

# Entrenamos SVM lineal con C grande
modelo <- ksvm(X, as.factor(y), type="C-svc", C=1e6, kernel="vanilladot", scaled=FALSE)

#Extraer coeficientes y vectores soporte
sv_idx <- SVindex(modelo)
X_sv <- X[sv_idx, , drop=FALSE]
alpha_sv <- as.numeric(coef(modelo)[[1]])   # vector numérico de α * y

cat("Vectores soporte:", sv_idx, "\n")
cat("alpha_sv:", alpha_sv, "\n")

# Cálculo de w usando sweep()
w <- colSums(sweep(X_sv, 1, alpha_sv, "*"))

#Calcular b 
b0 <- b(modelo)

cat("w =", round(w,3), "\n")
cat("b =", round(b0,3), "\n")

#  Ancho del canal
margin <- 2 / sqrt(sum(w^2))
cat("Ancho del canal =", round(margin,3), "\n")

#  Ecuaciones del hiperplano y márgenes
slope <- -w[1]/w[2]
intercept <- -b0/w[2]
intercept_pos <- (1 - b0)/w[2]
intercept_neg <- (-1 - b0)/w[2]
cat("Hiperplano: y =", round(slope,3), "*x +", round(intercept,3), "\n")
cat("Márgenes: y =", round(slope,3), "*x +", round(intercept_pos,3),
    "y y =", round(slope,3), "*x +", round(intercept_neg,3), "\n")

#  Clasificar puntos que no son SV 
no_sv_idx <- setdiff(1:nrow(X), sv_idx)
scores <- as.numeric(X[no_sv_idx, ] %*% w + b0)
pred <- ifelse(scores >= 0, +1, -1)
cat("\nClasificación puntos no SV:\n")
print(data.frame(Punto=no_sv_idx, Score=round(scores,3), Prediccion=pred))

# Dibujo 
plot(X, col=ifelse(y==1,"blue","red"), pch=19,
     xlab="x1", ylab="x2", xlim=c(0,4), ylim=c(-4,4))
text(X[,1]+0.15, X[,2], labels=c("A","B","C","D","E"))
abline(a=intercept, b=slope, lwd=2)
abline(a=intercept_pos, b=slope, lty=2)
abline(a=intercept_neg, b=slope, lty=2)
points(X_sv[,1], X_sv[,2], cex=1.6, lwd=2)
legend("bottomright", c("+1","-1","SV"), col=c("blue","red","black"),
       pch=c(19,19,1), pt.cex=c(1,1,1.6), bty="n")

