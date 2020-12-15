import threading
import secrets

class Test():
  def __init__(self):
    self._threads = []

  def _create_thread(self, *args, **kwargs):
    thread = threading.Thread(*args, **kwargs)
    self._threads.append(thread)
    return thread

  def test_timestamps_are_unique(self):
    obtained = []

    def create_item():
        for i in range(100):
            obtained.append(secrets.randbits(128))

    thread1 = self._create_thread(target=create_item)
    thread2 = self._create_thread(target=create_item)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    if len(obtained) != 200:
      print("incorrect length")
    else:
      print("correct length")
    
    if len(set(obtained)) != len(obtained):
      print("duplicates found")
    else:
      print("no duplicates found")

if __name__ == "__main__":
  t = Test()
  t.test_timestamps_are_unique()