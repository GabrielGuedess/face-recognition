import face_recognition as fr


def compare_faces(file1, file2):
    image1 = fr.load_image_file(file1)
    image2 = fr.load_image_file(file2)

    image1_encoding = fr.face_encodings(image1)[0]
    image2_encoding = fr.face_encodings(image2)[0]

    results = fr.compare_faces([image1_encoding], image2_encoding)
    return results[0]
