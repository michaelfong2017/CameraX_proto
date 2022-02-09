#============================================================
# import packages
#============================================================
from concurrent import futures
import time
import cv2
import grpc
import base64
import numpy as np
import Datas_pb2
import Datas_pb2_grpc
import sys
import threading


#============================================================
# classes
#============================================================
class ShowVideoStream:

	img = None
	thread = futures.ThreadPoolExecutor(max_workers=1)

	#==========
	def start(self):
		print("start: " + threading.currentThread().getName())
		self.ShowWindow()

	#==========
	def set(self, img):
		self.img = img

	#==========
	def ShowWindow(self):
		print("ShowWindow: " + threading.currentThread().getName())
		while True:
			if self.img is not None:
				# print(self.img)
				cv2.imshow('dst Image', self.img)
				k = cv2.waitKey(1) & 0xFF
				if k == 27:
					break

			time.sleep(1/60)




#====================
class Greeter(Datas_pb2_grpc.MainServerServicer):

	#==========
	def __init__(self):
		pass

	#==========
	def getStream(self, request_iterator, context):
		print("getStream: " + threading.currentThread().getName())

		timer = time.time()

		for req in request_iterator:

			# print('process time = ' + str(time.time() - timer))
			timer = time.time()

			# decode from base64
			b64d = base64.b64decode(req.datas)
			#print("base64 decode size : ", sys.getsizeof(b64d))

			# base64 buffer to uint8
			dBuf = np.frombuffer(b64d, dtype = np.uint8)
			#print("buffer size : ", sys.getsizeof(dBuf))

			# decode to cv2
			dst = cv2.imdecode(dBuf, cv2.IMREAD_COLOR)
			#print("dst size : ", sys.getsizeof(dst))

			# set pixels
			show.set(dst)

			# success
			yield Datas_pb2.Reply(reply = 1)




#============================================================
# property
#============================================================
show = ShowVideoStream()



#============================================================
# functions
#============================================================
def serve():
	print("serve: " + threading.currentThread().getName())

	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	Datas_pb2_grpc.add_MainServerServicer_to_server(Greeter(), server)
	server.add_insecure_port('[::]:50051')
	server.start()

	print('===== server start =====')

	server.wait_for_termination()



#============================================================
# main
#============================================================
if __name__ == '__main__':
	print("main: " + threading.currentThread().getName())
	thread = threading.Thread(target=serve)
	thread.start()
	show.start()


#============================================================
# after the App exit
#============================================================
cv2.destroyAllWindows()
