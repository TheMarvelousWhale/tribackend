###
mkdir previous_results
git clone git@github.com:TheMarvelousWhale/lightweight-human-pose-estimation.pytorch.git pose-estimation
git clone git@github.com:TheMarvelousWhale/pifuhd.git pifuhd
mkdir -p backend/static/uploads
wget https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth 
mv checkpoint_iter_370000.pth pose-estimation


mkdir -p pifuhd/{checkpoints,sample_images}
wget "https://dl.fbaipublicfiles.com/pifuhd/checkpoints/pifuhd.pt" pifuhd.pt
mv pifuhd.pt pifuhd/checkpoints/

git clone git@github.com:TheMarvelousWhale/pix2surf.git
#download blender on https://download.blender.org/release/Blender2.79/
mkdir pix2surf/{output,video}
cd pix2surf
bash scripts/prepare_data.sh