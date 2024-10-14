# Get R version
r_version <- R.version.string

# Get hostname
hostname <- Sys.info()["nodename"]

# Print the results
cat("R Version:", r_version, "\n")
cat("Hostname:", hostname, "\n")
