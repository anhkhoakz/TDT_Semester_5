import os
import psutil


class MemoryLogger:
    _instance = None

    def __init__(self):
        self.max_memory = 0
        self.recording_mode = False
        self.output_file = None
        self.writer = None

    @staticmethod
    def get_instance():
        if MemoryLogger._instance is None:
            MemoryLogger._instance = MemoryLogger()
        return MemoryLogger._instance

    def get_max_memory(self):
        return self.max_memory

    def reset(self):
        self.max_memory = 0

    def check_memory(self):
        current_memory = psutil.Process(os.getpid()).memory_info().rss / (1024 * 1024)
        if current_memory > self.max_memory:
            self.max_memory = current_memory
        if self.recording_mode and self.writer:
            self.writer.write(f"{current_memory}\n")
        return current_memory

    def start_recording_mode(self, file_name):
        self.recording_mode = True
        self.output_file = file_name
        self.writer = open(self.output_file, "w")

    def stop_recording_mode(self):
        if self.recording_mode and self.writer:
            self.writer.close()
        self.recording_mode = False
