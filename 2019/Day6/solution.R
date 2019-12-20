# Load data
dat <- readLines("./data.txt")

# ------------------------------ Part I ------------------------------ #

# This is useful in locating which path to follow
next_orbit <- sapply(dat, function(x) {
  strsplit(x, ")")[[1]][2]
})

# Function to trace a single orbit
traceOrbit <- function(spec) {

  # Parse
  spec_parse <- strsplit(spec, ")")[[1]]
  body <- spec_parse[1]

  # Check if this object orbits something else; if not, return 1, else recurse deeper
  idx <- which(next_orbit == body)
  if (length(idx) == 0) {
    return(1)
  } else {
    return(1 + traceOrbit(dat[idx]))
  }
}

# Apply to all orbits and calculate sum total
sum(sapply(dat, traceOrbit))

# ------------------------------ Part II ------------------------------ #

# Locate relevant specs in data
san <- grep("SAN", dat, value = TRUE)
you <- grep("YOU", dat, value = TRUE)

# This time, we'll keep track of the paths and will discover when they first share a common root
traceOrbit2 <- function(spec) {

  # Parse
  spec_parse <- strsplit(spec, ")")[[1]]
  body <- spec_parse[1]

  # Check if this object orbits something else; if not, return body, else recurse deeper
  idx <- which(next_orbit == body)
  if (length(idx) == 0) {
    return(body)
  } else {
    return(do.call("c", list(spec, traceOrbit2(dat[idx]))))
  }
}

# Trace paths from SAN and YOU to root node
san_path <- traceOrbit2(san)
you_path <- traceOrbit2(you)

# Find the location at which these paths begin to intersect
common_root <- san_path[which(san_path %in% you_path)[1]]

# Find the path distance accounting for this overlap (-2 to account for initial orbit and common node)
(which(san_path == common_root) - 2) + (which(you_path == common_root) - 2)
