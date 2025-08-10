import os
import numpy as np
import librosa
from django.shortcuts import render
from django.conf import settings
from tensorflow.keras.models import load_model
import joblib

model = load_model(os.path.join(settings.BASE_DIR, 'audioclassificationapp', 'saved_models', 'audio_classification_cnn.keras'))
label_encoder = joblib.load(os.path.join(settings.BASE_DIR, 'audioclassificationapp', 'labelencoder.pkl'))

def predict_audio(request):
    emotion = None
    audio_url = None

    if request.method == 'POST' and request.FILES.get('audio'):
        audio_file = request.FILES['audio']
        filename = audio_file.name  
        audio_path = os.path.join(settings.MEDIA_ROOT, filename)

        with open(audio_path, 'wb+') as destination:
            for chunk in audio_file.chunks():
                destination.write(chunk)

        y, sr = librosa.load(audio_path, sr=22050)
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        mfccs_scaled = np.mean(mfccs.T, axis=0)
        feature = mfccs_scaled.reshape(1, -1)

        LABEL_MAPPING = {
            1: "neutral",
            2: "calm",
            3: "happy",
            4: "sad",
            5: "angry",
            6: "fearful",
            7: "disgust",
            8: "surprised" 
        }

        prediction = model.predict(feature)
        predicted_label = np.argmax(prediction, axis=1)


        emotion = LABEL_MAPPING.get(predicted_label[0], "Unknown")


  
        audio_url = os.path.join(settings.MEDIA_URL, filename)

    return render(request, 'audioclassificationapp/index.html', {
    'emotion': emotion,
    'audio_url': audio_url
})




