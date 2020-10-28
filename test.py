from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED, FIRST_COMPLETED
import time

# 参数times用来模拟网络请求的时间
def download_video(index,a):
    time.sleep(2)
    print("download video {} finished at {}".format(index,time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())))
    return index

executor = ThreadPoolExecutor(max_workers=2)
urls = [(1,3),(2,3),(3,5),(4,6)]
all_task = [executor.submit(download_video,(url)) for url in urls]

wait(all_task,return_when=ALL_COMPLETED)

print("main ")