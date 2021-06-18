#!/bin/bash

# Substituir de acordo com o ambiente.
wget 'http://localhost:8080/desafio.tar' 

tar -xf desafio.tar
rm -rf desafio/README*

for i in `ls desafio/*.txt`; do cat $i; done > all

for i in `ls -alh ./desafio/ | awk '{print $9}' | grep "._" `; do rm -rf desafio/$i; done

s=$(cat all)
grep -Eo '[[:alpha:]]+|[0-9]+' <<<"$s" > separated

# Script para gerar arquivos
/usr/bin/python3 convert.py