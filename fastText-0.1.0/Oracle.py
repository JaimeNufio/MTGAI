from subprocess import call 

bash= "./fasttext predict-prob model_MTG.bin - 5" 
#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()
formatt = bash.split(" ");
call(formatt);
