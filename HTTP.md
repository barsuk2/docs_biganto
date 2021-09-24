status_code
200 - ОК
308 - PERMANENT REDIRECT

### http запросы

#### модуль request

#### Простой GET
import requests as RQ
req = RQ.get('https://biganto.com')

req.status_code - ответ сервера
resp.headers - заголовки


GET
B_URL='http://local.biganto.com'
API_QS = {'client': 'web', 'client_version': '1.0'}
API_TOURS =API_QS.copy()
API_TOURS['user_id']=9
rv = requests.get(f'{B_URL}/api/v3/tours', params=API_TOURS)
rv = requests.get(f'{B_URL}/api/v3/tours', params={'client': 'web', 'client_version': '1.0','user_id': '9'})

tours_rv = sess.get(f'{B_URL}/api/v3/tours', params={'client': 'web', 'client_version': '1.0','user_id':9})

### AUTH 🇦🇪️
import requests
B_URL='http://local.biganto.com'
API_QS = {'client': 'web', 'client_version': '1.0'}
API_TOURS =API_QS.copy()
user = requests.post(f'{B_URL}/api/v3/users/login', json={'email': 'kasiatora@ya.ru', 'password': '123'}, params=API_QS)
API_TOURS['auth_token'] = user.json()['result'].get('token')
rv = requests.get(f'{B_URL}/api/v3/tours/81/qr', params=API_TOURS)

API_TOURS['auth_token'] = '9|CZS_gtlqbWaezh0zuDpJ-5uCwYvTUy9fEUYBsUXKfUeXL00ERU7Dj81Zb3I6zIlwEOg7BRaQNjT7HZlj-TB8-A=='

B_URL='https://biganto.com'
user = requests.post(f'{B_URL}/api/v3/users/login', json={'email': 'mikhaylov.web@biganto.com', 'password': 'nDC0A7Iy1myt'}, params=API_QS)



#### Создание API
Простейший
@mod.route('/qr')
def genirate(tour_id=None):
    print(dir(requests))
    return 'asdads', 202

#### Основные методы request

request
'accept_charsets', 
'accept_encodings', 
'accept_languages', 
'accept_mimetypes', 
'access_control_request_headers', 'access_control_request_method', 
'access_route', 'application', 
'args', ImmutableMultiDict([('client', 'web'), ('client_version', '1.0')])
'authorization', 
base_url', 
'blueprint',
cache_control', 
'charset', 
'close', 
'content_encoding', 
'content_length', 
'content_md5', '
content_type', 
'cookies', 
'data', 
'date', 
'dict_storage_class', 
'disable_data_descriptor', 
'encoding_errors', 
'endpoint', 
'environ', 
'files', 
'form', 
'form_data_parser_class', 
'from_values', 
'full_path', 
'get_data', 
'get_json', 
'headers',
host', 
'host_url', 
'if_match', 
'if_modified_since', 
'if_none_match', 
'if_range', 
'if_unmodified_since', 
'input_stream', 
'is_json', 
'is_multiprocess', 
'is_multithread', 
'is_run_once', 
'is_secure', 
'json', 
'json_module', 'list_storage_class', 'make_form_data_parser', 'max_content_length', 
'max_form_memory_size', 'max_forwards', 'method', 'mimetype', 'mimetype_params', 
'on_json_loading_failed', 'origin', 'parameter_storage_class', 'path', 'pragma', 'query_string', 
'range', 'referrer', 'remote_addr', 'remote_user', 'routing_exception', 'scheme', 'script_root', 
'shallow', 'stream', 'trusted_hosts', 
'url', 
'url_charset', 'url_root', 'url_rule', 'user_agent', 'values', 'view_args', 'want_form_data_parsed'

