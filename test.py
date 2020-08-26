from SpeechModel251 import ModelSpeech
from LanguageModel2 import ModelLanguage
from keras import backend as K

def speech_recognition(f):
	datapath = '.'
	modelpath = 'model_speech' + '\\'

	ms = ModelSpeech(datapath)

	ms.LoadModel(modelpath + 'speech_model251_e_0_step_625000.model')
	r = ms.RecognizeSpeech_FromFile(f)

	K.clear_session()
	print('*[提示] 语音识别结果：\n',r)
	ml = ModelLanguage('model_language')
	ml.LoadModel()
	str_pinyin = r
	r = ml.SpeechToText(str_pinyin)
	print('语音转文字结果：\n',r)
	return r














