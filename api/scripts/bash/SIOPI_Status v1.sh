## SCRIPT RECICLAGEM AUTOMATIZADA DE INSTANCIAS JBOSS EAP - SIOPI-WEB
######################################################

######################################################
## CONTROLE DE VERSOES
######################################################
## 1.0 -03/03/2022 - Criacao do script
## Marcos Antônio Ferreira - P657816
######################################################

## DECLARACAO DE VARIAVEIS ALTERAVEIS
J_HOME="/opt/jboss/jboss-eap"

## DECLARACAO DE VARIAVEIS FIXA
L_DIR=/producao/rotina
L_BASE=PRDDB001
L_LOG=$L_DIR/$L_BASE/log
L_TMP=$L_DIR/$L_BASE/tmp
L_SHELL=$L_DIR/$L_BASE/shell
HOSTN=`hostname | cut -d "." -f1`
if [ $HOSTN == bbrnpapllx016 ]; then
HOSTN="brnpapllx016"
fi
DATA_HORA=`date +'%d%m%Y_%H%M%S'`
DATA=`date +'%d/%m/%Y %H:%M:%S'`
J_LOG=$L_LOG/$HOSTN.$DATA_HORA.log
SEPARA="echo "----------------------------------------------------------------------------------""
CONTSTART=1
CONTSTOP=1
HOST=`hostname | cut -d "." -f1| cut -c 9-13`
#DTC_CTC=`hostname -i | cut -d "." -f2`
#
#if [ $DTC_CTC -eq 252 ]
#   then
#    DTC_CTC="_DTC "
#   else
#    DTC_CTC=""
#  fi
#EXC=dbrngapllx046
HC_HOST=`hostname -i`

INSTANCIAS1="siopi-web-prd-node01_${HOST}"
INSTANCIAS2="siopi-web-prd-node02_${HOST}"
INSTANCIAS3="siopi-web-prd-node03_${HOST}"
INSTANCIAS4="siopi-intranet-prd-node01_${HOST}"
INSTANCIAS5="siopi-intranet-prd-node02_${HOST}"
INSTANCIAS6="siopi-intranet-prd-node03_${HOST}"
INSTANCIAS8="siopi-internet-prd-node01_${HOST}"
INSTANCIAS9="siopi-internet-prd-node02_${HOST}"


HC=$HC_HOST:9999
#HC=10.252.168.37:9999

## FUNCAO DE STOP DAS INSTANCIAS JBOSS



Test(){
	$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:read-attribute(name=status)"
	echo ""
}


## FUNCAO DE ORGANIZACAO E EXECUCAO NO $1
EXECUTA(){

for INST in `echo $INSTANCIAS1` `echo $INSTANCIAS2` `echo $INSTANCIAS3` `echo $INSTANCIAS4` `echo $INSTANCIAS5` `echo $INSTANCIAS6` `echo $INSTANCIAS8`
do

Test $INST



#$SEPARA >> $J_LOG2
$SEPARA
done
}


EXECUTA > $J_LOG