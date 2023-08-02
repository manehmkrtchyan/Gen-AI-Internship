from abc import ABC, abstractmethod
import requests
import threading
import multiprocessing


class Download(ABC):
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    @abstractmethod 
    def start_download(self):
        raise NotImplemented()

    def save_file(self, content):
        with open(self.filename, 'wb') as file:
            file.write(content)

    def download_complete(self):
        print(f'Download of {self.url} is completed!')

class ThreadingDownloader(Download):
    def start_download(self):
        thread = threading.Thread(target=self._start_downloading)
        thread.start()
        return thread        

    def _start_downloading(self):
        content = download_file(self.url)
        self.save_file(content)
        self.download_complete()


class MultiprocessingDownloader(Download):
    def start_download(self):
        process = multiprocessing.Process(target=self._start_download)
        process.start()
        return process
    
    def _start_download(self):
        content = download_file(self.url)
        self.save_file(content)
        self.download_complete()


class DownloadManager:
    def __init__(self, max_threads=3, max_processes=2):
        self.max_threads = max_threads
        self.max_processes = max_processes
        self.downloads = []
        self.after_start = []

    def download(self, url, filename):
        flag = input('Choose the way to download (Th or M): ')
        if flag == 'Th':
            download = ThreadingDownloader(url, filename)  
        elif flag == 'M':
            download = MultiprocessingDownloader(url, filename)  
        else:
            raise Exception('Not supported way for downloading')
        self.downloads.append(download)

    def start(self):
        thread_count, process_count = 0, 0
        for download in self.downloads:
            if isinstance(download, ThreadingDownloader):
                thread_count += 1
                if thread_count > self.max_threads:
                    raise Exception('Too many threads')
            elif isinstance(download, MultiprocessingDownloader):
                process_count += 1
                if process_count > self.max_processes:
                    raise Exception('Too many processes')
            self.after_start.append(download.start_download())


    def wait(self):
        for download in self.after_start:
            download.join()


def download_file(url):
    response = requests.get(url)
    return response.content
    

if __name__ == "__main__":
    download_manager = DownloadManager(max_threads=3, max_processes=2)

    download_manager.download("http://example.com/file1.txt", "file1.txt")
    # download_manager.download("ftp://example.com/file2.txt", "file2.txt")
    download_manager.download("http://example.com/file3.txt", "file3.txt")

    download_manager.start()
    download_manager.wait()

    print("All downloads completed!")
