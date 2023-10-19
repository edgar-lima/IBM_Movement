def convert(x,y, conf):

  ux= conf[2]
  uy= conf[5]
  resx= conf[0]
  resy= conf[4]
  newx= ux + x * resx
  newy= uy + y * resy

  return (newx,newy)


convert(0,0,land.meta["transform"])
dest
land.meta
