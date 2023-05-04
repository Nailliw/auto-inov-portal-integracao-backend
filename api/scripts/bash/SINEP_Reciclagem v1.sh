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

INSTANCIAS1="SRV159_SINEP_${HOST}"
INSTANCIAS2="SRV159_SINEP-Internet_${HOST}"

HC=$HC_HOST:9999


## FUNCAO DE STOP DAS INSTANCIAS JBOSS
funcSTOP(){
$SEPARA
echo "EFETUANDO STOP DA INSTANCIA $1"

$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:kill"
#$J_HOME/bin/jboss-cli.sh -c --controller=10.123.41.37 --command="/host=cctdcapllx0159/server-config=SRV159_SINEP:status"
#/opt/jboss-master/bin/jboss-cli.sh -c --controller=10.123.41.37 --command="/host=cctdcapllx0159/server-config=SRV159_SINEP:status"

sleep 10 #
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1::stop"
sleep 10
#ps -ef | grep $1 | grep -v grep | awk '{print $2}'
PID_INSTANCIA = ps -ef | grep $1 | grep -v grep | awk '{print $2}'
kill -9 $PID_INSTANCIA

CHECK_PID = ps -ef | grep $1 | grep -v grep | awk '{print $2}'

# TESTE DE CHECAGEM DE PARA DE PID
if [ $CHECK_PID = 0]; then  
	echo "PID finalizado" |tee -a $J_LOG
else 
	echo "PID ainda em execução" |tee -a $J_LOG 
fi
}

##FUNCAO DE START DAS INSTANCIAS
funcSTART(){
$SEPARA
echo "INICIANDO INSTANCIA $1"
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:kill"
sleep 10
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:stop"
sleep 10
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:start"
sleep 10
}


## FUNCAO PARA VERIFICACAO DE STATUS

funcTesteStart(){


while [ $CONTSTART -le 6 ]; do

TESTE_START=`$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:read-attribute(name=status)" | grep STARTED | wc -l`
TESTE_STARTING=`$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:read-attribute(name=status)" | grep STARTING | wc -l`

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

TESTE_STOPDISABLE=`$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:read-attribute(name=status)" | egrep "STOPPED|DISABLED|FAILED" | wc -l`
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
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:kill"
sleep 10
$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=$HOSTN/server-config=$1:stop"
sleep 10
fi


done
}

funcClean(){
	#LIMPEZA DE TMP
	for (( COUNTER=1; counter<4; counter++))
	do
	rm -rf /opt/jboss-slave/domain/servers/SRV159_SINEP-Internet/tmp/*
	rm -rf /opt/jboss-slave/domain/servers/SRV159_SINEP/tmp/*
	

	#LIMPEDATA DE DATA
	rm -rf /opt/jboss-slave/domain/servers/SRV159_SINEP-Internet/data/*
	rm -rf /opt/jboss-slave/domain/servers/SRV159_SINEP/data/*
	done
	
	
#OPTION 2
    tar -czvf /tmp/server-one-tmp.tar.gz /opt/jboss/jboss-eap-digitalizar/domain/servers/server-one/tmp/*
    rm -rf /opt/jboss/jboss-eap-digitalizar/domain/servers/server-one/tmp/*
    tar -czvf /tmp/server-two-tmp.tar.gz/opt/jboss/jboss-eap-digitalizar/domain/servers/server-two/tmp/*
    rm -rf /opt/jboss/jboss-eap-digitalizar/domain/servers/server-two/tmp/*

        #LIMPEDATA DE DATA

    tar -czvf /tmp/server-one-data.tar.gz /opt/jboss/jboss-eap-digitalizar/domain/servers/server-one/data/*
    rm -rf /opt/jboss/jboss-eap-digitalizar/domain/servers/server-one/data/*
    tar -czvf /tmp/server-two-data.tar.gz /opt/jboss/jboss-eap-digitalizar/domain/servers/server-two/data/*
    rm -rf /opt/jboss/jboss-eap-digitalizar/domain/servers/server-two/data/*
	
}


Test(){
	$J_HOME/bin/jboss-cli.sh -c --controller=$HC --command="/host=habitacao_$HOSTN/server-config=$1:read-attribute(name=status)"
}


## FUNCAO DE ORGANIZACAO E EXECUCAO NO $1
EXECUTA(){

for INST in `echo $INSTANCIAS1` `echo $INSTANCIAS2` `echo $INSTANCIAS3` `echo $INSTANCIAS4` `echo $INSTANCIAS5` `echo $INSTANCIAS6` `echo $INSTANCIAS8`
do

#Version JBOSS
cat /opt/jboss-master/version.txt
#Version JBOSS Slave
cat /opt/jboss-slave/version.txt
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