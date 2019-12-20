# Load data
dat <- readLines("./data.txt")

# ------------------------------ Part I ------------------------------ #

# Break CSVs into value array
s1 <- as.numeric(strsplit(dat, ",")[[1]])

# Given initial input of 1
input <<- 1

# Process one n-array instruction set
processInstructionSet <- function(op, x, modes) {

  # Perform calculation according to operator and mode
  val <- switch(op,
    # Addition operator
    "1" = {
      s1[x[3] + 1] <<-
        ifelse(modes[1] == "0", s1[x[1] + 1], x[1]) +
        ifelse(modes[2] == "0", s1[x[2] + 1], x[2])
    },
    # Multiplication operator
    "2" = {
      s1[x[3] + 1] <<-
        ifelse(modes[1] == "0", s1[x[1] + 1], x[1]) *
          ifelse(modes[2] == "0", s1[x[2] + 1], x[2])
    },
    # Input
    "3" = {
      s1[x[1] + 1] <<- input
    },
    # Output
    "4" = {
      ifelse(modes == "0", print(s1[x[1] + 1]), print(x[1]))
    },
    # Halt signal
    "99" = {
      return(NULL)
    },
    # Invalid operator (default)
    stop(paste("Invalid operator:", op))
  )
}

# Start pointer at beginning and trace through until halt encountered
pointer <- 1; operator <- 0

while (operator != 99) {
  cur_op <- as.character(s1[pointer])

  if (nchar(cur_op) > 2) {
    # New immediate mode
    codes <- strsplit(cur_op, "")[[1]]
    operator <- as.numeric(substr(cur_op, nchar(cur_op) - 1, nchar(cur_op)))
    if (!(operator %in% 3:4)) {
      modes <- rev(c(rep("0", 5 - nchar(cur_op)), strsplit(substr(cur_op, 1, nchar(cur_op) - 2), "")[[1]]))
    } else {
      modes <- codes[1]
    }

    # Relevant parameters
    params <- s1[(pointer + 1):(pointer + ifelse(any(3:4 %in% operator), 1, 3))]
  } else {

    # Position Mode (as before)
    operator <- as.numeric(cur_op)

    # Relevant parameters
    params <- s1[(pointer + 1):(pointer + ifelse(any(3:4 %in% operator), 1, 3))]

    # All parameters are called by reference in this mode
    modes <- rep("0", length(params))
  }

  # Process Instructions
  processInstructionSet(operator, params, modes)

  # Update pointer
  pointer <- pointer + ifelse(any(3:4 %in% operator), 2, 4)
}

# ------------------------------ Part II ------------------------------ #
# Extended with added opcodes

# Reset vector
s1 <- as.numeric(strsplit(dat, ",")[[1]])

# Given initial input of 5 this time
input <- 5

# Process one n-array instruction set
processInstructionSet2 <- function(op, x, modes) {
  if (op == "1") {
    # Addition operator
    s1[x[3] + 1] <<-
      ifelse(modes[1] == "0", s1[x[1] + 1], x[1]) +
      ifelse(modes[2] == "0", s1[x[2] + 1], x[2])
    pointer <<- pointer + 4
  } else if (op == "2") {
    # Multiplication operator
    s1[x[3] + 1] <<-
      ifelse(modes[1] == "0", s1[x[1] + 1], x[1]) *
        ifelse(modes[2] == "0", s1[x[2] + 1], x[2])
    pointer <<- pointer + 4
  } else if (op == "3") {
    # Input
    s1[x[1] + 1] <<- input
    pointer <<- pointer + 2
  } else if (op == "4") {
    # Output
    ifelse(modes == "0", print(s1[x[1] + 1]), print(x[1]))
    pointer <<- pointer + 2
  } else if (op == "5") {
    # Jump-if-true
    if (ifelse(modes[1] == "0", s1[x[1] + 1], x[1]) != 0) {
      pointer <<- ifelse(modes[2] == "0", s1[x[2] + 1], x[2]) + 1
    } else {
      pointer <<- pointer + 3
    }
  } else if (op == "6") {
    # Jump-if-false
    if (ifelse(modes[1] == "0", s1[x[1] + 1], x[1]) == 0) {
      pointer <<- ifelse(modes[2] == "0", s1[x[2] + 1], x[2]) + 1
    } else {
      pointer <<- pointer + 3
    }
  } else if (op == "7") {
    # Less than
    s1[x[3] + 1] <<- as.integer(
      ifelse(modes[1] == "0", s1[x[1] + 1], x[1]) <
        ifelse(modes[2] == "0", s1[x[2] + 1], x[2])
    )
    pointer <<- pointer + 4
  } else if (op == "8") {
    # Equal
    s1[x[3] + 1] <<- as.integer(
      ifelse(modes[1] == "0", s1[x[1] + 1], x[1]) ==
        ifelse(modes[2] == "0", s1[x[2] + 1], x[2])
    )
    pointer <<- pointer + 4
  } else if (op == "99") {
    # Halt signal
    return(NULL)
  } else {
    # Invalid operator (default)
    stop(paste("Invalid operator:", op))
  }
}

# Utility function to help dictate
getParams <- function(operator) {
  if (operator %in% 1:2) {
    params <- s1[(pointer + 1):(pointer + 3)]
  } else if (operator %in% 3:4) {
    params <- s1[(pointer + 1)]
  } else if (operator %in% 5:6) {
    params <- s1[(pointer + 1):(pointer + 2)]
  } else if (operator %in% 7:8) {
    params <- s1[(pointer + 1):(pointer + 3)]
  } else if (operator == 99) {
    print("Halting instructions encountered")
    params <- NULL
  } else {
    stop("Invalid operator")
  }
  return(params)
}

# Start pointer at beginning and trace through
pointer <<- 1; operator <- 0

while (operator != 99) {
  cur_op <- as.character(s1[pointer])

  if (nchar(cur_op) > 2) {

    # New immediate mode
    codes <- strsplit(cur_op, "")[[1]]
    operator <- as.numeric(substr(cur_op, nchar(cur_op) - 1, nchar(cur_op)))
    if (!(operator %in% 3:4)) {
      modes <- rev(c(rep("0", 5 - nchar(cur_op)), strsplit(substr(cur_op, 1, nchar(cur_op) - 2), "")[[1]]))
    } else {
      modes <- codes[1]
    }

    # Relevant parameters depending on operation
    params <- getParams(operator)
  } else {

    # Position Mode (as before)
    operator <- as.numeric(cur_op)

    # Relevant parameters depending on operation
    params <- getParams(operator)

    # All parameters are called by reference in this mode
    modes <- rep("0", length(params))
  }

  # Process Instructions
  processInstructionSet2(operator, params, modes)
}
