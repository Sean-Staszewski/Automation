import os
import importlib
import subprocess

#need default settings for batch_size, learning_rate, and # of nodes

file_name = "docking_train.ipynb"
file = importlib.import_module(f"{file_name}")

SysResCommand = ["./SysResCollector", "write", "1000000000", "620000000000", "Dock_TrainingT1.bin"]
fileCommand = ["jupyter", "nbconvert", "--to", "notebook", "--execute", "--inplace", "docking_train.ipynb"]
translateCommand = ["./SysResCollector", "read", "Dock_TrainingT1.bin", "Dock_TrainingT1.csv"]

new_learning_rate = [0.005, 0.01, 0.05, 0.1, 0.5]
new_node_size = [32, 64, 128, 256, 512]

for new_batch_size in range(1,100000):
    if (hasattr(file, 'batch_size')):
        setattr(file, 'batch_size', new_batch_size)
        #run NN and syscollector
        subprocess.Popen(SysResCommand)
        subprocess.run(fileCommand, check=true)
        subprocess.run(translateCommand, check=true)


SysResCommand[4] = "Dock_TrainingT2.bin"
translateCommand[2] = SysResCommand[4]
translateCommand[3] = "Dock_TrainingT2.csv"
#set batch size to standard
for i in range(len(new_learning_rate)):
    if (hasattr(file, 'lr')):
        setattr(file, 'lr', new_learning_rate[i])
        # run NN and syscollector
        subprocess.Popen(SysResCommand)
        subprocess.run(fileCommand, check=true)
        subprocess.run(translateCommand, check=true)


SysResCommand[4] = "Dock_TrainingT3.bin"
translateCommand[2] = SysResCommand[4]
translateCommand[3] = "Dock_TrainingT3.csv"
#set learning rate to standard
for i in range(len(new_node_size)):
    if (hasattr(file, 'size')):
        setattr(file, 'size', new_node_size[i])
        #run NN and syscollector
        subprocess.Popen(SysResCommand)
        subprocess.run(fileCommand, check=true)
        subprocess.run(translateCommand, check=true)

