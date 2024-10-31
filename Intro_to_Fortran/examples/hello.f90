program hello
  implicit none
  character(len=100) :: your_name

  print *, 'Your Name Please'
  read *, your_name
  print *, 'Hello ', your_name

end program hello
