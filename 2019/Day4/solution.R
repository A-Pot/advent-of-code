# Given this range
min_input <- 372037
max_input <- 905157

# ------------------------------ Part I ------------------------------ #

# 1) & 2) Generate all (six-digit) numbers in this range
possibilities <- min_input:max_input

# 3) Two adjacent digits are the same
adjacent_digits <- grepl(paste0(0:9,"{2}", collapse = "|"), possibilities)

# 4) Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)
# If the sorted string version of the number equals itself, it meets this criterion
nondecrease_digits <- sapply(possibilities, function(x) {
  char_num <- strsplit(as.character(x), split = "")[[1]]
  return(all(sort(char_num) == char_num))
})

# Answer - Number of codes meeting the criteria
length(possibilities[adjacent_digits & nondecrease_digits])

# ------------------------------ Part II ------------------------------ #

# Additional rule: the two adjacent matching digits are not part of a larger group of matching digits.

# Start with the set of possiblities from the previous part
possibilities2 <- possibilities[adjacent_digits & nondecrease_digits]

# Tabulate the number of digits in each number, and increment counter if a double is present
sum <- 0
for (p in possibilities2) {
  char_num <- strsplit(as.character(p), "")[[1]]
  if (2 %in% table(char_num)) {
    sum <- sum + 1
  }
}
sum
