##SCRIPT RECICLAGEM AUTOMATIZADA DE INSTANCIAS JBOSS EAP - sictd-digitalizar-intranet
######################################################

######################################################
## CONTROLE DE VERSOES
######################################################
## 1.0 -05/07/2022 - Criacao do script - Igor Nava - p540406
## 1.1 28/03/2023 - Inclusão da função de limpeza - p527488 - Joesley S. Silva - WO0000061877230
######################################################

## DECLARACAO DE VARIAVEIS ALTERAVEIS
J_HOME="/opt/jboss/jboss-eap-digitalizar"

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
if [ $HOSTN == dbrngapllx117 ]; then
	HOSTN="dbrngapllx117"
fi
HOSTNAME='hostname | cut -d "." -f1'
HC_HOST=`hostname -i`

INSTANCIAS1="sictd-digitalizar-intranet_node1_$HOSTNAME"
INSTANCIAS2="sictd-digitalizar-intranet_node3_$HOSTNAME"
INSTANCIAS3="sictd-digitalizar-intranet_node5_$HOSTNAME"

HC=$HC_HOST:9999
#HC=10.252.168.148:9999

## FUNCAO DE STOP DAS INSTANCIAS JBOSS




}


Test(){
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=digitalizar_$HOSTN/server-config=$1:read-attribute(name=status)"
}


## FUNCAO DE ORGANIZACAO E EXECUCAO NO $1
EXECUTA(){

for INST in `echo $INSTANCIAS1` `echo $INSTANCIAS2` `echo $INSTANCIAS3`
do

Test $INST

#$SEPARA >> $J_LOG2
$SEPARA
done
}

EXECUTA > $J_LOG