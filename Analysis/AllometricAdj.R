## Carregando pacotes
library(openxlsx)
library(tidyverse)
library(dplyr)
library(minpack.lm)
library(nlstools)

## Carregando a base de dados
dire<- c("C:\\Users\\Edgar\\OneDrive - unb.br\\Doutorado\\CapII\\Dados_analises")

BMR<- read.xlsx(paste(dire,"Alometria.xlsx", sep = "\\" ), sheet = 1)# Dados para taxa metabolica basal
HRS<- read.xlsx(paste(dire,"Alometria.xlsx", sep = "\\" ), sheet = 2)# Dados para tamanho do home range
View(BMR); View(HRS)

## Organizando a base de dados
BMR2<-BMR%>% select(-c(Reff., Guilda))
colnames(BMR2)<- c("sp", "Mass", "BMR")
colnames(HRS)<- c("sp", "Mass", "HRS")

HRS2<-HRS%>%mutate(HRM= HRS*10000)%>%
  select(-HRS)# Convertendo de hectares para metros

BMR3<-BMR2%>%group_by(sp)%>%summarise(Mass= mean(Mass),
            BMR= mean(BMR))%>%
  filter(Mass<40)# Calculando a massa e BMR media das sp

HRS3<-HRS2%>%group_by(sp)%>%
  summarise(Mass= mean(Mass),HRM= mean(HRM))%>%
  filter(Mass<40)%>%filter(HRM<785000)# Calculando a massa e HRM media das sp

## Ajustando modelo para taxa metabolica basal.
BMR4<- nlsLM(BMR3$BMR ~ K*BMR3$Mass^b,
             data=BMR3,
             start=list(K=0.0005,b=0.75),
             alg="default")

summary(BMR4)
coefficients(BMR4)

## Ajustando modelo para taxa metabolica basal.
HRS4<- nlsLM(HRS3$HRM ~ K*HRS3$Mass^b,
             data=HRS3,
             start=list(K=0.5,b=0.75),
             alg="default")

summary(HRS4)
coefficients(HRS4)

## Grafico da taxa metabolica basal

ggplot(BMR3,aes(x=Mass, y= BMR))+
  geom_point(size= 3.5)+
  stat_smooth(method = "nls",formula = y ~ a*x^b,
              method.args = list(start = list(a=0.5,b=0.75)),
              se = F, colour= "red")+
  scale_x_continuous(breaks= seq(0,45,5),limits = c(0,45))+
  scale_y_continuous(breaks= seq(0,0.75,0.1),limits = c(0, 0.75))+
  xlab("Body mean mass (g)") + 
  ylab("Basal Metabolic Rate (W)")+
  #annotate("text",y= 24, x= 40 ,label="t= -1.413; df= 12; p= 0.183", size= 8)+
  annotate("text",y= 0.75, x= 5 ,label="BMR== 0.044*M^{0.634} ",parse= T, size= 8)+
  theme_bw()+
  theme(panel.grid = element_blank(),
        axis.title = element_text(size = 20, colour = "black"),
        axis.text = element_text(size = 16, colour = "black"),
        panel.border = element_rect(size= 1.4))

ggsave(filename = "BMR.pdf", width = 31, 
       height = 25, units = "cm", dpi = 200)

## Grafico do Home range

ggplot(HRS3,aes(x=Mass, y= HRM))+
  geom_point(size= 3.5)+
  stat_smooth(method = "nls",formula = y ~ a*x^b,
              method.args = list(start = list(a=0.5,b=0.75)),
              se = F, colour= "red")+
  scale_x_continuous(breaks= seq(0,45,5),limits = c(0,45))+
  #scale_y_continuous(breaks= seq(0,80000,500),limits = c(0, 80000))+
  xlab("Body mean mass (g)") + 
  ylab("Basal Metabolic Rate (W)")+
  #annotate("text",y= 24, x= 40 ,label="t= -1.413; df= 12; p= 0.183", size= 8)+
  annotate("text",y= 80000, x= 5 ,label="HRS== 943.557*M^{1.055} ",parse= T, size= 8)+
  theme_bw()+
  theme(panel.grid = element_blank(),
        axis.title = element_text(size = 20, colour = "black"),
        axis.text = element_text(size = 16, colour = "black"),
        panel.border = element_rect(size= 1.4))

ggsave(filename = "HRS.pdf", width = 31, 
       height = 25, units = "cm", dpi = 200)
