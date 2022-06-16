# Reconhecimento facial - como usar

Para que funcione o reconhecimento facia, vamos precisar de algumas bibliotecas e por isso, se preferir, é recomendado utilizar de um ambiente virtual para realizar testes.

## Para iniciar
- Vamos precisar do Pip


No linux: 
```
sudo apt-get install pip
```

- Agora vamos instalar o OpenCv


No linux: 
```
pip install opencv-python
```

- Instalamos o Bazel 


No linux:
```
npm install @bazel/bazelisk

```
Caso ocorra algum problema com esse comando, você precisa instalar o gerenciador npm do nodeJS. Você pode utilizar o comando:


No linux:
```
sudo apt install nodejs
```
Agora pode testar novamente.

- Vamos precisar insatalar o Medipipe e fazer um clone do seu repositório. Para isso utilize o comando: 
```
git clone https://github.com/google/mediapipe.git
```
Caso esse comando retorne algum erro, você precisará instalar o git. Para isso utilize o comando: 


No linux
```
sudo apt-get install git
```
Agora teste novamente o comando.

- Após a clonagem do repositório, nos entramos na pasta com o comando: 
```
cd mediapipe
```
E instalamos as seguintes dependências: 


No linux: 
```
sudo apt-get install -y \
    libopencv-core-dev \
    libopencv-highgui-dev \
    libopencv-calib3d-dev \
    libopencv-features2d-dev \
    libopencv-imgproc-dev \
    libopencv-video-dev
```

- Agora instalamos o Mediapipe:


No linux:
```
pip install mediapipe
```

- Por útimmo vamos precisar instalar o reconhecimento facial:


No linux:
```
pip install face_recognition
```


## Possíveis erros e suas soluções

Após a instalação das bibliotecas, podem ser que algumas outras bibliotecas auxiliares sejam necessárias mais na frente.

- TensorFlow


Caso apareça algum erro com esse comando você poderá resolver:


No linux:
```
pip install tensorflow==2.9.1\
```
Caso queira entender melhor o erro: 
https://exerror.com/typeerror-descriptors-cannot-not-be-created-directly/

- Dlib


Para erros com o delib nos podemos resolver apenas com sua instalação:


No linux:
```
sudo apt-get update
$ sudo apt-get install build-essential cmake
$ sudo apt-get install libopenblas-dev liblapack-dev 
$ sudo apt-get install libx11-dev libgtk-3-dev
$ sudo apt-get install python python-dev python-pip
$ sudo apt-get install python3 python3-dev python3-pip
```
Para saber mais, vá até a seção - Installing dlib on Ubuntu: 
https://pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/
