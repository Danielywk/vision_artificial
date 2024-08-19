# Usage example: python3 opencv_yolov3.py --image=test.png

import sys
import cv2
import argparse
import numpy as np
import os.path

# Inicialización de parámetros
# Umbral de similitud
confThreshold = 0.5  # Confidence threshold

# Umbral del algoritmo NMS
nmsThreshold = 0.4

# Ingrese el ancho y la altura de la imagen
inpWidth = 416
inpHeight = 416

parser = argparse.ArgumentParser(description='Object detection using YOLOv3 in opencv')
parser.add_argument('--image', help='Path to image file.')
args = parser.parse_args()

# Importar archivo de clase de objeto, soporte predeterminado 80 tipos
classesFile = "coco.names"
classes = None
with open(classesFile, 'rt') as f:
    classes = f.read().rstrip('\n').split('\n')

# yolo v3 archivo de configuración y pesos
modelConfiguration = "yolov3.cfg"
modelWeights = "yolov3.weights"

# opencv Leer modelo externo
net = cv2.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# Use CPU aquí, si desea usar GPU, el parámetro es DNN_TARGET_OPENCL, pero la versión actual solo admite GPU interna, si es otra GPU, cambiará automáticamente al modo CPU
net.setPreferableTarget(cv2.dnn.DNN_TARGET_OPENCL)


# Get the names of the output layers
def getOutputsNames(net):
    # Get the names of all the layers in the network
    layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
    return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]


# Dibujar cuadro delimitador
def drawPred(classId, conf, left, top, right, bottom):
    # Draw a bounding box.
    cv2.rectangle(frame, (left, top), (right, bottom), (255, 178, 50), 3)

    label = '%.2f' % conf

    # Get the label for the class name and its confidence
    if classes:
        assert (classId < len(classes))
        label = '%s:%s' % (classes[classId], label)

    # Display the label at the top of the bounding box
    labelSize, baseLine = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
    top = max(top, labelSize[1])
    cv2.rectangle(frame, (left, top - round(1.5 * labelSize[1])), (left + round(1.5 * labelSize[0]), top + baseLine),
                  (255, 255, 255), cv2.FILLED)
    cv2.putText(frame, label, (left, top), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 0), 1)


# Use el algoritmo NMS para descartar el cuadro delimitador de baja similitud
def postprocess(frame, outs):
    frameHeight = frame.shape[0]
    frameWidth = frame.shape[1]

    classIds = []
    confidences = []
    boxes = []
    # Scan through all the bounding boxes output from the network and keep only the
    # ones with high confidence scores. Assign the box's class label as the class with the highest score.
    classIds = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                center_x = int(detection[0] * frameWidth)
                center_y = int(detection[1] * frameHeight)
                width = int(detection[2] * frameWidth)
                height = int(detection[3] * frameHeight)
                left = int(center_x - width / 2)
                top = int(center_y - height / 2)
                classIds.append(classId)
                confidences.append(float(confidence))
                boxes.append([left, top, width, height])

    # Perform non maximum suppression to eliminate redundant overlapping boxes with
    # lower confidences.
    indices = cv2.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
    for i in indices:
        i = i[0]
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        drawPred(classIds[i], confidences[i], left, top, left + width, top + height)


# Process inputs
winName = 'Deep learning object detection in OpenCV'
cv2.namedWindow(winName, cv2.WINDOW_NORMAL)

if (args.image):

    if not os.path.isfile(args.image):
        print('Input image file {} does not exist.'.format(args.image))
        sys.exit(1)
    frame = cv2.imread(args.image, cv2.IMREAD_ANYCOLOR)
    outputFile = args.image[:-4] + '/Users/isa/Pictures/Reconocimiento/Angel1.mp4'

    # Create a 4D blob from a frame.
    blob = cv2.dnn.blobFromImage(frame, 1 / 255, (inpWidth, inpHeight), [0, 0, 0], 1, crop=False)

    # Sets the input to the network
    net.setInput(blob)

    # Runs the forward pass to get output of the output layers
    outs = net.forward(getOutputsNames(net))

    # Remove the bounding boxes with low confidence
    postprocess(frame, outs)

    cv2.imshow(winName, frame)
    cv2.imwrite(outputFile, frame)
    cv2.destroyAllWindows()