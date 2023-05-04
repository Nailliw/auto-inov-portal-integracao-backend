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
funcSTOP(){
$SEPARA
echo "EFETUANDO STOP DA INSTANCIA $1"

$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:kill"
sleep 10 #
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:stop"
sleep 10
#ps -ef | grep $1 | grep -v grep | awk '{print $2}'
PID_INSTANCIA = ps -ef | grep $1 | grep -v grep | awk '{print $2}'
# TESTE EM MAQUINA
#PID_INSTANCIA = ps -ef | grep 'sictd-digitalizar-intranet_node1_dbrngapllx135' | grep -v grep | awk '{print $2}'
kill -9 $PID_INSTANCIA

CHECK_PID = ps -ef | grep $1 | grep -v grep | awk '{print $2}'

# TESTE DE CHECAGEM DE PARA DE PID
if [ $CHECK_PID = 0]; then  
	echo "PID finalizado" 
else 
	echo "PID ainda em execução" 
	funcSTOP
fi
}

##FUNCAO DE START DAS INSTANCIAS
funcSTART(){
$SEPARA
echo "INICIANDO INSTANCIA $1"
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:kill"
sleep 10
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:stop"
sleep 10
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:start"
sleep 10
}


## FUNCAO PARA VERIFICACAO DE STATUS

funcTesteStart(){


while [ $CONTSTART -le 6 ]; do

TESTE_START=`$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:read-attribute(name=status)" | grep STARTED | wc -l`
TESTE_STARTING=`$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:read-attribute(name=status)" | grep STARTING | wc -l`

        if [ $TESTE_START -ge 1 ]; then
                echo "INSTANCIA JBOSS $1 INICIADA COM SUCESSO" |tee -a $J_LOG
                break
        elif [ $TESTE_STARTING -eq 1 ]; then
                echo "INSTANCIA JBOSS $1 SENDO INICIADA..."
                sleep 15
        elif [ $TESTE_START -ne 1 ] && [ $CONTSTART -eq 6 ]; then
                -DADNGAPLLX035
                break
        else
                sleep 15
                CONTSTART=`expr $CONTSTART + 1`
        fi

done
}


funcTesteStop(){

while [ $CONTSTOP -le 6 ]; do

TESTE_STOPDISABLE=`$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:read-attribute(name=status)" | egrep "STOPPED|DISABLED|FAILED" | wc -l`
        if [ $TESTE_STOPDISABLE -ge 1 ]; then
                echo "INSTANCIA JBOSS $1 PARADA COM SUCESSO" |tee -a $J_LOG
                break
        elif [ $TESTE_STOPDISABLE -ne 1 ] && [ $CONTSTOP -eq 6 ]; then
                echo "INSTANCIA JBOSS $1 TRAVADA"
                exit 2
        else
                sleep 30
                CONTSTOP=`expr $CONTSTOP + 1`
        fi

 if [ $CONTSTOP -eq 2 ] || [ $CONTSTOP -eq 4 ]; then
         pid=`ps -ef | grep $1 | grep -v grep|  awk '{print $2}'`
   echo "executando kill no processo $pid da instancia $1"
         kill -9 $pid



echo "Instancia $1 encontra-se travada executando stop"
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:kill"
sleep 10
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:stop"
sleep 10
fi


done
}

funcClean(){
	#LIMPEZA DE TMP
	for (( COUNTER=1; counter<4; counter++))
	do
	rm -rf /opt/jboss/jboss-eap/hc/tmp/servers/siopi-web-prd-node0"$COUNTER"_lx013/*

	#LIMPEDATA DE DATA
	rm -rf /opt/jboss/jboss-eap/hc/data/servers/siopi-web-prd-node0"$COUNTER"_lx013/*
	done

}


Test(){
	$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:read-attribute(name=status)"
	echo ""
}


## FUNCAO DE ORGANIZACAO E EXECUCAO NO $1
EXECUTA(){

for INST in `echo $INSTANCIAS1` `echo $INSTANCIAS2` `echo $INSTANCIAS3` `echo $INSTANCIAS4` `echo $INSTANCIAS5` `echo $INSTANCIAS6` `echo $INSTANCIAS8`
do

#Test $INST
funcSTOP $INST
sleep 15 # 
# funcTesteStop $INST #Já há um teste dentro do stop. Atualizado em 16/03/2023
#sleep 15
funcClean $INST
sleep 15
funcSTART $INST
sleep 15
funcTesteStart $INST


#$SEPARA >> $J_LOG2
$SEPARA
done
}


EXECUTA > $J_LOG