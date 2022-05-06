# DS2022 4.14 Excercises RAJ Exercise 1 (R)

# check input (pulled from VitoshKa@stackoverflow)
check_int <- function(N) {
  !grepl("[^[:digit:]]", format(N,  digits = 20, scientific = FALSE))
}

# get user input
get_user_guess <- function() {
  
  guess <- readline(prompt = "Your guess please (integer): ")
  
  if(check_int(guess) == TRUE) {
    return(as.integer(guess)) 
  }
  else {return(get_user_guess()) }
}

# get random integer 
random_int <- sample(1:100, 1)
guess <- -1

# start guessing
cat("You are to guess a whole number between 0 and 100!")

while(guess != random_int) {
    
  guess <- get_user_guess()
    
  if (guess == random_int)
  {
    cat("You got it!")
  }
  else if (guess < random_int)
  {
    cat(guess, "is too small!")
  }
  else if(guess > random_int)
  {
    cat(guess, "is too large!")
  }
}
