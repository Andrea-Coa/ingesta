# Ejecuta en segundo plano (¡y en paralelo!) y redirige salida de pantalla a archivo de log 
# Todo lo que pintes en los archivos, en vez de que salga en pantalla lo redirige a logs
nohup python3 ingesta01.py > ./logs/ingesta01.log &
nohup python3 ingesta02.py > ./logs/ingesta02.log &
nohup python3 ingesta03.py > ./logs/ingesta03.log &
nohup python3 ingesta04.py > ./logs/ingesta04.log &
nohup python3 ingesta05.py > ./logs/ingesta05.log &
