from subprocess import call 

bash= "./fastText-0.1.0/fasttext predict-prob ./fastText-0.1.0/model_MTG.bin - 5" 
formatt = bash.split(" ");
call(formatt);
