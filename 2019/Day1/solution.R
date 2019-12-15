# Load data
dat <- read.table("./data.txt")[[1]]

# ------------------------------ Part I ------------------------------ #
getFuel <- function(mass) {
  return(floor(mass / 3) - 2)
}
(total_fuel <- sum(sapply(dat, getFuel)))

# ------------------------------ Part II ------------------------------ #
getFuel2 <- function(mass) {
  if (getFuel(mass) <= 0) {
    return(mass)
  } else {
    return(mass + getFuel2(getFuel(mass)))
  }
}
(total_fuel2 <- sum(sapply(dat, function(x) {getFuel2(x) - x})))