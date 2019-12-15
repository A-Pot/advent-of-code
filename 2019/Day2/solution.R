# ------------------------------ Part I ------------------------------ #

# Load data
dat <- readLines("./data.txt")

# Break CSVs into value array
s1 <- as.numeric(strsplit(dat,',')[[1]])

# Before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.
s1[2] <- 12; s1[3] <- 2

# Process one 4-array instruction set
processInstructionSet <- function(x) {
  
  # Perform calculation according to operator
  val <- switch(x[1], 
         # Addition operator
         "1" = {s1[x[4] + 1] <<- s1[x[2] + 1] + s1[x[3] + 1]},
         # Multiplication operator
         "2" = {s1[x[4] + 1] <<- s1[x[2] + 1] * s1[x[3] + 1]},
         # Halt signal
         "99" = {return(NULL)},
         # Invalid operator (default)
         stop(paste("Invalid operator:", x[1]))
         )
}

# Process consecutive sets until halting instructions are encountered
idx <- 0; instruction_set <- 0
while (instruction_set[1] != 99) {
  instruction_set <- s1[1:4 + 4*idx]
  processInstructionSet(instruction_set)
  idx <- idx + 1
}
print(paste("Answer:", s1[1]))
  
# ------------------------------ Part II ------------------------------ #

# Wrap up previous logic in a function of its own that accepts nouns and verbs and returns the answer
calcVal <- function(noun, verb) {
  s1 <<- as.numeric(strsplit(dat,',')[[1]])
  s1[2] <<- noun; s1[3] <<- verb
  
  idx <- 0; instruction_set <- 0
  while (instruction_set[1] != 99) {
    instruction_set <- s1[1:4 + 4*idx]
    processInstructionSet(instruction_set)
    idx <- idx + 1
  }
  return(s1[1])
}

# Define search grid
grid <- expand.grid(i=0:99, j=0:99)

# Search over grid and stop when the target is located
target <- 19690720
for (idx in 1:nrow(grid)) {
  if (calcVal(grid[idx,]$i, grid[idx,]$j) == target) {
    print(paste("Answer:", 100 * grid[idx,]$i + grid[idx,]$j))
    break
  }
}
