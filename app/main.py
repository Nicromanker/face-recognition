import cv2
import face_recognition
import numpy as np
import os

video_name = 'test2.mp4'

# Lets learn all of our faces
directory = os.fsencode('app/images')

known_face_encoding = []
known_face_names = []

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith('.jpg'):
        person_image = cv2.cvtColor(cv2.imread(
            f'app/images/{filename}'
        ), cv2.COLOR_BGR2RGB)
        print('Studing file ' + filename)
        person_face_encoding = face_recognition.face_encodings(person_image)[0]

        known_face_encoding.append(person_face_encoding)
        known_face_names.append(filename.split('.')[0])


# Define some variables
face_locations = []
face_encodings = []
process_current_frame = True

capture = cv2.VideoCapture(f'app/videos/{video_name}')

width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv2.CAP_PROP_FPS))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

storage = cv2.VideoWriter(
    f'app/output/{video_name}',
    fourcc,
    fps,
    (width, height)
)

while True:

    ret, frame = capture.read()

    if ret:
        face_names = []
        if process_current_frame:

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame,
                face_locations
            )

            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(
                    known_face_encoding,
                    face_encoding
                )
                name = "Unknown"

                face_distances = face_recognition.face_distance(
                    known_face_encoding,
                    face_encoding
                )
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                face_names.append(name)

        process_current_frame = not process_current_frame
        for (top, right, bottom, left), name in zip(
            face_locations,
            face_names
        ):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(
                frame,
                (left, bottom - 35),
                (right, bottom),
                (0, 0, 255),
                cv2.FILLED
            )
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(
                frame,
                name,
                (left + 6, bottom - 6),
                font,
                1.0,
                (255, 255, 255),
                1
                )

        storage.write(frame)
    else:
        break

capture.release()
storage.release()
cv2.destroyAllWindows()
