setwd("C:\\Users\\Edgar\\OneDrive - unb.br\\IBM_Movement\\LandScapes")
library(raster)

gausfrag = function(aresta,pais,filhos){
  D=matrix(nrow=aresta,ncol=aresta,data=0)
  for (ipais in 1:pais){
    mlp=round(runif(1,-1,aresta+1));mcp=round(runif(1,-1,aresta+1));
    for (ifilhos in 1:filhos){
      ml=round(rnorm(1,mlp,aresta/runif(1,25,50)));mc=round(rnorm(1,mcp,aresta/runif(1,25,50)));
      sigma=runif(1,0,1)*0.20*aresta+0.20*aresta*runif(1,0,1);
      for (l in 1:aresta){
        for (c in 1:aresta){
          D[l,c]=D[l,c]+10*exp(-(((l-ml)^2)+(((c-mc)^2)))/sigma);
        }
      }
    }
  }
  
  mn=min(D)
  mx=max(D)
  D=(D - mn)/(mx-mn);
  return(D)}
D=gausfrag(100,70,40)
####################################################################################
############################Gerador de rasters #####################################
####################################################################################
pland= seq(0.1,0.9,0.1)
a= landgenerator(100,70,40,10,0.2)

landgenerator= function(aresta,pais,filhos,cres,pland,n=1){
  D= gausfrag(aresta,pais,filhos)
  resGD= cres/11131
  coord_max= resGD*aresta
  
  for (p in pland){
    p1=quantile(D,1-p)
    mrast= raster(D>p1, xmn = 0, xmx = coord_max,ymn = 0, ymx = coord_max)
    nrast= paste0("Land",gsub("%","", names(p1)),"_",n,".tif")
    #writeRaster(mrast,nrast,format="GTiff", overwrite= F)

    
  }
  return(mrast)
}
