logLik_normal <- function(mu, sigma, x) {
  sum(dnorm(x, mean = mu, sd = sigma, log = TRUE))
}
