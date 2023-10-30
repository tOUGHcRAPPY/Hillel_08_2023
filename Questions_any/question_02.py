import os
import requests
import threading
import time
from multiprocessing import Process
from threading import Thread

# AC:

# This code works pretty slowly.
# Change it using multithreading and multiprocessing as we did in the lesson
# Add time counters and uncomment the print command in the try/except block.
# P.S. Use time.perf_counter.
# The encryption could simulate the heavy task.
# No need to achieve the actual encryption
# The image downloader should download the image for real


image_url = "https://picsum.photos/1000/1000"
file_path = "rockyou.txt"


class Task:
    # NOTE:CPU-bound task (heavy computation)

    @staticmethod
    def encrypt_file(file_path: str):
        """This function is CPU-bound task function.
        It is encrypting the specific file."""
        start_time = time.perf_counter()
        print(f"Encrypting file from {file_path} in process {os.getpid()}")
        # Simulate heavy computation by sleeping for a while:
        _ = [i for i in range(150_000_000)]
        end_time = time.perf_counter()
        encryption_time = end_time - start_time
        print(f"Encrypting file takes {encryption_time} second.")
        return encryption_time

    # NOTE:I/O-bound task (downloading image from URL)

    @staticmethod
    def download_image(image_url: str):
        """This function is IO-bound task function.
        It is downloading image from the internet."""
        start_time = time.perf_counter()
        print(
            f"Downloading image from {image_url} \n"
            f"in thread {threading.current_thread().name}"
        )
        response = requests.get(image_url)
        with open("image.jpg", "wb") as f:
            f.write(response.content)
        end_time = time.perf_counter()
        downloading_time = end_time - start_time
        print(f"Downloading image takes {downloading_time} seconds.")
        return downloading_time


def run():
    # NOTE: common execution:
    print("➡️ common execution➡️")
    try:
        common_encryption_time = Task.encrypt_file(file_path)
        common_downloading_time = Task.download_image(image_url)
        total = common_encryption_time + common_downloading_time
        print(
            f"Time taken for CPU-bound encryption task:\n"
            f"{common_encryption_time} seconds⏱,\n"
            f"IO-bound task: {common_downloading_time} seconds⏱,\n"
            f"Total: {total} seconds✅"
        )
    except Exception as e:
        print(f"Error occurred: {e}")

    # NOTE:concurrent execution:
    # NOTE:IO-bound in threads and CPU-bound in processes:
    print("🔀concurrent execution..🔀")

    try:
        download_start = time.perf_counter()

        threads = [Thread(target=Task.download_image, args=(image_url,))]

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

        downloading_time = time.perf_counter() - download_start

        encryption_start = time.perf_counter()

        process = Process(target=Task.encrypt_file, args=(file_path,))
        process.start()
        process.join()
        # for process in processes:
        # process.start()

        # for process in processes:
        # process.join()

        encryption_time = time.perf_counter() - encryption_start

        total = encryption_time + downloading_time

        print(
            f"Time taken for CPU-bound encryption task:\n"
            f"{encryption_time} seconds⏱,\n"
            f"IO-bound task: {downloading_time} seconds⏱,\n"
            f"Total: {total} seconds✅"
        )
    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    run()
