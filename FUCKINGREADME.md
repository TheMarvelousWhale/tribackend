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


