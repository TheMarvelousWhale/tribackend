import datetime as dt
import yaml 

def load_config_from_yaml(filename):
    with open(filename, "r") as yamlfile:
        data = yaml.load(yamlfile, Loader=yaml.FullLoader)
        return data

def is_file_allowed(filename:str, whitelist:list) -> bool:
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in whitelist

def now():
    mytime = dt.datetime.strptime('0130','%H%M').time()
    mydatetime = str(dt.datetime.combine(dt.date.today(), mytime))
    return mydatetime.replace(' ','_').replace(':','-')