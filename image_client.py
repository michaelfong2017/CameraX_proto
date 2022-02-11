#============================================================
# import packages
#============================================================
from concurrent import futures
import grpc
import cv2
import sys
sys.path.append("image")
import image_pb2 as service
import image_pb2_grpc as rpc
import uuid


#============================================================
# class
#============================================================



#============================================================
# property
#============================================================
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)




#============================================================
# functions
#============================================================
def Request(frame):

#print("origin size : ", sys.getsizeof(gray))

    ret, buf = cv2.imencode('.jpg', frame)

    if ret != 1:
        return

    # encode to base64
    b = buf.tobytes()
    #print("base64 encode size : ", sys.getsizeof(b64e))

    random_uuid = str(uuid.uuid4())
    metadata = service.Metadata(id=random_uuid, image_format="jpeg")
    yield service.ImageUploadRequest(metadata=metadata)
    yield service.ImageUploadRequest(image = b)


#====================
def run():

	channel = grpc.insecure_channel('localhost:50051')
	stub = rpc.ImageServiceStub(channel)

	while True:

		try:

			ret, frame = cap.read()
			if ret != 1:
				continue

			# cv2.imshow('Capture Image', frame)
			k = cv2.waitKey(1)
			if k == 27:
				break

			responses = stub.Upload(Request(frame))
			for res in responses:
				print(res)

		except grpc.RpcError as e:
			print(e.details())
			#break



#============================================================
# Awake
#============================================================



#============================================================
# main
#============================================================
if __name__ == '__main__':
	run()



#============================================================
# after the App exit
#============================================================
cap.release()
cv2.destroyAllWindows()
