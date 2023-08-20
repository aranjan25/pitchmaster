import numpy as np

class PitchEstimator:
	def __init__(self, audio: np.ndarray):
		self.audio = audio
	
	def get_pitch(self) -> float:
		pass
