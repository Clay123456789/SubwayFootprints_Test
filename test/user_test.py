import pytest
import requests
import json
from load_data import yaml_load


#以test开头才会被pytests识别
#pytest中，使用mark标记实现参数处理
@pytest.mark.parametrize('config',yaml_load.load('../config/config.yaml'))
@pytest.mark.parametrize('data',yaml_load.load('../data/user_login.yaml'))
def test_login(config,data):
    url = config['protocol']+'://'+config['ip']+":"+config['port']+config['user']['login']['path']
    res = requests.post(url,json=data['Data'])
    #print(res.text)
    message=json.loads(res.text)['message']
    #断言
    assert data['message'] == message


@pytest.mark.parametrize('config',yaml_load.load('../config/config.yaml'))
@pytest.mark.parametrize('data',yaml_load.load('../data/user_sendRegistEmail.yaml'))
def test_sendRegistEmail(config,data):
    url = config['protocol']+'://'+config['ip']+":"+config['port']+config['user']['sendRegistEmail']['path']
    res = requests.post(url,json=data['Data'])
    message=json.loads(res.text)['message']
    #断言
    assert data['message'] == message


@pytest.mark.parametrize('config',yaml_load.load('../config/config.yaml'))
@pytest.mark.parametrize('data',yaml_load.load('../data/user_regist.yaml'))
def test_regist(config,data):
    url = config['protocol']+'://'+config['ip']+":"+config['port']+config['user']['regist']['path']
    res = requests.post(url,json=data['Data'])
    message=json.loads(res.text)['message']
    #断言
    assert data['message'] == message

if __name__=='__main__':
    pytest.main(['-v','-s'])