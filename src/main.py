import time
import threading
from extract_data import extract_data
from transform_data import get_transformed_data
from load_data import load_data

def my_scheduled_job():
    # Place your function calls here
    print("Executing scheduled job at ", time.strftime("%Y-%m-%d %H:%M:%S"))
    extract_data()
    load_data()
    print("Scheduled job finished at ", time.strftime("%Y-%m-%d %H:%M:%S"))

def run_background_job(interval_minutes=1 ):
    def job_loop():
        while True:
            my_scheduled_job()
            time.sleep(interval_minutes * 60)
    thread = threading.Thread(target=job_loop, daemon=True)
    thread.start()

if __name__ == "__main__":
    run_background_job()
    # Keep the main thread alive
    while True:
        time.sleep(1)