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



# utilizei a uma aresta de 110 para a resolução do raster ter 1m
D=gausfrag(445,70,40)
#x11()
#hist(D,main="distribuição dos valores originais")
ras= "C:\\Users\\Edgar\\Documents\\Python_Scripts\\PDI\\habin3.tif"
rast(ras)
image(mrast)
p= 0.5
p1=quantile(D,1-p)
mrast= raster(D>p1)
aggregate(mrast, fact=9 )



for (p in seq(0.1,0.9,0.1)){
  p1=quantile(D,1-p)
  #x11()
  image(D>p1)
  title(main=p)
  # print(c(p,p1,mean(D>=p1)))
}

####################################################################################
############################Tranformando a resolução do raster######################
####################################################################################
#Transformando metros em graus decimais 2/111.320.
# 1 metro tem 111.320 graus.

= seq(0.1,0.9,0.1)

for(i in 3:10){
  landgenerator(110,70,40,pland,i)
}


landgenerator= function(aresta,pais,filhos,pland,n){
  
  D= gausfrag(aresta,pais,filhos)
  
  for (p in pland){
    p1=quantile(D,1-p)
    mrast= raster(D>p1)
    nrast= paste0("Land",gsub("%","", names(p1)),"_",n,".tif")
    writeRaster(mrast,nrast,format="GTiff", overwrite= F)

    
  }
  
}


