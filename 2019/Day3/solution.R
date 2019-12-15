# Load data, and separate instructions for each wire
dat <- readLines("./data.txt")
w1 <- strsplit(dat[[1]],",")[[1]]
w2 <- strsplit(dat[[2]],",")[[1]]

# ------------------------------ Part I ------------------------------ #

# Contants for a "big enough" matrix to hold the wires
mat_size <- 30000; init_cursor <- floor(mat_size /2)

# Function to draw wire in matrix representation (1 if wire there, 0 if not)
drawWire <- function(wire) {
  
  # Init
  m <- matrix(data = FALSE, nrow = mat_size, ncol = mat_size)
  cursor_x <- init_cursor
  cursor_y <- init_cursor
  
  # Process draw instructions for the wire
  for (i in wire) {
    
    # Get direction and magnitude
    instructions <- strsplit(i,"(?=[RLUD])", perl = TRUE)[[1]]
    dir <- instructions[1]
    len <- as.numeric(instructions[2])

    # Write TRUE along the lines of movement, and update cursor
    if (dir == "R") {
      m[cursor_x, cursor_y:(cursor_y + len)] <- TRUE
      cursor_y <- cursor_y + len
    } else if (dir == "L") {
      m[cursor_x, (cursor_y - len):cursor_y] <- TRUE
      cursor_y <- cursor_y - len
    } else if (dir == "U") {
      m[cursor_x:(cursor_x + len), cursor_y] <- TRUE
      cursor_x <- cursor_x + len
    } else if (dir == "D") {
      m[(cursor_x - len):cursor_x, cursor_y] <- TRUE
      cursor_x <- cursor_x - len
    } else {
      stop("Invalid direction encountered.")
    }
  }
  return(m)
}

# Calculate wire matrices
m1 <- drawWire(w1)
m2 <- drawWire(w2)

# Overlay to discover all intersections
overlay <- Reduce("&",list(m1,m2))
intersections <- which(overlay, arr.ind = TRUE)

# Locate closest intersection
(closest_intersection <- sort(rowSums(abs(intersections - init_cursor)))[2]) #2, since 1 represents the starting point

# ------------------------------ Part II ------------------------------ #

# Since we have already discovered all of the intersections, we just need to learn for each intersection 
# the combined number of steps to reach the target and take the lowest among them
calculateSteps <- function(target_row, target_col, wire) {
  
  # Init
  cursor_x <- init_cursor
  cursor_y <- init_cursor
  step_count <- 0
  
  for (w in wire) {
    
    # Get direction and magnitude
    instructions <- strsplit(w, "(?=[RLUD])", perl = TRUE)[[1]]
    dir <- instructions[1]
    len <- as.numeric(instructions[2])
    cur_step <- 0
    
    while (cur_step < len) {
      
      # Count number of steps and update cursor incrementally
      if (dir == "R") {
        cursor_y <- cursor_y + 1
      } else if (dir == "L") {
        cursor_y <- cursor_y - 1
      } else if (dir == "U") {
        cursor_x <- cursor_x + 1
      } else if (dir == "D") {
        cursor_x <- cursor_x - 1
      } else {
        stop("Invalid direction encountered.")
      }
      step_count <- step_count + 1
      cur_step <- cur_step + 1
      
      # When target has been reached, it is the first such occurrence
      if ( (cursor_x == target_row) & (cursor_y == target_col) ) {
        return(step_count)
      }
    }
  }
}

# Compute and add together the steps from both wires
calculateBothSteps <- function(r,c) {
  return(calculateSteps(r,c,w1) + calculateSteps(r,c,w2))
}

# Apply function to all intersections
steps <- sort(unlist(apply(intersections, 1, FUN = function(x) calculateBothSteps(x[1], x[2]))))

# Answer:
steps[1]

