def print_square(size):
    """burada iste bir eded olur ve bir #simvolu onu 4 e vuranda 4 dene eyni simvol yansai olacag onu isteyir bizden"""

   if  isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
   if not isinstance(size, int):
        raise TypeError("size must be an integer")
   if size < 0:
       raise TypeError("size must be >= 0")
   for i in range(size):
       print("#" * size)
