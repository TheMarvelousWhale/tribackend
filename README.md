# Hello 

## WARNING
If you are running on sm_86 for cuda (aka NVIDIA 3080)

Then please follow this guide to install the wheel installation build for torch https://blog.csdn.net/a563562675/article/details/121656894

Otherwise, your default torch install will install a wrong version of cudatoolkit=1.10.2

Please switch conda to base env and git branch of pifuhd to gpu if you want to use gpu

## SETUP

Before you can run, at the root of this project, you need to git clone these 2 forks into their respective folder that I have gitignored

* https://github.com/TheMarvelousWhale/pifuhd
* https://github.com/TheMarvelousWhale/lightweight-human-pose-estimation.pytorch

Then you will need to put 
* `checkpoint_iter_370000.pth` in `lightweight-human-pose-estimation.pytorch\`
* `pifuhd.pt` under `pifuhd\checkpoints\` 

Anyway I make it into 3 microservices to run them independently

Then run the 3 microservices at the port designated on config.yaml

## How It works

The backend has 3 parts:
1. A web interface to serve commands
2. A pose estimation pipeline
3. PifuHD pipeline

The web will send the image to the pose estimation pipeline, which will then extract the pose information into a text format into a designated folder inside pifuHD. pifuHD will then output a obj file in the result folder. 

Pending: display the 3D obj file on web