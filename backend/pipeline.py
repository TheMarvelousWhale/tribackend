import importlib.util,os,subprocess,shutil
import datetime as dt
from unittest import result

def preprocessing_image(id,res=256):
    cd = os.getcwd()
    os.chdir('../lightweight-human-pose-estimation.pytorch')
    subprocess.call(f"python preprocessing.py ../pifuhd/sample_images/{id} -r {res}")
    os.chdir(cd)

def gen_model_from_image(res=256):
    cd = os.getcwd()
    os.chdir('../pifuhd')
    subprocess.call(f"python -m apps.simple_test --use_rect -r {res} -i sample_images")
    os.chdir(cd)

def clean_up(id,res):
    try:
        file_prefix = gen_curtime()
        result_dir = "../pifuhd/results/pifuhd_final/recon/"
        obj = id[:id.rfind('.')]+f"_{res}.obj"
        shutil.move(f"{result_dir}result_{obj}",f"../previous_results/{file_prefix}_{obj}")
        png = obj.replace('.obj','.png')
        shutil.move(f"{result_dir}result_{png}",f"../previous_results/{file_prefix}_{png}")
        os.remove(f"../pifuhd/sample_images/{id}")
        os.remove(f"../pifuhd/sample_images/{id[:id.rfind('.')]}_rect.txt")
    except Exception as e:
        print(e)

def gen_curtime():
    mytime = dt.datetime.strptime('0130','%H%M').time()
    mydatetime = str(dt.datetime.combine(dt.date.today(), mytime))
    return mydatetime.replace(' ','_').replace(':','-')

