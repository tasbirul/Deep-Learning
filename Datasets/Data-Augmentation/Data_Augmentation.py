import os
import numpy as np
from PIL import Image

class Augmentation(object):
	def __init__(self, data_dir, flip=True):
		super(Augmentation, self).__init__()
		self.data_dir = data_dir
		self.flip = flip
		self.array_data = []
		self.flip_data = []
		self.augment_data = []
		self.shifting_rate = 1e-1

	def get_data(self):
		try:
			return os.listdir(self.data_dir)
		except FileNotFoundError as e:
			print("Error! Directory Not Found ")

	def data2array(self):
		data_list = self.get_data()
		for data in data_list:
			img = Image.open(os.path.join(self.data_dir, data))
			img = np.array(img)
			img = img[:,:,:3]
			self.array_data.append(img)
			self.augment_data.append(img)

	def flipped(self):
		for data in self.array_data:
			flipped_img = np.fliplr(data)
			self.flip_data.append(flipped_img)
			self.augment_data.append(flipped_img)

	def Shift_Top_left(self, data):
		self.augment_data.append(data[:-int(data.shape[0] * self.shifting_rate),
									  :-int(data.shape[0] * self.shifting_rate)])
    	

	def Shift_Bottom_Right(self, data):
		self.augment_data.append(data[:int(data.shape[0] * self.shifting_rate),
									   int(data.shape[0] * self.shifting_rate):])

	def Shift_Center(self, data):
		self.augment_data.append(
						data[int(data.shape[0] * self.shifting_rate / 2):-int(data.shape[0] * self.shifting_rate / 2),
							 int(data.shape[0] * self.shifting_rate / 2):-int(data.shape[0] * self.shifting_rate / 2)])
        
            
	def main(self):
		self.get_data()
		self.data2array()

		if self.flip == True:
			self.flipped()
			for flip_img in self.flip_data:
				self.Shift_Top_left(flip_img)
				self.Shift_Bottom_Right(flip_img)
				self.Shift_Center(flip_img)

		for iter_data in self.array_data:
			self.Shift_Top_left(iter_data)
			self.Shift_Bottom_Right(iter_data)
			self.Shift_Center(iter_data)

if __name__ == '__main__':
	data_path = './data'
	arg = Augmentation(data_path)
	arg.main()