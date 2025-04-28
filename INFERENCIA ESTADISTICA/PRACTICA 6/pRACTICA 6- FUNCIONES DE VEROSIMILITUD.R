# PRACTICA 6 - FUNCIONES DE LOG-VEROSIMILITUD
# Autor: Juan Elias Lara Soto

# Librerías
library(testthat)

# -------------------------------
# Funciones de Log-Verosimilitud
# -------------------------------

# Exponencial
logLik_exp <- function(lambda, x) {
  n <- length(x)
  n * log(lambda) - lambda * sum(x)
}

# Normal
logLik_normal <- function(mu, sigma, x) {
  n <- length(x)
  -n/2 * log(2 * pi * sigma^2) - 1/(2 * sigma^2) * sum((x - mu)^2)
}

# Uniforme
logLik_unif <- function(a, b, x) {
  n <- length(x)
  if (any(x < a | x > b)) return(-Inf)
  n * log(1/(b - a))
}

# Bernoulli
logLik_ber <- function(p, x) {
  n <- length(x)
  sum(x) * log(p) + (n - sum(x)) * log(1 - p)
}

# Binomial
logLik_bin <- function(n1, p, x) {
  n2 <- length(x)
  sum(lchoose(n1, x) + x * log(p) + (n1 - x) * log(1 - p))
}

# Geométrica
logLik_geom <- function(p, x) {
  n <- length(x)
  n * log(p) + sum(x - 1) * log(1 - p)
}

# Poisson
logLik_poiss <- function(lambda, x) {
  n <- length(x)
  -n * lambda + sum(x) * log(lambda) - sum(lfactorial(x))
}

# Gamma
logLik_gamma <- function(alpha, beta, x) {
  n <- length(x)
  n * (alpha * log(beta) - lgamma(alpha)) + (alpha - 1) * sum(log(x)) - beta * sum(x)
}

# Beta
logLik_beta <- function(alpha, beta, x) {
  n <- length(x)
  if (any(x < 0 | x > 1)) return(-Inf)
  n * (lgamma(alpha + beta) - lgamma(alpha) - lgamma(beta)) + 
    (alpha - 1) * sum(log(x)) + (beta - 1) * sum(log(1 - x))
}

# Chi-cuadrado
logLik_chi2 <- function(k, x) {
  n <- length(x)
  n * (-k/2 * log(2) - lgamma(k/2)) + (k/2 - 1) * sum(log(x)) - sum(x)/2
}

# -------------------------------
# Pruebas unitarias
# -------------------------------

test_that("logLik_exp calcula un número finito", {
  x <- rexp(30, 1)
  expect_true(is.finite(logLik_exp(1, x)))
})

test_that("logLik_normal calcula un número finito", {
  x <- rnorm(30, 10, 3)
  expect_true(is.finite(logLik_normal(10, 3, x)))
})

test_that("logLik_unif calcula correctamente", {
  x <- runif(30, 2, 9)
  expect_true(is.finite(logLik_unif(2, 9, x)))
})

test_that("logLik_ber calcula correctamente", {
  x <- rbinom(30, 1, 0.7)
  expect_true(is.finite(logLik_ber(0.7, x)))
})

test_that("logLik_bin calcula correctamente", {
  x <- rbinom(30, 10, 0.3)
  expect_true(is.finite(logLik_bin(10, 0.3, x)))
})

test_that("logLik_geom calcula correctamente", {
  x <- rgeom(30, 0.3) + 1
  expect_true(is.finite(logLik_geom(0.3, x)))
})

test_that("logLik_poiss calcula correctamente", {
  x <- rpois(30, 3)
  expect_true(is.finite(logLik_poiss(3, x)))
})

test_that("logLik_gamma calcula correctamente", {
  x <- rgamma(30, 2, 1)
  expect_true(is.finite(logLik_gamma(2, 1, x)))
})

test_that("logLik_beta calcula correctamente", {
  x <- rbeta(30, 2, 5)
  expect_true(is.finite(logLik_beta(2, 5, x)))
})

test_that("logLik_chi2 calcula correctamente", {
  x <- rchisq(30, 5)
  expect_true(is.finite(logLik_chi2(5, x)))
})

# -------------------------------
# Ejemplos de comparación de log-verosimilitudes
# -------------------------------

# Datos normales
n <- 30
mu <- 10
sigma <- 3
x <- rnorm(n, mean = mu, sd = sigma)

logLik_normal(mu = mu, sigma = sigma, x)  # debería ser mayor
logLik_exp(lambda = mu, x)

# Datos exponenciales
lambda <- 10
x <- rexp(n, rate = lambda)

logLik_normal(mu = mu, sigma = sigma, x)
logLik_exp(lambda = mu, x)  # debería ser mayor

# Datos normales otra vez
x <- rnorm(n, mean = mu, sd = sigma)
logLik_normal(mu = mu, sigma = sigma, x)
logLik_exp(lambda = mu, x)
logLik_unif(a = min(x), b = max(x), x)
logLik_poiss(lambda = mean(x), x)

# Datos exponenciales
lambda <- 0.5
x <- rexp(n, rate = lambda)
logLik_exp(lambda = lambda, x)
logLik_normal(mu = mean(x), sigma = sd(x), x)
logLik_unif(a = min(x), b = max(x), x)
logLik_poiss(lambda = mean(x), x)

# Datos Poisson
lambda <- 3
x <- rpois(n, lambda)
logLik_poiss(lambda = lambda, x)
logLik_normal(mu = mean(x), sigma = sd(x), x)
logLik_bin(n1 = max(x)+5, p = mean(x)/(max(x)+5), x)

# Datos uniformes
a <- 0
b <- 5
x <- runif(n, min = a, max = b)
logLik_unif(a = a, b = b, x)
logLik_normal(mu = mean(x), sigma = sd(x), x)
logLik_exp(lambda = 1/mean(x), x)

# Datos Bernoulli
p <- 0.7
x <- rbinom(n, size = 1, prob = p)
logLik_ber(p = p, x)
logLik_bin(n1 = 1, p = p, x)  # en Bernoulli, n1 = 1
logLik_poiss(lambda = mean(x), x)

