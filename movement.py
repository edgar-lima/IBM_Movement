def movement(x,eq,land,tmove="NOri"):
  pop2= []
  
  if tmove=="NOri":
    for i in range(x.shape[0]):
      pop2.append(IndNoriented(x.values[i,:],eq,land))
      
  elif tmove=="Ori":
    for i in range(x.shape[0]):
      pop2.append(IndOriented(x.values[i,:],eq,land))
      
  elif tmove=="Memo":
    for i in range(x.shape[0]):
      pop2.append(IndMemory(x.values[i,:],eq,land))

  return(pop2)

