# Reconhecimento facial 

def reconhecer_face() : 
    try : 
        import cv2
        import time
    
        camera_port = 0
        nFrames = 30
        camera = cv2.VideoCapture(camera_port)
        file = "./unknow_pictures/unknow.png"      
        emLoop= True
        
        while(emLoop):
        
            retval, img = camera.read()

            cv2.imwrite(file,img)
            emLoop= False
        cv2.destroyAllWindows()
        camera.release()
    except : 
        return 0
    else : 
        return 1

# Rechonhecimento facial acaba aqui 

# Localizando rostos na imagem lida 

def localizar() : 
    try : 
        from PIL import Image
        import face_recognition

        image = face_recognition.load_image_file("unknow_pictures/unknow.png")

        face_locations = face_recognition.face_locations(image)

        print("I found {} face(s) in this photograph.".format(len(face_locations)))

        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location

            # You can access the actual face itself like this:
            face_image = image[top-85:bottom+40, left-35:right+30]
            pil_image = Image.fromarray(face_image)
            pil_image.save("./unknow_pictures/unknow.png", quality=95)
    except : 
        return 0
    else : 
        return 1

# Termina de localizar os rostos na imagem

# Inicia o processo de identificação

def identificar() :
    try :
        import os
        import face_recognition

        os.system("face_recognition ./pictures ./unknow_pictures/unknow.png > result.txt")

        image = face_recognition.load_image_file("unknow_pictures/unknow.png")
        face_locations = face_recognition.face_locations(image)

        with open("result.txt") as result:
            for lines in result:
                break
            if len(face_locations) == 0: 
                print("Nenhuma pessoa encontrada, caso esteja de máscara, por favor, retírea")
            elif lines[:43] == "./unknow_pictures/unknow.png,unknown_person":
                print("Unknow people")
            else :
                print("People that i know")
    except : 
        return 0
    else : 
        return 1