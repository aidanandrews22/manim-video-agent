import threading
import time
from datetime import datetime, timedelta
import sys

class BackgroundTimer:
    def __init__(self, prefix="Elapsed time: "):
        self.running = False
        self.timer_thread = None
        self.start_time = None
        self.prefix = prefix
        self.last_print_length = 0
        self._lock = threading.Lock()
    
    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.timer_thread = threading.Thread(target=self._run_timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()
    
    def stop(self):
        self.running = False
        if self.timer_thread and self.timer_thread.is_alive():
            self.timer_thread.join(timeout=1.0)
        
        # Clear the last timer line
        with self._lock:
            sys.stdout.write('\r' + ' ' * self.last_print_length + '\r')
            sys.stdout.flush()
    
    def _run_timer(self):
        while self.running:
            elapsed = time.time() - self.start_time
            elapsed_td = timedelta(seconds=int(elapsed))
            
            # Format as HH:MM:SS
            timer_display = f"{self.prefix}{elapsed_td}"
            
            with self._lock:
                # Clear previous line
                sys.stdout.write('\r' + ' ' * self.last_print_length + '\r')
                # Write new timer
                sys.stdout.write(timer_display)
                sys.stdout.flush()
                self.last_print_length = len(timer_display)
            
            time.sleep(1)  # Update every second