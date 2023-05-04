## SCRIPT RECICLAGEM AUTOMATIZADA DE INSTANCIAS JBOSS EAP - SINEP
######################################################

######################################################
## CONTROLE DE VERSOES
######################################################
## 1.0 -18/03/2022 - Criacao do script
## Joesley Soares Silva - p527488
######################################################

## DECLARACAO DE VARIAVEIS ALTERAVEIS
J_HOME="/opt/jboss-slave"

## DECLARACAO DE VARIAVEIS FIXA
L_DIR=/producao/rotina
L_BASE=PRDDB001
L_LOG=$L_DIR/$L_BASE/log
L_TMP=$L_DIR/$L_BASE/tmp
L_SHELL=$L_DIR/$L_BASE/shell
DATA_HORA=`date +'%d%m%Y_%H%M%S'`
DATA=`date +'%d/%m/%Y %H:%M:%S'`
J_LOG=$L_LOG/$HOSTN.$DATA_HORA.log
SEPARA="echo "----------------------------------------------------------------------------------""
CONTSTART=1
CONTSTOP=1
HOST=`hostname | cut -d "." -f1| cut -c 9-13`
HOSTN=`hostname | cut -d "." -f1`
HC_HOST=`hostname -i`

INSTANCIAS1="SRV159_SINEP"
INSTANCIAS2="SRV159_SINEP-Internet"

HC=$HC_HOST:9999



## FUNCAO PARA VERIFICACAO DE STATUS

funcTesteStart(){

while [ $CONTSTART -le 6 ]; do
TESTE_START=`$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:read-attribute(name=status)" | grep STARTED | wc -l`
	# INSTANCE
	#SRV159_SINEP-Internet_lx015
	#TESTE DE PROVA
	#/opt/jboss-master/bin/jboss-cli.sh -c --controller=10.123.41.37:9999 --command="/host=cctdcapllx0159/server-config=SRV159_SINEP-Internet:read-attribute(name=status)" | grep STARTED | wc -l


}



Test(){
	$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:read-attribute(name=status)" | grep STARTED | wc -l
	#/opt/jboss-master/bin/jboss-cli.sh -c --controller=10.123.41.37:9999 --command="/host=cctdcapllx0159/server-config=SRV159_SINEP-Internet:read-attribute(name=status)" | grep STARTED | wc -l
	#/opt/jboss-master/bin/jboss-cli.sh -c --controller=10.123.41.37:9999 --command="/host=$HOSTN/server-config=SRV159_SINEP-Internet_lx015:read-attribute(name=status)" 
}


## FUNCAO DE ORGANIZACAO E EXECUCAO NO $1
EXECUTA(){

for INST in `echo $INSTANCIAS1` `echo $INSTANCIAS2` 
do
# Version JBOSS 
# Red Hat JBoss Enterprise Application Platform - Version 7.0.9.GA
cat /opt/jboss-master/version.txt 

# Version JBOSS Slave 
# Red Hat JBoss Enterprise Application Platform - Version 7.0.6.GA

cat /opt/jboss-slave/version.txt

Test $INST
sleep 15
funcTesteStart $INST


#$SEPARA >> $J_LOG2
$SEPARA
done
}

EXECUTA > $J_LOG